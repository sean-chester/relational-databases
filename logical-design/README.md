# CSC 370 - Relational Data Model Assignment

## Assignment Goals

In this assignment you will:

  * demonstrate knowledge of database decomposition (namely BCNF)

    + implement the calculation of attribute set closures to identify keys and normal form violations
    + implement a standard algorithm for decomposition, the BCNF Decomposition Algorithm

## Task

You should write a computer program in either Python or Java (or, after consultation with the instructor, another language of your choice) that determines how many levels of recursion are required to decompose a relation into BCNF. More specifically, you are provided with a class definition for a set of relations R and a set of functional dependencies F, and you should implement a function that returns -1 if the relations are not in BCNF or a non-negative integer indicating how many recursive steps of BCNF decomposition are required to convert the union of elements of R into R using BCNF decomposition with F. 

Be careful that there is more than one possible decomposition for a given input, depending on the order in which you process BCNF violations. For example, if you were to decompose R(A,B,C,D,E) into BCNF with functional dependencies AB→C and BD→C, there are two correct decompositions for which your program should output 1:

  * R1(ABC) and R2(ABDE), corresponding to decomposing with the first BCNF violation first
  * R1(BCD) and R2(ABDE), corresponding to decomposing with the second BCNF violation first

Note that R1(ABC), R2(ABD), and R3(DE) is not a correct solution, even though this decomposition is in BCNF, because you would not arrive at it using the decomposition algorithm in the textbook. (It has been decomposed unnecessarily much.) Your program should output -1 on this input.

As a third example, given R(A,B,C) and functional dependency AB→C, your program should output 0, because the input is already in BCNF.  


## Submission

You should implement the (empty) function called `decompose()` in `bcnf.py` and then submit the single file `bcnf.py` (or the equivalent in Java). You are welcome to add auxillairy ("helper") functions, so long as they are in the `bcnf.py` file that you submit.  

## Evaluation

Included with the starter code is a set of unit tests (`tests.py`). This imports your `bcnf.py` code. To evaluate your submission, we will use a marking script that will run `python3 tests.py` and count the percentage of unit tests that your code passes. This percentage will be your grade on the assignment.

We may make minor modifications to `tests.py` prior to evaluation in order to circumvent hard-coded and/or plagiarised solutions.

As you can see from `tests.py`, you will pass:

  * at least 40% of tests if you can correctly determine when a relation is already in BCNF
  * at least 30% more tests if you can also correctly solve cases that require at most one recursive step
  * at least 30% more tests if you can also correctly solve those that involve multiple levels of recursion
  * bonus marks if you can handle very challenging cases, such as those involving non-determinism

## Sources and Academic Integrity

You are permitted to use sources that you find on the Internet, so long as the source is clearly dated with a last edit prior to 1-January-2022 and you provide a citation in your source code. For example, GitHub and StackOverflow content is permitted, so long as they are clearly dated prior to this year. If you do not include a citation in your source code, your work will be considered plagiarism.

You must otherwise complete the assignment independently, including the development of pseudocode. Submissions will be subjected to plagiarism detection software and evidence of collaboration will be reported as an Academic Integrity infringement. You are welcome to prepare for the assignment with peers in the class by working through the ungraded worksheets together, which are designed to prepare you well for this assignment.

Finally, you are encouraged to look through the commit history of [this course's public GitHub repository](https://github.com/sean-chester/relational-databases/tree/main/logical-design) for additional test cases. 

## Summary

I hope that this assignment is a fun way to work through the edge cases of database normalisation. Good luck!
