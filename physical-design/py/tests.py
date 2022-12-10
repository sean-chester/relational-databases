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


# Insert into full node
class TestCase03(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.update(1,1,1),\
            Record.update(1,2,2),\
            Record.update(1,5,3),\
            Record.commit_transaction(1)])

        key = 2
        expected_output = [3,1,2]

        self.assertEqual( expected_output, ImplementMe.lookup( ImplementMe.from_log( log ), key ) )



# Insert into full node with full parent, causing root split.
class TestCase04(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.update(1,1,1),\
            Record.update(1,2,2),\
            Record.update(1,5,4),\
            Record.update(1,8,3),\
            Record.update(1,9,0),\
            Record.commit_transaction(1)])

        key = 3
        expected_output = [3,4,3]

        self.assertEqual( expected_output, ImplementMe.lookup( ImplementMe.from_log( log ), key ) )


# Insert into full node but does not cause root split
class TestCase05(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.update(1,1,1),\
            Record.update(1,2,2),\
            Record.update(1,5,4),\
            Record.update(1,8,5),\
            Record.update(1,9,6),\
            Record.commit_transaction(1)])

        key = 7
        expected_output = [4,6,6]

        self.assertEqual( expected_output, ImplementMe.lookup( ImplementMe.from_log( log ), key ) )


# Insert causes split that propagates three times
class TestCase06(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.update(1,1,1),\
            Record.update(1,2,20),\
            Record.update(1,5,40),\
            Record.update(1,8,30),\
            Record.update(1,9,0),\
            Record.commit_transaction(1),\
            Record.start_transaction(3),\
            Record.update(3,4,4),\
            Record.update(3,6,2),\
            Record.update(3,16,41),\
            Record.update(3,17,43),\
            Record.update(3,18,42),\
            Record.commit_transaction(3)])

        key = 38
        expected_output = [30,42,40,30]

        self.assertEqual( expected_output, ImplementMe.lookup( ImplementMe.from_log( log ), key ) )


# Range search on full tree
class TestCase07(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.update(1,1,1),\
            Record.update(1,2,2),\
            Record.update(1,5,3),\
            Record.update(1,6,0),\
            Record.commit_transaction(1)])

        lower_bound = 0
        upper_bound = 10
        expected_output = [2,0,1,2,3]

        self.assertEqual( expected_output, ImplementMe.range( ImplementMe.from_log( log ), lower_bound, upper_bound ) )

# Range search that starts or ends on leaf node boundary
# Not provided
class TestCase08(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.update(1,1,1),\
            Record.update(1,2,2),\
            Record.update(1,5,4),\
            Record.update(1,6,0),\
            Record.update(1,3,5),\
            Record.commit_transaction(1)])

        lower_bound = 1
        upper_bound = 3
        expected_output = [2,0,1,2,4]

        self.assertEqual( expected_output, ImplementMe.range( ImplementMe.from_log( log ), lower_bound, upper_bound ) )


# Range search fully contained in one leaf node
# Not provided
class TestCase09(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):


        log = Log([Record.start_transaction(1),\
            Record.update(1,1,1),\
            Record.update(1,2,2),\
            Record.update(1,5,4),\
            Record.update(1,6,0),\
            Record.update(1,3,5),\
            Record.commit_transaction(1)])

        lower_bound = 0
        upper_bound = 1
        expected_output = [2,0,1]

        self.assertEqual( expected_output, ImplementMe.range( ImplementMe.from_log( log ), lower_bound, upper_bound ) )

# Range search on tall tree
class TestCase10(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.update(1,1,1),\
            Record.update(1,2,20),\
            Record.update(1,5,40),\
            Record.update(1,8,30),\
            Record.update(1,9,0),\
            Record.commit_transaction(1),\
            Record.start_transaction(3),\
            Record.update(3,4,4),\
            Record.update(3,6,2),\
            Record.update(3,16,41),\
            Record.update(3,17,43),\
            Record.update(3,18,42),\
            Record.commit_transaction(3)])

        lower_bound = 4
        upper_bound = 31
        expected_output = [30,4,20,4,20,30,40]

        self.assertEqual( expected_output, ImplementMe.range( ImplementMe.from_log( log ), lower_bound, upper_bound ) )

# A value is changed, moving a tuple's key to a different leaf
class TestCase11(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.update(1,1,1),\
            Record.update(1,2,2),\
            Record.update(1,3,3),\
            Record.commit_transaction(1),\
            Record.start_transaction(2),\
            Record.update(2,1,4),\
            Record.commit_transaction(2)])

        key = 4
        expected_output = [3,3,4]

        self.assertEqual( expected_output, ImplementMe.lookup( ImplementMe.from_log( log ), key ) )


