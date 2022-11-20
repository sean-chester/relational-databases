# CSC 370 - B+-Tree Reconstruction from Logs

## Assignment Goals

In this assignment you will:

  * demonstrate knowledge of some query optimisation concepts, particularly how B+-tree indexes work:
    + implement a B+-tree that handles insertions
    + implement efficient lookup and range queries on the B+-tree 
  * demonstrate knowledge of some data recovery concepts, particularly how to parse a REDO log file:

## Task

The horror! 😱

Your relational database has crashed! Fortunately, you have a log file from which to recover it. Unfortunately, you cannot be confident that your index structures are consistent with the database state at the time of failure. Thus, in this assignment, you will rebuild your B+-tree index from a log file.

In particular, you need to implement a B+-tree index that can support efficient lookup and range queries. It should be constructed from a REDO log file. You are provided with a class definition for a ternary B+-tree and for a log file. You are also provided with an empty ImplementMe class that contains the three unimplemented static methods that provide functionality for the B+-tree. You can assume that the B+-tree is on a primary key attribute.

You should complete the implementation of the three empty static functions:
  * `lookup( key )` returns a list of keys that are visited to check if the input key is in the tree
  * `range( lower, upper )` returns a list of keys that are visited to find all keys in the range [lower, upper]
  * `from_log( log )` returns a B+-tree constructed by parsing the log to replay all the insertions that are committed to the index

As you parse the REDO log file, you should assume that all entries refer to the same attribute and, if they have the same value, correspond to the same tuple. For example, in the log below the final tree should have two values, 6 and 7, since transaction 2 changes the value for tuple A:

[START T1]
[T1, A, 5]
[T2, B, 6]
[COMMIT T1]
[T2, A, 7]
[COMMIT T2]

The implementations of these must be computationally efficient in order to obtain marks; otherwise, the lists returned by your `lookup()` and `range()` functions will have an incorrect length. The B+-tree also must conform to the specifications shown in Garcia-Molina, which is a disk-based adaptation of (2,4)- and B-trees as presented in Goodrich & Tamassia.

Finally, note that inserting 5, inserting 6, and then modifying 5 to 7 does not necesssarily produce the same tree as simply inserting 6 and then inserting 7. You should handle insertions as a deletion followed by an insertion. You should handle all underflows by merging with a sibling and if, combined, they exceed the maximum capacity of four, then re-splitting.


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

## Closing

I hope that this assignment is an enjoyable way to learn about data recovery and query efficiency. Good luck!
