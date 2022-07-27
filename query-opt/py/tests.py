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
from node import *
from index import *
from implement_me import ImplementMe


# Insert into an empty tree
class TestCase01(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):
        btree = Index()
        key = 99

        expected_output = Index(Node(\
            KeySet([99, None]),\
            PointerSet([None]*3)))

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert existing key
class TestCase02(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):
        btree = Index(Node(\
            KeySet([99, None]),\
            PointerSet([None]*Index.FAN_OUT)))
        key = 99

        expected_output = Index(Node(\
            KeySet([99, None]),\
            PointerSet([None]*Index.FAN_OUT)))

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into existing node that is not full
class TestCase03(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):
        btree = Index(Node(\
            KeySet([87, None]),\
            PointerSet([None]*Index.FAN_OUT)))
        key = 66

        expected_output = Index(Node(\
            KeySet([66, 87]),\
            PointerSet([None]*Index.FAN_OUT)))

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into full node.
class TestCase04(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):
        btree = Index(Node(\
            KeySet([66, 99]),\
            PointerSet([None]*Index.FAN_OUT)))
        key = 87

        expected_output = Index(Node(\
            KeySet([87, None]),\
            PointerSet([Node(\
                KeySet([66, None]),\
                PointerSet([None]*Index.FAN_OUT)),\
            Node(\
                KeySet([87,99]),\
                PointerSet([None]*Index.FAN_OUT)
                ),\
            None])))
        expected_output.root.pointers.pointers[0].pointers.pointers[Index.NUM_KEYS] = \
         expected_output.root.pointers.pointers[1]

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into full node with full parent, causing root split.
# Not shown. To be designed by student.
class TestCase05(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):
        btree = Index()
        key = 99

        expected_output = Index()

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into full node with full parent, but does not cause a root split.
class TestCase06(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):
        btree = Index()
        key = 12


        expected_output = Index()

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insertion causes splits that propagates at least three times
class TestCase07(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):
        btree = Index()
        key = 12

        expected_output = Index()

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Boundary case: lookup smallest key in tree
class TestCase08(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):
        btree = Index(Node(\
            KeySet([87, None]),\
            PointerSet([Node(\
                KeySet([66, None]),\
                PointerSet([None]*Index.FAN_OUT)),\
            Node(\
                KeySet([87,99]),\
                PointerSet([None]*Index.FAN_OUT)
                ),\
            None])))
        btree.root.pointers.pointers[0].pointers.pointers[Index.NUM_KEYS] = \
         btree.root.pointers.pointers[1]

        key = 66

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Boundary case: lookup largest key in tree
# Fake data in first node to test complexity
class TestCase09(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):
        btree = Index(Node(\
            KeySet([87, None]),\
            PointerSet([Node(\
                KeySet([66, None]),\
                PointerSet([None]*Index.FAN_OUT)),\
            Node(\
                KeySet([87,99]),\
                PointerSet([None]*Index.FAN_OUT)
                ),\
            None])))
        btree.root.pointers.pointers[0].pointers.pointers[Index.NUM_KEYS] = \
         btree.root.pointers.pointers[1]

        key = 99

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )




# Lookup key outside range of tree's keys
# Fake data in middle leaf to test complexity
class TestCase10(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):
        btree = Index(Node(\
            KeySet([87, None]),\
            PointerSet([Node(\
                KeySet([66, None]),\
                PointerSet([None]*Index.FAN_OUT)),\
            Node(\
                KeySet([87,99]),\
                PointerSet([None]*Index.FAN_OUT)
                ),\
            None])))
        btree.root.pointers.pointers[0].pointers.pointers[Index.NUM_KEYS] = \
         btree.root.pointers.pointers[1]

        key = 42

        expected_output = False

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Lookup key within tree's range but not in tree
# Fake data in one leaf to test complexity
class TestCase11(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):
        btree = Index(Node(\
            KeySet([87, None]),\
            PointerSet([Node(\
                KeySet([41, None]),\
                PointerSet([None]*Index.FAN_OUT)),\
            Node(\
                KeySet([87,99]),\
                PointerSet([None]*Index.FAN_OUT)
                ),\
            None])))
        btree.root.pointers.pointers[0].pointers.pointers[Index.NUM_KEYS] = \
         btree.root.pointers.pointers[1]

        key = 66

        expected_output = False

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )

