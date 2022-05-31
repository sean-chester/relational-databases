# CSC 370 - Conceptual Data Modelling Assignment

## Assignment Goals

In this assignment you will:

  * demonstrate knowledge of conceptual data modelling and the SQL DDL

    + convert entity-relationship diagrams into a logical model
    + implement a model in a relational database with SQL

## Task

You should write a computer program in python (or another programming language with prior approval of the instructor) that will take as input an entity-relationship diagram (ERD) and print out to the standard output stream a series of SQL DDL queries (i.e., CREATE TABLE statements) that populates an empty MySQL database with a set of tables that match the ERD.

You have been provided with an ERD class that can be directly instantiated, even for complex examples like the one shown below. You are also provided with a Database class that has methods for comparing two databases for equality and for printing out CREATE TABLE statements. There is only one function missing, the one that you should implement, which converts an arbitrary ERD instance into a corresponding Database instance.

You will need to handle all concepts introduced in the lessons (e.g., weak entity sets, subclass hierarchies, many-many relationships), but you should assume that every one-many and many-one relationship requires referential integrity. You should not modify any identifiers. For simplicity, we have made every attribute of data type INT and avoided use of specifiers like "AUTOINCREMENT" and NOT NULL.

You _do not need to write any scripts_ for this assignment. We have instead wrapped all the code in a unit testing framework and we will directly probe the objects that you create by creating mock objects as solutions and using the provided equality comparator to determine whether you have the same solution. Where order is not important as per the SQL standard, we use set-based comparisons; where it is important, we check order. You can verify this by inspecting the comparators.

The starter code, test harness, and README with build instructions has been shipped out in both C++ and Python and attached as a compressed archive to this assignment description. We anticipate releasing Java code, too, but will not extend the deadline due to delays with its release. For specific build and run instructions, refer to the relevant README.

## Submission

You should only submit one .py file, uncompressed, which implements the convert_to_table() function with the exact signature provided.

## Evaluation

We will swap out the test file with a new set of unit tests and assign a grade of pass (1) or fail (0) for each assertion that you pass. If your code takes more than five minutes on a single test, it may be terminated before the test finishes, resulting in a fail on that test. Your grade on the assignment will be the number of tests passed. There will be a total of twenty-two tests, each worth 5%; so, it is possible to score a maximum grade of 110% on this assignment.

The current code release is in "beta" state because we will provide more sample tests.

## Sources

You are permitted to use sources that you find on the Internet, so long as it is clear that the source existed prior to the creation of this assignment and you provide a citation in your source code. For example, GitHub and StackOverflow content is permitted, so long as they are clearly dated prior to the beginning of this semester. If you do not include a citation in your source code, your work will be considered plagiarism.

You should, however, work through the assignment on your own. You are welcome to prepare for the assignment with peers in the class by working through the ungraded worksheets together.

## Illness Policy

The end date for the assignment is three days later than the due date. This is expected to provide sufficient contingency for most minor illnesses and you should submit by the due date rather than the end date if you are not constrained by illness.

In the event that three days contingency is insufficient, you could contact the instructor in advance of the due date with a brief explanation. If you have submitted all previous, graded assignments, then your quiz for this module will be used as the assessment for these learning outcomes. If, on the other hand, you have a missing assignment due to, for example, prior illness this semester, then a well-justified second absence longer than three days we be accommodated with a make-up assessment in the form of an individual, closed, recorded oral exam over Zoom conducted by the instructor. The use of make-up assessments will help to ensure that there are sufficiently many assessment activities (at least 80% of the grade) for each student to accurately reflect their achievement in this course.

You are encouraged to submit your preliminary progress one week and again three days prior to the assignment deadline to document progress in case of illness. These preliminary submissions can, of course, be overwritten by your final submission.

## Summary

I hope that this assignment is a fun way to work through the systematic translation of ERD's into databases. Good luck!