# Log file has at least one incomplete transaction
class TestCase12(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.update(1,1,2),\
            Record.start_transaction(2),\
            Record.update(2,2,1),\
            Record.commit_transaction(1)])

        key = 1
        expected_output = [2]

        self.assertEqual( expected_output, ImplementMe.lookup( ImplementMe.from_log( log ), key ) )


# A value is changed, leaving a search key that is not in the leaves
class TestCase13(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.update(1,1,1),\
            Record.update(1,2,2),\
            Record.update(1,3,3),\
            Record.update(1,4,4),\
            Record.commit_transaction(1),\
            Record.start_transaction(2),\
            Record.update(2,3,5),\
            Record.commit_transaction(2)])

        key = 5
        expected_output = [3,4,5]

        self.assertEqual( expected_output, ImplementMe.lookup( ImplementMe.from_log( log ), key ) )


# A value is updated to itself
class TestCase14(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.update(1,1,1),\
            Record.update(1,2,2),\
            Record.commit_transaction(1),\
            Record.start_transaction(2),\
            Record.update(2,2,2),\
            Record.commit_transaction(2)])

        key = 2
        expected_output = [1,2]

        self.assertEqual( expected_output, ImplementMe.lookup( ImplementMe.from_log( log ), key ) )



# Two values in a tree change, causing the tree to change shape
class TestCase15(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.start_transaction(3),\
            Record.update(3,4,5),\
            Record.update(1,1,1),\
            Record.update(1,2,2),\
            Record.update(1,3,3),\
            Record.commit_transaction(1),\
            Record.start_transaction(2),\
            Record.update(2,1,6),\
            Record.update(2,2,4),\
            Record.commit_transaction(2)])

        key = 4
        expected_output = [5,3,4]

        self.assertEqual( expected_output, ImplementMe.lookup( ImplementMe.from_log( log ), key ) )

# Range search after a value is changed, leaving a search key that is not in the leaves
class TestCase16(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.update(1,1,1),\
            Record.update(1,2,2),\
            Record.update(1,3,3),\
            Record.update(1,4,4),\
            Record.commit_transaction(1),\
            Record.start_transaction(2),\
            Record.update(2,3,5),\
            Record.commit_transaction(2)])

        lower_bound = 2
        upper_bound = 5
        expected_output = [3,1,2,4,5]

        self.assertEqual( expected_output, ImplementMe.range( ImplementMe.from_log( log ), lower_bound, upper_bound ) )


# The same value is changed twice
class TestCase17(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.start_transaction(3),\
            Record.update(3,4,7),\
            Record.update(1,1,1),\
            Record.update(1,2,2),\
            Record.update(1,5,3),\
            Record.update(1,3,6),\
            Record.commit_transaction(1),\
            Record.start_transaction(2),\
            Record.update(2,1,8),\
            Record.update(2,1,0),\
            Record.commit_transaction(2)])

        lower_bound = 0
        upper_bound = 7
        expected_output = [3,0,2,3,6,7]

        self.assertEqual( expected_output, ImplementMe.range( ImplementMe.from_log( log ), lower_bound, upper_bound ) )


# The log file is empty
class TestCase18(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([])

        lower_bound = 3
        upper_bound = 3
        expected_output = []

        self.assertEqual( expected_output, ImplementMe.range( ImplementMe.from_log( log ), lower_bound, upper_bound ) )

# The same value is changed twice, causing persistent structural changes
class TestCase19(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.start_transaction(3),\
            Record.update(3,4,7),\
            Record.update(1,1,1),\
            Record.update(1,2,2),\
            Record.update(1,5,3),\
            Record.update(1,3,6),\
            Record.commit_transaction(1),\
            Record.start_transaction(2),\
            Record.update(2,1,4),\
            Record.update(2,1,8),\
            Record.commit_transaction(2)])

        lower_bound = 2
        upper_bound = 9
        expected_output = [6,3,2,3,6,7,8]

        self.assertEqual( expected_output, ImplementMe.range( ImplementMe.from_log( log ), lower_bound, upper_bound ) )


# The tree decreases in height due to a key update
class TestCase20(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        log = Log([Record.start_transaction(1),\
            Record.start_transaction(3),\
            Record.update(3,4,7),\
            Record.update(1,1,1),\
            Record.update(1,2,2),\
            Record.update(1,5,6),\
            Record.update(1,3,5),\
            Record.commit_transaction(1),\
            Record.start_transaction(2),\
            Record.update(2,1,8),\
            Record.update(2,2,1),\
            Record.commit_transaction(2)])

        lower_bound = 0
        upper_bound = 9
        expected_output = [6,1,5,6,7,8]

        self.assertEqual( expected_output, ImplementMe.range( ImplementMe.from_log( log ), lower_bound, upper_bound ) )

# Run all unit tests above.
unittest.main(argv=[''],verbosity=2, exit=False)
