
import os

def extract_student_id(dirname):
    st_num_pos = dirname.find(" - V")
    if st_num_pos == -1:
        raise RuntimeError(f"No student number in the folder name {dirname.decode()}")

    return dirname[st_num_pos+3:st_num_pos+3+9]


def load_submission_folders(current_path, assignment_path):
    assignment_directory = os.fsencode(args.path + "/" + args.assignment)
    submission_folders = {extract_student_id(sub_dir.decode()): assignment_directory.decode() + "/" + sub_dir.decode() for sub_dir in os.listdir(assignment_directory)}
    return submission_folders


class StudentReader:
    def __init__(self, current_path, assignment_path):
        self.submission_folders = load_submission_folders(current_path, assignment_path)

    def get_folder_map(self):
        return self.submission_folders
