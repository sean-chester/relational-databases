# CSC 370 - Data Model Checker

## Assignment Goals

In this assignment you will:

  * demonstrate data modelling skills with a combination of SQL and python

    + write SQL queries to inspect the model of a MySQL database
    + write python code to connect to a MySQL database and handle the output of queries, including exception handling

## Task

A well implemented relational database should enforce all the constraints that were identified (even implicitly) during the design phase, such as the functional dependencies, the check constraints, and the referential integrity. In this assignment, we will write generic testing software that confirms whether an implementation of a database design is correct. You will write a series of tester functions in python that connect to a MySQL database and probe it to check whether a given constraint is being enforced correctly.

As an example, imagine that you have two relations: *Employee(<ins>employee_id</ins>, employee_name, dept_id)* and *Department(<ins>dept_id</ins>, dept_name)*. Naturally, we might expect in this case that a SQL query like the following should only return one row per employee:

```sql
SELECT *
FROM `Employee`
    NATURAL JOIN `Department`;
```

If this is not the case, we can be confident that Department.dept_id has not been set up as a primary key; if it were, it should not be possible for more than one Department tuple to match each Employee on dept_id. If you designed a function that could take in two relations likes this and the foreign key relationship between them, you could connect to a database and check that this behaviour is as expected.

Unfortunately, this example above only shows that a primary key _does not_ exist; it is insufficient to conclude that the primary key _has_ been created. You would need a better test design to be confident that you will score full marks on this assignment. As a strong hint, you may find that queries that modify the contents of tables combined with exception handling in your python code will be a more robust approach, though it certainly isn't the only one.

Specifically, you are given a python library, `DataModelChecker.py`, to implement. The API has already been exposed but none of the functions contain bodies yet. You should implement these six functions so that they can be used to test the correctness of any MySQL implementation of a relational database design.

It is important to remember that this is an exercise in software testing and creative thinking. You will probably want to create your own sandbox MySQL database and try out different table definitions to improve test coverage.


## Submission

You should submit `DataModelChecker.py` _without renaming it_, after implementing the six functions that contain TODO comments in their bodies. You are welcome to add other classes and auxiliary functions to support your solution (and improve code quality), but these must all appear in the same `DataModelChecker.py` file that you submit.

## Evaluation

Your functions will be evaluated with a series of unit tests and your score on the assignment will be the number of unit tests that you pass. Each test will run your function with a boundary case input against a localhost MySQL database.

For example, a test of `confirmSuperkey()` might pass as input a table for which no primary key was ever defined in the database and ask if a particular set of attributes is an enforced superkey or not, i.e., allows insertions that violate the supposed key constraint. If the function returns false, the test passes; otherwise it fails. Approximately twenty such test cases will be defined and tested.

Note that we will modify our testing dataset to avoid hard-coded solutions, such as by changing constraints between the pre-test and test database. You should not make assumptions that a hard-coded solution that passes pre-testing will also pass in the final evaluation. Moreover, if you create temporary files, you are responsible for monitoring their existence: there is no guarantee that we will run test cases in a deterministic order.

A subset of the test cases will be provided after the first pre-marking; however, these are only _structurally_ correct. The underlying database and therefore also the correct answer will change with 50% probability between what is provided and the final grading. You will need to also identify some important boundary cases to test that have not been released in advance.

Pre-marking will occur at an arbitrary point in the morning on the following dates. You should submit prior to midnight the night before to be certain to receive a pre-grading update:

  * Monday, 10 July 2023
  * Monday, 17 July 2023

## Dataset

For this assignment, we will use random data to test your code. It will be engineered to test particular boundary cases in the lessons. Functional dependencies may cross multiple tables, though these will share common attributes that facilitate NATURAL JOIN.


## Sources and Academic Integrity

_This assignment is equivalent to an in-person, solo, written exam_. As such, it must be completed independently, even the development of general ideas or pseudocode. Submissions may be subjected to plagiarism detection software and evidence of collaboration will be reported as an Academic Integrity infringement. You are welcome to prepare for the assignment with peers in the class by working through the in-class problems together or studying the practice quizzes, which are designed to prepare you well for this assignment.

You are permitted to use sources that you find on the Internet, so long as the source is clearly dated with a last edit prior to 1-January-2023 and you provide a citation in your source code. For example, GitHub and StackOverflow content is permitted, so long as it is clearly dated prior to this year. The use of Generative AI tools must also be cited. (Clearly, it has a last edit of whenever you used it). If you do not include a citation as a comment in your source code, your work will be considered plagiarism.


## Illness, Lateness, Technical Issues, and Personal Circumstances

Submissions will be accepted until the _end date_ of the assignment listed in Brightspace, which provides a three day buffer to address most challenges that are likely to arise. Note that support for the assignment will not be available after the deadline, however. Submissions will not be accepted after the _end date_; if you have not submitted code by then, whether by choice or circumstances, the weight for this assignment will be shifted to the corresponding midterm exam.

## Summary

I hope that this assignment is a fun way to learn and/or practice data modelling, the SQL query language, and connecting to MySQL databases from a high-level, application-layer code base. Good luck!
