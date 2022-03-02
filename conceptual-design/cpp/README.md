# CSC370-202201 Assignment 2 C++ Implementation

_This "starter" code provides the test harness for completing Assignment 2 in C++, which will be evaluated with the Catch2 unit testing framework. You should fill it in so that it passes not just the provided tests, but also other ones that could reasonably arise from the worksheets or lecture material._

## Build Instructions

This project uses [CMake](https://cmake.org/) and [Catch2](https://github.com/catchorg/Catch2) as a build and unit test system, respectively. You are suggested to use an _out-of-source_ build by creating a separate subdirectory and invoking both `cmake` and `make` from there. For example, if you start in the top-level directory:

```
mkdir build
cd build
cmake ../
make
./db-gen
```

You can also build the sample unit tests as well with the `-BUILD_TESTS` flag to `cmake` as follows:
```
mkdir build
cd build
cmake ../ -DBUILD_TESTS=1
make
./test/unit_tests
```

## Dependencies

In order to run this code, you will need:

  * CMake (which comes pre-installed in most development environments)
  * Catch2 (which is a header-only library that has been shipped with this code)

## Task

You should complete the implementation of the function `convert_to_table()` in `include/db-gen/converter/erd-converter.hpp`.
You are welcome to add anything you like to this header file and the accompanying implementation (i.e., .cpp) file located in `src/converter/erd-converter.cpp`. While you may modify any other files, these are the only two that you will submit; so, only changes to these files will be taken into account during evaluation.

You are encouraged to consult `test/converter/sample-tests.cpp`, both as a source of documentation and as a unit testing framework.
This has been set up well for test-driven development (TDD), as you already have one very simple failing test.
You are encouraged to add more as your development progresses.
When we evaluate you `erd-converter` header and implementation files, we will swap out this set of unit tests for an expanded set of twenty-two test cases, each worth 5% of the grade (for a maximum possible score of 110%).

You can expect some test cases will be quite difficult, but none will involve obscene numbers of entity sets and/or relationships.

## License

This code is released under the terms of the [Unlicense](https://unlicense.org/) with the exception of the Catch2 header file; it inherits the license of its creators.

Please refer to [the difference between copyright and citation](https://researchguides.uic.edu/c.php?g=252209&p=1682805)
(TL;DR: it is still plagiarism to forget citations to works in the public domain).
 