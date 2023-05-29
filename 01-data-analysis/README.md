# CSC 370 - SQL Golf

## Assignment Goals

In this assignment you will:

  * demonstrate data analysis skills with SQL

    + write SQL queries with varied complexity to extract desired information from a relational database
    + optimise SQL queries towards simplicity

## Task

[Code Golf](https://www.barrymichaeldoyle.com/code-golf/) is a sort of recreational programming activity in which one tries to implement functionality using as few characters as possible. The general goal is to think of alternative solutions to a problem and it derives its name from the sport of _golf_, in which one tries to minimise the number of whacks with an iron shaft to put a tiny ball in a far-flung hole. In this assignment, you will try not just to write SQL queries that are correct, but that also are "minimal." 

As an example, imagine that you have two relations: *Employee(<ins>employee_id</ins>, employee_name, dept_id)* and *Department(<ins>dept_id</ins>, dept_name)* and you would like to find the names of all employees in a department named "Shipping & Receiving". A simple solution would be:

```sql
SELECT `employee_name`
FROM `Employee`
    NATURAL JOIN `Department`
WHERE `dept_name` LIKE 'Shipping \& Receiving';
```

Certainly, another "correct" solution would be:

```sql
SELECT `employee_name`
FROM `Employee`
WHERE `dept_id` IN (
    SELECT `dept_id`
    FROM `Department`
    WHERE `dept_name` LIKE 'Shipping \& Receiving' );
```

Both queries retrieve the same result, but the second query is unnecessarily complex, or at the very least non-idiomatic. I hope that you prefer the first solution. Even if not, this assignment is designed to encourage you to write the first query by rewarding you inversely to the number of times any of the following tokens appears in your SQL query:

  * SELECT (i.e., projection operator)
  * FROM (i.e., the table- or index-scan operator)
  * , (i.e., the cross product operator, _including other appearances such as in a SELECT clause_)
  * JOIN (i.e., a theta-, natural, or outer join or per MySQL an intersection)
  * UNION (i.e., the bag union operator)
  * DISTINCT (i.e., the duplicate elimination operator)
  * GROUP (i.e., the group-by operator)
  * ORDER (i.e., the sort operator)
  * HAVING (i.e., the selection operator applied to groups)
  * WHERE (i.e., the selection operator applied to tuples)
  * LIMIT (i.e., the MySQL top-k operator)

This gives us a metric by which to claim the first query is better: it only uses 4 instances of the above set of operators (SELECT, FROM, JOIN, and WHERE), whereas the second query uses 6 instances (2×SELECT, 2×FROM, 2×WHERE). This is the metric that you should aim to minimise with the SQL queries that you submit. You would receive more marks for the first query than the second one.

It is important to remember that this is an exercise in code simplification and creative thinking, not in performance optimisation. Although you are trying to minimise the number of operator references, SQL is a _declarative language_ and there is no specific reason to assume that the first example query will run faster than the second one. However, simple and idiomatic code is easier for compilers to optimise; so, there could be tangential performance benefits to striving for simpler—or at least shorter—queries. _The real intent here is to leverage an assumed correlation between this "golf score" metric and the quality of a SQL query to encourage you to write better SQL_.

You are given instructions to create (optionally) a MySQL database or to connect to one on a remote server. Moreover, you are given ten `.sql` files that are unfortunately empty except for a comment indicating their intended query and their mapping between "SQL Golf" scores (i.e., total instances of the aforementioned operators/tokens) and grade. For example, the above problem would be represented by the following `example.sql` file:

```sql
-- Find the names of all employees in a department named "Shipping & Receiving"
-- 1.1 marks: <4 operators
-- 1.0 marks: <6 operators
-- 0.8 marks: correct answer

```

Alongside the `.sql` file will be a `.tsv` file showing the expected result, which you can use for testing.


## Submission

You should submit all ten of the `.sql` files _without renaming them_, but after replacing the final empty line with an actual SQL query that achieves the stated objective. Ordinarily, you should submit ten `.sql` files, though it is okay to submit fewer files if you do not have a solution for all ten tests.

## Evaluation

Your grade on the assignment will be the sum of your scores on each query. This could be in excess of 10 (i.e., full marks), particularly if you minimise your queries more effectively than the teaching team has. However, to receive any marks on a particular query, you *must* produce the correct result, including attribute names. We will ascertain this by performing a `diff` between the corresponding `.tsv` file and your query results on an up-to-date MySQL instance prior to counting operators, similar to:

```bash
sudo mysql -u root counties < query01.sql > query01-your-solution.tsv
diff query01-solution.tsv query01-your-solution.tsv
```

In the running example, the first query would score 1.0 marks and the second query would score 0.8 marks. If you can answer the query with fewer operator instances than the first query, you would score 1.1 marks. The following query would obtain 0.0 marks, even though the number of operators is small, because it does not produce the same result (namely, it doesn't filter by department):

```sql
SELECT `employee_name`
FROM `Employee`;
```

Note that we may modify our testing dataset to avoid hard-coded solutions, such as by changing the id values of or deleting tuples. You should not make assumptions (e.g., of uniqueness or non-nulls) that are not supported by the data model in the CREATE TABLE statements below. Moreover, if you create temporary files, you are responsible for monitoring their existence: there is no guarantee that we will run queries in numerical order.

Pre-marking will occur at an arbitrary point in the morning on the following dates. You should submit prior to midnight the night before to be certain to receive a pre-grading update:

  * Wednesday, 31 May 2023
  * Monday, 5 June 2023

## Dataset

For this assignment, we will use [a compilation of US county-level census data](https://github.com/evangambit/JsonOfCounties) that has been transformed from a document-oriented to a relational format for the purpose of this assignment. The data has been loaded into MySQL and [exported into .sql format](./counties.sql). You can import it into your local instance of MySQL from the command line as follows:

```bash
mysql -u [username] -p counties < counties.sql
```

(Or, you could simply copy-paste the whole file into a query window and execute it.)


## Queries

The queries are available in two locations:

  * You can access them on [the public-facing GitHub repo](https://github.com/sean-chester/relational-databases/01-data-analysis) for this course's assignments. The advantages to this source are that it is the freshest (first place updates are pushed) and that you can directly check out the code with `git`, which might be an easier toolchain
  * You can access them by downloading the compressed tarball that is attached to this assignment description and unpack it locally.

Remember to edit and upload the `.sql` files and to use the `.tsv` files to check the correctness of your solutions.


## Sources and Academic Integrity

_This assignment is equivalent to an in-person, solo, written exam_. As such, it must be completed independently, even the development of general ideas or pseudocode. Submissions may be subjected to plagiarism detection software and evidence of collaboration will be reported as an Academic Integrity infringement. You are welcome to prepare for the assignment with peers in the class by working through the in-class problems together or studying the practice quizzes, which are designed to prepare you well for this assignment.

You are permitted to use sources that you find on the Internet, so long as the source is clearly dated with a last edit prior to 1-January-2023 and you provide a citation in your source code. For example, GitHub and StackOverflow content is permitted, so long as it is clearly dated prior to this year. The use of Generative AI tools must also be cited. (Clearly, it has a last edit of whenever you used it). If you do not include a citation as a comment in your source code, your work will be considered plagiarism.


## Illness, Lateness, Technical Issues, and Personal Circumstances

Submissions will be accepted until the _end date_ of the assignment listed in Brightspace, which provides a three day buffer to address most challenges that are likely to arise. Note that support for the assignment will not be available after the deadline, however. Submissions will not be accepted after the _end date_; if you have not submitted code by then, whether by choice or circumstances, the weight for this assignment will be shifted to the corresponding midterm exam.

## Summary

I hope that this assignment is a fun way to learn and/or practice the SQL query language. Good luck!
