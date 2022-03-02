# CSC 370 - Relational Data Model Assignment

## Assignment Goals

In this assignment you will:

  * demonstrate knowledge of database decomposition (namely 3NF and BCNF)

    + implement the calculation of attribute set closures to identify keys and normal form violations
    + implement two standard algorithms for decomposition, the 3NF Synthesis Algorithm and the BCNF Decomposition Algorithm

## Task

You should write a computer program in the programming language of your choice that will take as input a set of relations _R_, a set of functional dependencies, _F_, a flag indicating a normal form, and a second set of relations _R'_; your program will output whether _R'_ can be the result of decomposing _R_ using _F_, into the indicated normal form.

Note that there is more than one possible decomposition for a given input, depending on the order in which you process BCNF violations. For example, if you were to decompose R(A,B,C,D,E) into BCNF with functional dependencies AB→C and BD→C, there are two correct decompositions:

  * R1(ABC) and R2(ABDE), corresponding to decomposing with the first BCNF violation first
  * R1(BCD) and R2(ABDE), corresponding to decomposing with the second BCNF violation first

However, R1(ABC), R2(ABD), and R3(DE) would not form a correct solution, even though this decomposition is in BCNF, because you would not arrive at it using the decomposition algorithm in the textbook. (It has been decomposed unnecessarily much.)

You should also write two short scripts for an Ubuntu-based machine:

  * `build`: this will conduct any preprocessing necessary, such as calling a compiler to compile the code.
  * `run`: this will execute your code, forwarding any command line arguments

(By requesting scripts, it allows you to choose a programming language of your choice, though you should ask first if you plan to use something very esoteric.)

The input format to the run script will be a set of command line arguments, formatted as follows:

  1. The attributes of the input relations, where relations are separated by semicolons and attributes are separated by commas
  2. The set of functional dependencies, where FDs are separated by semicolons, attributes are separated by commas, and the LHS of the FD is separated from the RHS by a forward slash, '\'
  3. A single character 'B' or '3', indicating BCNF or 3NF, respectively
  4. The set of relations in the decomposition, where relations are separated by semicolons and attributes are separated by commas

You can safely assume that the input will be well-formed (i.e., free of errors). The transcript below provides some examples:

```
./build
./run "a,b,c" "a,b/c" "B" "a,b,c"
True
./run "a,b,c" "a,b/c" "3" "a,b;b,c"
False
./run "title,theatre,city" "theatre/city;title,city/theatre" "3" "theatre,city;theatre,title"
False
./run "title,theatre,city" "theatre/city;title,city/theatre" "B" "theatre,city;theatre,title"
True
./run "a,b,c,d,e" "a,b/c;b,d/c" "B" "a,b,c;a,b,d,e"
True
./run "a,b,c,d,e" "a,b/c;b,d/c" "B" "b,c,d;a,b,d,e" 
True
./run "a,b,c,d,e" "a,b/c;b,d/c" "B" "a,b,c;a,b,d;d,e" 
False
./run "a,b,c;d,e" "a,b/c;d/e" "B" "a,b,c;d,e" 
True
```

## Submission

You are likely to produce at least three files, the two scripts noted above and at least one implementation file (e.g., .py, .java, .cpp). You should archive all of these into a single .zip or .tgz file that you will upload. Please be sure that you have archived the file such that when we gunzip it, your build and run scripts will work in the top-level directory of the archive. You may overwrite your submission as many times as you like prior to the deadline.

## Evaluation

We will grade the assignment with a marking script that will sample twenty inputs and assign a grade of pass (1) or fail (0) for each input. If your code takes more than five minutes on a single test, it may be terminated before the test finishes, resulting in a fail on that test. Your grade on the assignment will be the number of tests passed.

You will pass:

  * at least 40% of tests if you can correctly determine when a relation is already in the correct normal form
  * at least 20% more tests if you can also correctly solve fairly simple cases (such as the first four in the transcript)
  * at least 20% more tests if you can also solve more challenging cases (e.g., those that involve multiple levels of recursion)
the remaining tests if you can solve cases with multiple solutions (e.g., the last three in the transcript above)

## Sources

You are permitted to use sources that you find on the Internet, so long as it is clear that the source existed prior to the creation of this assignment and you provide a citation in your source code. For example, GitHub and StackOverflow content is permitted, so long as they are clearly dated prior to the beginning of this semester. If you do not include a citation in your source code, your work will be considered plagiarism.

You should, however, work through the assignment on your own. You are welcome to prepare for the assignment with peers in the class by working through the ungraded worksheets together.

## Summary

I hope that this assignment is a fun way to work through the edge cases for database normalisation. Good luck!
