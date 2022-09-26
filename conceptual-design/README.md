# CSC 370 - Conceptual Data Modelling Assignment

## Assignment Goals

In this assignment you will:

  * demonstrate knowledge of conceptual data modelling, generalisation abstractions, and cardinality constraints

    + interpret entity-relationship diagrams
    + understand identifiers
    + determine how entity sets are transitively related to each other 

## Task

You should write a computer program in python (or another programming language with prior approval of the instructor) that will take as input an entity-relationship diagram (ERD) and two sets of attributes and identify the lower and upper bounds on the number of ways those attributes can be combined.

You have been provided with an ERD class that can be directly instantiated. There is only one function missing, the one that you should implement, which calculates the range of bounds.

You will need to handle all concepts introduced in the lessons (e.g., weak entity sets, subclass hierarchies, many-many relationships). You should not modify any identifiers.

The starter code, test harness, and README with build instructions has been shipped out in Python and attached as a compressed archive to this assignment description. For specific build and run instructions, refer to the relevant README.

## Submission

You should implement the (empty) function called `calculate_bounds()` in `cardinalities_bounds.py` and then submit the single file `cardinalities_bounds.py`. You are welcome to add auxillairy ("helper") functions, so long as they are in the `cardinalities_bounds.py` file that you submit.  

## Evaluation

Included with the starter code is an incomplete set of unit tests (`tests.py`). This imports your `cardinalities_bounds.py` code. To evaluate your submission, we will use a marking script that will run `python3 tests.py` and count the percentage of unit tests that your code passes. This percentage will be your grade on the assignment. You are expected to design some test cases yourself to improve test coverage, though we will evaluate your submission with our own test suite.

We may make minor modifications to `tests.py` prior to evaluation in order to circumvent hard-coded and/or plagiarised solutions and to calibrate the assignment difficulty.

If you upload your (in-progress?) solution at least four days prior to the deadline, we will batch grade it and provide preliminary feedback through Brightspace. This gives you an opportunity to:
  * identify any library/package errors that prevents your code from running as expected
  * compare your code coverage to our expectations
  * obtain a preliminary evaluation of how well you are doing
  * finish the assignment early and be confident of your grade
  * obtain a sense of how well you are doing on the assignment prior to the midterm exam for this module

## Sources and Academic Integrity

You are permitted to use sources that you find on the Internet, so long as the source is clearly dated with a last edit prior to 1-January-2022 and you provide a citation in your source code. For example, GitHub and StackOverflow content is permitted, so long as they are clearly dated prior to this year. If you do not include a citation in your source code, your work will be considered plagiarism.

You must otherwise complete the assignment independently, including the development of pseudocode. Submissions will be subjected to plagiarism detection software and evidence of collaboration will be reported as an Academic Integrity infringement. You are welcome to prepare for the assignment with peers in the class by working through the ungraded worksheets together, which are designed to prepare you well for this assignment.

## Illness, Lateness, Technical Issues, and Personal Circumstances

Submissions will be accepted until the _end date_ of the assignment listed in Brightspace, which provides a three day buffer to address most challenges that are likely to arise. Note that support for the assignment will not be available after the deadline, however. Submissions will not be accepted after the _end date_; if you have not submitted code by then, whether by choice or circumstances, the weight for this assignment will be shifted to the corresponding midterm exam.

## Summary

I hope that this assignment is a fun way to work through the systematic interpretation of ERD's and conceptual database designs. Good luck!
