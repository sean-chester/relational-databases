# CSC 370 - B+-Tree Implementation

## Assignment Goals

In this assignment you will:

  * demonstrate knowledge of some query optimisation concepts, particularly how B+-tree indexes work:

    + implement a B+-tree that handles insertions 
    + implement efficient queries on the B+-tree 

## Task

You are provided with a class definition for a ternary B+-tree, but it does not have any methods for inserting or querying data. You are also provided with an empty ImplementMe class that contains a number of unimplemented static methods to provide functionality for a B+-tree. 

You should complete the implementation of the three empty static functions: one for inserting a new key into a tree, one to look up whether a specific key is in the index, and one to retrieve all keys in the index within a range. The implementations of these must be computationally efficient in order to obtain marks.


## Submission

You should implement the ImplementMe class in `implement_me.py` and submit only that one file. For evaluation, we will use our own copy of `index.py`, `node.py`, and `tests.py`. 

## Evaluation

Your grade on the assignment will be the number of test cases passed by running `python3 tests.py`, for a maximum score of 20/20. All test cases are disclosed, but not all of them have been written.

You should be aware that we will change the actual data, including potentially the shapes of the trees, in our final version of `tests.py`. Marks will not be awarded for implementations that are detected to have sub-optimal complexity, such as a linear cost lookup function. 

## Sources and Academic Integrity

You are permitted to use sources that you find on the Internet, so long as the source is clearly dated with a last edit prior to 1-January-2022 and you provide a citation in your source code. For example, GitHub and StackOverflow content is permitted, so long as they are clearly dated prior to this year. If you do not include a citation in your source code, your work will be considered plagiarism.

You must otherwise complete the assignment independently, including the development of pseudocode. Submissions may be subjected to plagiarism detection software and evidence of collaboration will be reported as an Academic Integrity infringement. You are welcome to prepare for the assignment with peers in the class by working through the ungraded worksheets together, which are designed to prepare you well for this assignment.

## Illness, Lateness, Technical Issues, and Personal Circumstances

Submissions will be accepted until the _end date_ of the assignment listed in Brightspace, which provides a three day buffer to address most challenges that are likely to arise. Note that support for the assignment will not be available after the deadline, however. Submissions will not be accepted after the _end date_; if you have not submitted code by then, whether by choice or circumstances, the weight for this assignment will be shifted to the corresponding midterm exam.

## Summary

I hope that this assignment is a fun way to learn and/or practice the SQL query language. Good luck!


## Change Log

[31 July: 00:48] Repaired test case 6, which falsely inherited references from input object
[29 July: 13.03] Added two new test cases to better document classes
[27 July: 11.36] Add missing linked list pointers in leaf nodes
[25 July: 11.13] Repair default constructor that did not properly handle mutable default values
