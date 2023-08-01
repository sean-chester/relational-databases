# CSC 370 - Transaction Concurrency

## Assignment Goals

In this assignment you will:

  * demonstrate knowledge of some query database concurrency and transaction management concepts, particularly how transaction schedules can be reordered:
    + implement a function that determines whether a transaction schedule is serialisable
    + determine which serial schedules are conflict-equivalent to a concurrent schedule

## Task

You should implement part of what could be a simple transaction manager. It will take as input part of a concurrent schedule and confirm that it conforms to a serialisable isolation level. More specifically, it should report the serial schedule to which it is equivalent, or *None* if there is no such serial schedule.

You should complete the implementation of the one empty function in `SerialisabilityTester.py`:
  * `to_serial( schedule )` returns the smallest serial transaction schedule that is conflict-equivalent to the schedule that is provided as input or *None* if the schedule is not serialisable.

A schedule consists of a list of three-tuples that represent database I/O operations on atomic elements. For example, consider the schedule below:

[(1, "READ", "A")
,(2, "READ", "A")
,(1, "WRITE", "A")
,(2, "WRITE", "A")]

This schedule operates only on element A. First transaction 1 reads it, then transaction 2 reads it. Next transaction 1 writes it and then transaction 2 writes it. You should be able to confirm that this schedule is *not* serialisable. The output should be *None*.

Consider instead the following schedule:

[(2 , "READ", "A")
,(10, "READ", "A")]

This schedule is serialisable and there are two possible serial schedules that are equivalent to it: [2, 10] and [10, 2]. You should return the one that sorts (as integers) the transaction ids in ascending order, i.e., the "smallest sequence." In other words, the output should be [2, 10]. (Both *None* and [10, 2] are incorrect for this input.)


## Submission

You should implement the `to_serial()` function in `SerialisabilityTseter.py` and submit only that one file _without renaming it_. For evaluation, we will use our own copy of `Schedule.py` and `tests.py`. 

## Evaluation

Your functions will be evaluated with a series of unit tests and your score on the assignment will be the number of unit tests that you pass for a maximum score of 10/10. For example, a test of `to_serial()` might pass as input either of the examples above and check that the output matches the expected output.

A subset of the test cases will be provided. You will need to also identify some important boundary cases to test that have not been released in advance. The pre-released cases will be available in `tests.py`. Marking will take place by running:

```bash
python3 tests.py
```

Pre-marking will occur at an arbitrary point in the morning on the following date. You should submit prior to midnight the night before to be certain to receive a pre-grading update:

  * Saturday, 12 August 2023

The instructor reserves the right to award a score of 0 to functions that have not been implemented at all (e.g., simply return None with no dependence on the input parameters).

## Sources and Academic Integrity

You are permitted to use sources that you find on the Internet, so long as the source is clearly dated with a last edit prior to 1-January-2022 and you provide a citation in your source code. For example, GitHub and StackOverflow content is permitted, so long as they are clearly dated prior to this year. If you do not include a citation in your source code, your work will be considered plagiarism.

You must otherwise complete the assignment independently, including the development of pseudocode. Submissions may be subjected to plagiarism detection software and evidence of collaboration will be reported as an Academic Integrity infringement. You are welcome to prepare for the assignment with peers in the class by working through the ungraded worksheets together, which are designed to prepare you well for this assignment.

## Illness, Lateness, Technical Issues, and Personal Circumstances

Submissions will be accepted until the _end date_ of the assignment listed in Brightspace, which provides a three day buffer to address most challenges that are likely to arise. Note that support for the assignment will not be available after the deadline, however. Submissions will not be accepted after the _end date_; if you have not submitted code by then, whether by choice or circumstances, the weight for this assignment will be shifted to the corresponding midterm exam.

## Closing

I hope that this assignment is an enjoyable way to learn about database concurrency and back-end engineering. Good luck!
