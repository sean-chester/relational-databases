# CSC 370 - B+-Tree Implementation

## Assignment Goals

In this assignment you will:

  * demonstrate knowledge of some query optimisation concepts, particularly how B+-tree indexes work:

    + implement a B+-tree that handles insertions 
    + implement efficient queries on the B+-tree 

## Task

You are provided with a class definition for a linearised, ternary B+-tree, but it does not have any methods for inserting or querying data. You are also provided with an empty ImplementMe class that contains a number of unimplemented static methods to provide functional for a B+-tree. 

You should complete the implementation of the three empty static functions: one for inserting a new key into a tree, one to look up whether a specific key is in the index, and one to retrieve all keys in the index within a range. The implementations of these must be computationally efficient in order to obtain marks.

A "linearised" tree is one that is implemented as an array rather than with pointers. That is not how B+-trees are generally implemented in secondary storage, but it provides a simpler mechanism for testing on this assignment. To transform a tree into an array, a node is mapped onto an index that corresponds to its position in a breadth-first search of a full tree of the same height. For example, a binary tree with one root and one right child would map onto an array of length three: [root, ?, child], where the '?' is wasted space. More details about the linearisation of a ternary tree are provided in the inline comments in `index.py`.


## Submission

You should implement the ImplementMe class in `implement_me.py` and submit only that one file. For evaluation, we will use our own copy of `index.py`, `node.py`, and `tests.py`. 

## Evaluation

Your grade on the assignment will be the number of test cases passed by running `python3 tests.py`, for a maximum score of 20/20. All but three test cases are disclosed and, of those, all but two provide sample inputs and outputs.

You should be aware that we will change the actual data, including potentially the shapes of the trees, in our final version of `tests.py`. Marks will not be awarded for implementations that are detected to have sub-optimal complexity, such as a linear cost lookup function. 

## Sources

You are permitted to use sources and libraries that you find on the Internet, so long as it is clear that the source existed prior to the creation of this assignment and you provide a citation in your source code. For example, GitHub and StackOverflow content is permitted, so long as they are clearly dated prior to the beginning of this semester. If you do not include a citation in your source code, your work will be considered plagiarism.

You must work through the assignment on your own. Collaboration on the assignment, even at the conceptual design stage, if detected, will be immediately reported to the Academic Integrity Committee. You are welcome to prepare for the assignment with peers in the class by working through the ungraded worksheets together, which are designed to prepare you adequately for this assignment.

## Illness Policy

The end date for the assignment is three days later than the due date. This is expected to provide sufficient contingency for most minor illnesses and you should submit by the due date rather than the end date if you are not constrained by illness. Submissions will not be accepted even a couple minutes after the end of the illness buffer period (visible as the _end date_ of the assignment in Brightspace).

Support for the assignment _will not be provided_ during the illness buffer. You are encouraged to ask questions early.

_Note that grades for the class need to be submitted to Records within seven days of the due date of this assignment. Any further accommodations need to be addressed and graded within that window._

In the event that three days' contingency is insufficient, you could contact the instructor in advance of the due date with a brief explanation. If you have submitted all previous, graded assignments, then your quiz for this module will be used as the assessment for these learning outcomes. If, on the other hand, you have a missing assignment due to, for example, prior illness this semester, then a well-justified second absence longer than three days we be accommodated with a make-up assessment in the form of an individual, closed, recorded oral exam over Zoom conducted by the instructor. The use of make-up assessments will help to ensure that there are sufficiently many assessment activities (at least 80% of the grade) for each student to accurately reflect their achievement in this course.

You are encouraged to submit your preliminary progress one week and again three days prior to the assignment deadline to document progress in case of illness. These preliminary submissions can, of course, be overwritten by your final submission.

## Summary

I hope that this assignment is a fun way to learn about database indexes in more depth. Good luck!

## Change Log

