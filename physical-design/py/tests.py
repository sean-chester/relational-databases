# Test cases for ImplementMe class.
# The mocked objects (and therefore expected output) may change
# at the point of evaluation, including into a more complex object,  
# and the functionality tested by each test case may increase in difficulty.
# Your implementation should anticipate ways in which these mocks
# or tests could be more complex, as well as design mocks
# for some disclosed but not written test cases.

import unittest
import time
import timeout_decorator

from log import *
from index import *
from implement_me import ImplementMe


# Lookup on a tree with a log file with one update
class TestCase01(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.update(1,1,1)])

        key = 1
        expected_output = []

        self.assertEqual( expected_output, ImplementMe.lookup( ImplementMe.from_log( log ), key ) )


# Lookup on a tree with a log file with two updates
class TestCase02(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.update(1,1,1),\
            Record.update(1,2,2),\
            Record.commit_transaction(1)])

        key = 2
        expected_output = [1,2]

        self.assertEqual( expected_output, ImplementMe.lookup( ImplementMe.from_log( log ), key ) )




# Run all unit tests above.
unittest.main(argv=[''],verbosity=2, exit=False)