# Lookup key strictly within the tree's range
class TestCase12(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):
        btree = Index(Node(\
            KeySet([87, None]),\
            PointerSet([Node(\
                KeySet([41, 66]),\
                PointerSet([None]*Index.FAN_OUT)),\
            Node(\
                KeySet([87,99]),\
                PointerSet([None]*Index.FAN_OUT)
                ),\
            None])))
        btree.root.pointers.pointers[0].pointers.pointers[Index.NUM_KEYS] = \
         btree.root.pointers.pointers[1]

        key = 66

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Range query fully contained in one leaf node
class TestCase13(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):
        btree = Index(Node(\
            KeySet([87, None]),\
            PointerSet([Node(\
                KeySet([41, 68]),\
                PointerSet([None]*Index.FAN_OUT)),\
            Node(\
                KeySet([87,99]),\
                PointerSet([None]*Index.FAN_OUT)
                ),\
            None])))
        btree.root.pointers.pointers[0].pointers.pointers[Index.NUM_KEYS] = \
         btree.root.pointers.pointers[1]

        lower_bound = 42
        upper_bound = 66

        expected_output = []

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Range query half-open to the left
class TestCase14(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):
        btree = Index(Node(\
            KeySet([87, None]),\
            PointerSet([Node(\
                KeySet([41, 68]),\
                PointerSet([None]*Index.FAN_OUT)),\
            Node(\
                KeySet([87,99]),\
                PointerSet([None]*Index.FAN_OUT)
                ),\
            None])))
        btree.root.pointers.pointers[0].pointers.pointers[Index.NUM_KEYS] = \
         btree.root.pointers.pointers[1]

        lower_bound = 0
        upper_bound = 42

        expected_output = [41]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Range query half-open to the right
class TestCase15(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):
        btree = Index(Node(\
            KeySet([87, None]),\
            PointerSet([Node(\
                KeySet([41, 68]),\
                PointerSet([None]*Index.FAN_OUT)),\
            Node(\
                KeySet([87,99]),\
                PointerSet([None]*Index.FAN_OUT)
                ),\
            None])))
        btree.root.pointers.pointers[0].pointers.pointers[Index.NUM_KEYS] = \
         btree.root.pointers.pointers[1]

        lower_bound = 42
        upper_bound = 1024

        expected_output = [68,87,99]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Range query with matching upper and lower bound
class TestCase16(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):
        btree = Index()
        lower_bound = 7
        upper_bound = 7

        expected_output = []

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Multi-leaf range query in middle of tree
class TestCase17(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):
        btree = Index()
        lower_bound = 42
        upper_bound = 87

        expected_output = []

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Lookup recently added key
class TestCase18(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_unknown(self):
        btree = Index()
        key = 12

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex(\
        ImplementMe.InsertIntoIndex( btree, key ), key ) )



# Lookup range that includes recently added key
class TestCase19(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_unknown(self):
        btree = Index()
        key = 12
        lower_bound = 12
        upper_bound = 66

        expected_output = [12,27]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex(\
        ImplementMe.InsertIntoIndex( btree, key ), lower_bound, upper_bound ) )


# Lookup range with nearly matching lower and upper bound equal to recently added key
class TestCase20(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_unknown(self):
        btree = Index()
        key = 12
        lower_bound = 12
        upper_bound = 13

        expected_output = []

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex(\
        ImplementMe.InsertIntoIndex( btree, key ), lower_bound, upper_bound ) )


# Run all unit tests above.
unittest.main(argv=[''],verbosity=2, exit=False)
