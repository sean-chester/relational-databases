add_executable(
  unit_tests
    unitTests.cpp
    converter/sample-tests.cpp
)

target_link_libraries( 
  unit_tests
    converter
    gcov
)

target_compile_options(
  unit_tests
    PRIVATE --coverage
)
