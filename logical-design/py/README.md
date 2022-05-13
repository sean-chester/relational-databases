# CSC370 Assignment 1 Python Implementation

_This "starter" code provides the test harness for completing Assignment 1 in Python, which will be evaluated with the unittest Python module for unit testing. You should expand the test suite to ensure that your implementation passes not just the provided tests, but also other ones that could reasonably arise from the worksheets or lecture material. This repository is designed to facilitate test-driven development (TDD)._

## Build Instructions

This project uses Python3 and can be run in any environment that supports Python3 (e.g., command line interpreter or Jupyter Notebook). There are no specific build requirements; you can simply run the test suite by executing the main method in `tests.py`
```
python3 ./tests.py
```

## Dependencies

In order to run this code, you will need:

  * Python3 (python2 is not guaranteed to be supported)
  * The `timeout-decorator` package if you want to confirm time-outs under 15s (or you can comment out those lines)

## Task

You should complete the implementation of the methods in the class `ImplementMe` in `bcnf.py`.
You are welcome to add anything you like to this file, which is the only one that you will submit. While you may modify any other files, e.g., by adding assert statements or additional test cases, these will not be part of your submission.

You can also refer to the test cases in `tests.py` for additional documentation of expected behaviour.

When we evaluate your `ImplementMe` class, we will modify `tests.py` with a revised set of twenty plus two similar test cases; each test case is worth 5% of the grade (for a maximum possible score of 110%). You can expect the bonus test cases will be quite difficult as they will test non-deterministic behaviour.

## Classes

You are provided with two classes, `RelationSet` in `relation.py` and `FDSet` in `functional_dependency.py`, that you should not need to modify. The input to `ImplementMe.DecompositionSteps` in `bcnf.py` is one instance of each class. The mock objects in `tests.py` exemplify their construction.

## License

This code is released under the terms of the [Unlicense](https://unlicense.org/). Please refer to [the difference between copyright and citation](https://researchguides.uic.edu/c.php?g=252209&p=1682805)
(TL;DR: it is still plagiarism to forget citations to works in the public domain).
 