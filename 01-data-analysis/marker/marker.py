#!/usr/bin/en python3
"""
MySQLMarker.py: Marking SQL Scripts for CSC370
pip3 install tqdm
"""

from token_counter import TokenCounter
from mysql_runner import MySQLRunner
from student_reader import StudentReader
from file_differ import compare_outputs

import sys
import csv
from tqdm import tqdm
import argparse
import traceback
import json


def setup_arg_parser():
    parser = argparse.ArgumentParser(description='Marking SQL assignment for CSC370')
    parser.add_argument('--path', dest='path', default="./submissions", help='Base path of submissions', required=False)
    parser.add_argument('--results-path', dest='expected_results', default=".", help='Path to the expected/correct results', required=False)
    parser.add_argument('--assignment-path', dest='assignment_path', default='..', help="Relative path to root of assignment directory", required=False)
    parser.add_argument('--database', dest='database', default='counties', help="Database Name", required=False)
    parser.add_argument('--db-user', dest='db_user', default='root', help="Database User Name", required=False)
    parser.add_argument('--scoring-file', dest='scoring_file', default='./scoring-function.json', help="JSON-structured map from query+tokens->grade", required=False)
    parser.add_argument('--blacklist', dest='blacklist', default='./a3/Blacklist-A3.json', help="Students input that breaks the process and needs to blacklisted", required=False)
    parser.add_argument('--marks-output', dest='marks_output', default='./student-grades.csv', help="Output marks in csv format", required=False)
    parser.add_argument('--sql-tokens', dest='sql_tokens', default='./sql-tokens.txt', help="MySQL tokens file", required=False)

    return parser


def load_scorer(scoring_file):
    scorer = {}
    with open(scoring_file) as fp_scorer:
        scorer = json.load(fp_scorer)

    return scorer


def load_results_files(query_count, expected_results_path):
    results = {} 
    for i in range(1, query_count + 1):
        with open(f"{args.results_path}/query{i:02}-result.tsv") as fl:
            results[i] = [l.strip() for l in fl.readlines()]

    return results


def init_output_csv(query_count, student_grade_file):
    queries = range(1, query_count + 1)
    cols = ["StudentID"]
    cols.extend([f"query{i:02}" for i in queries])
    cols.extend([f"tokens{i:02}"for i in queries])
    cols.extend([f"mark{i:02}"for i in queries])
    cols.extend(["Final"])
    with open(student_grade_file, 'w', newline='\n') as csvfile:
        writer = csv.DictWriter(csvfile,
                                fieldnames=cols,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        return (writer, csvfile)


class GradeRow:
    def __init__(self, student_id):
        self.row = {"StudentID": student_id}

    def set_query_score(self, query_number, token_count, score):
        self.row[f"tokens{query_number:02}"] = token_count
        self.row[f"query{query_number:02}"] = score

        row[f"query{i:02}"] = -1 # Default to error value
        row[f"tokens{i:02}"] = -1 # Default to error value
        row[f"mark{i:02}"] = 0

    def set_final_score(self, final_score):
        self.row["Final"] = final_score

    def flush_row(self, writer, csvfile):
        writer.writerow(self.row)
        csvfile.flush()


class SQLGolfMarker:
    def __init__(self, scoring_file, sql_tokens, expected_results_path, student_grade_file):
        self.score_function = load_scorer(scoring_file)
        self.query_count = len(self.score_function)
        self.token_counter = TokenCounter(sql_tokens)
        self.expected_results = load_results_files(self.query_count, expected_results_path)
        self.writer, self.csvfile = init_output_csv()

    def get_query_count(self):
        return self.query_count

    def compute_token_count(self, query_submission_filename):
        return self.token_counter.count_tokens(query_submission_filename)

    def compute_diff_and_score(self, query_number, token_count):
        output, errors = mysql_runner.run_query(query_submission_filename)

        if errors:
            return (-1, 0)

        diffs = len(compare_outputs(results[i], output))
        if(diffs > 0):
            return (diffs, 0)

        for tokens, score in self.score_function[f"query{query_number:02}"].items():
            if token_count < int(tokens):
                return (0, score)

        # this line should be unreachable if the JSON file is set up correctly
        assert(0)

    def grade_all(self, student_reader, mysql_runner):
        with tqdm(total=len(submissionFolders)*self.get_query_count()) as progress_bar:
            for student_id, folder in student_reader.get_folder_map().items():
                student_csv_row = GradeRow(student_id)
                total_grade = 0

                for i in range(1, self.get_query_count()+1):
                    progress_bar.set_description("Processing %s" % f"{student_id}, Query {i:02}")
                    inputfile = f"{folder}/query{i:02}.sql"

                    token_count = self.get_token_count(inputfile)
                    diff, score = self.get_diff_and_score(i, token_count)
                    total_grade = total_grade + score
                    student_csv_row.write_score(i, token_count, diff, score)
                    progress_bar.update(1)

                student_csv_row.set_final_score(total_grade)
                student_csv_row.flush_row(self.writer, self.csvfile)


                # write the marks to file 
                # with open(f"{folder}/feedback-marking-{st_id}.json", 'w') as f_mark:
                #    f_mark.write( json.dumps(student_csv_row.row, indent=4) )


if __name__ == '__main__':
    parser = setup_arg_parser()

    try:
        args = parser.parse_args()
        marker = SQLGolfMarker(args.scoring_file, args.sql_tokens, args.expected_results, args.marks_output)
        marker.grade_all( \
            StudentReader(args.path, args.assignment_path), \
            MySQLRunner(args.database, args.db_user))

    except Exception as e:
        print(">>>>>>>>>>>>>>>> Major Error")
        print(traceback.format_exc())
