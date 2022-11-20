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

        root = Node()
        btree = Index( root )

        key = 87

        newRoot = Node(\
            KeySet([87,None]),\
            PointerSet([None]*Index.FAN_OUT))
        expected_output = Index( newRoot )

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert existing key
class TestCase02(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        root = Node(\
            KeySet([87,None]),\
            PointerSet([None]*Index.FAN_OUT))
        btree = Index( root )

        key = 87

        newRoot = Node(\
            KeySet([87,None]),\
            PointerSet([None]*Index.FAN_OUT))
        expected_output = Index( newRoot )

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into existing node that is not full
class TestCase03(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        root = Node(\
            KeySet([87, None]),\
            PointerSet([None]*Index.FAN_OUT))
        btree = Index( root )

        key = 99

        newRoot = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        expected_output = Index( newRoot )

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into full node.
class TestCase04(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        root = Node(\
            KeySet([66, 87]),\
            PointerSet([None]*Index.FAN_OUT))
        btree = Index( root )

        key = 99

        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([66, None]),\
            PointerSet([None, None, leaf1]))
        newRoot = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        expected_output = Index( newRoot )

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into full node with full parent, causing root split.
class TestCase05(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):

        leaf2 = Node(\
            KeySet([87,None]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf1 = Node(\
            KeySet([27,66]),\
            PointerSet([None,None,leaf2]))
        leaf0 = Node(\
            KeySet([7,9]),\
            PointerSet([None,None,leaf1]))
        root = Node(\
            KeySet([27,87]),\
            PointerSet([leaf0,leaf1,leaf2]))
        btree = Index(root)

        key = 42

        newLeaf3 = Node(\
            KeySet([87,None]),\
            PointerSet([None]*Index.FAN_OUT))
        newLeaf2 = Node(\
            KeySet([42,66]),\
            PointerSet([None,None,newLeaf3]))
        newLeaf1 = Node(\
            KeySet([27,None]),\
            PointerSet([None,None,newLeaf2]))
        newLeaf0 = Node(\
            KeySet([7,9]),\
            PointerSet([None,None,newLeaf1]))
        newParent1 = Node(\
            KeySet([87,None]),\
            PointerSet([newLeaf2,newLeaf3,None]))
        newParent0 = Node(\
            KeySet([27,None]),\
            PointerSet([newLeaf0,newLeaf1,None]))
        newRoot = Node(\
            KeySet([42,None]),\
            PointerSet([newParent0,newParent1,None]))
        expected_output = Index(newRoot)

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into full node with full parent, but does not cause a root split.
class TestCase06(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):

        leaf4 = Node(\
            KeySet([97,99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf3 = Node(\
            KeySet([87, None]),\
            PointerSet([None,None,leaf4]))
        leaf2 = Node(\
            KeySet([66,None]),\
            PointerSet([None,None,leaf3]))
        leaf1 = Node(\
            KeySet([27,None]),\
            PointerSet([None,None,leaf2]))
        leaf0 = Node(\
            KeySet([7,9]),\
            PointerSet([None,None,leaf1]))
        parent1 = Node(\
            KeySet([97,None]),\
            PointerSet([leaf3,leaf4,None]))
        parent0 = Node(\
            KeySet([27,66]),\
            PointerSet([leaf0,leaf1,leaf2]))
        root = Node(\
            KeySet([87,None]),\
            PointerSet([parent0,parent1,None]))
        btree = Index(root)

        key = 5

        newLeaf5 = Node(\
            KeySet([97,99]),\
            PointerSet([None]*Index.FAN_OUT))
        newLeaf4 = Node(\
            KeySet([87, None]),\
            PointerSet([None,None,newLeaf5]))
        newLeaf3 = Node(\
            KeySet([66,None]),\
            PointerSet([None,None,newLeaf4]))
        newLeaf2 = Node(\
            KeySet([27,None]),\
            PointerSet([None,None,newLeaf3]))
        newLeaf1 = Node(\
            KeySet([7,9]),\
            PointerSet([None,None,newLeaf2]))
        newLeaf0 = Node(\
            KeySet([5,None]),\
            PointerSet([None,None,newLeaf1]))
        newParent2 = Node(\
            KeySet([97,None]),\
            PointerSet([newLeaf4,newLeaf5,None]))
        newParent1 = Node(\
            KeySet([66,None]),\
            PointerSet([newLeaf2,newLeaf3,None]))
        newParent0 = Node(\
            KeySet([7,None]),\
            PointerSet([newLeaf0,newLeaf1,None]))
        newRoot = Node(\
            KeySet([27,87]),\
            PointerSet([newParent0,newParent1,newParent2]))
        expected_output = Index(newRoot)

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insertion causes splits that propagates at least three times
class TestCase07(unittest.TestCase):
    @timeout_decorator.timeout(25)
    def test_insertion(self):

        leaf5 = Node(\
            KeySet([97,99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf4 = Node(\
            KeySet([87, None]),\
            PointerSet([None,None,leaf5]))
        leaf3 = Node(\
            KeySet([66,None]),\
            PointerSet([None,None,leaf4]))
        leaf2 = Node(\
            KeySet([27,None]),\
            PointerSet([None,None,leaf3]))
        leaf1 = Node(\
            KeySet([7,9]),\
            PointerSet([None,None,leaf2]))
        leaf0 = Node(\
            KeySet([5,None]),\
            PointerSet([None,None,leaf1]))
        parent2 = Node(\
            KeySet([97,None]),\
            PointerSet([leaf4,leaf5,None]))
        parent1 = Node(\
            KeySet([66,None]),\
            PointerSet([leaf2,leaf3,None]))
        parent0 = Node(\
            KeySet([7,None]),\
            PointerSet([leaf0,leaf1,None]))
        root = Node(\
            KeySet([27,87]),\
            PointerSet([parent0,parent1,parent2]))
        btree = Index(root)

        key1 = 8
        key2 = 12

        newLeaf7 = Node(\
            KeySet([97,99]),\
            PointerSet([None]*Index.FAN_OUT))
        newLeaf6 = Node(\
            KeySet([87, None]),\
            PointerSet([None,None,newLeaf7]))
        newLeaf5 = Node(\
            KeySet([66,None]),\
            PointerSet([None,None,newLeaf6]))
        newLeaf4 = Node(\
            KeySet([27,None]),\
            PointerSet([None,None,newLeaf5]))
        newLeaf3 = Node(\
            KeySet([9,12]),\
            PointerSet([None,None,newLeaf4]))
        newLeaf2 = Node(\
            KeySet([8,None]),\
            PointerSet([None,None,newLeaf3]))
        newLeaf1 = Node(\
            KeySet([7,None]),\
            PointerSet([None,None,newLeaf2]))
        newLeaf0 = Node(\
            KeySet([5,None]),\
            PointerSet([None,None,newLeaf1]))
        newParent3 = Node(\
            KeySet([97,None]),\
            PointerSet([newLeaf6,newLeaf7,None]))
        newParent2 = Node(\
            KeySet([66,None]),\
            PointerSet([newLeaf4,newLeaf5,None]))
        newParent1 = Node(\
            KeySet([9,None]),\
            PointerSet([newLeaf2,newLeaf3,None]))
        newParent0 = Node(\
            KeySet([7,None]),\
            PointerSet([newLeaf0,newLeaf1,None]))
        newNonRoot1 = Node(\
            KeySet([87,None]),\
            PointerSet([newParent2,newParent3, None]))
        newNonRoot0 = Node(\
            KeySet([8,None]),\
            PointerSet([newParent0,newParent1,None]))
        newRoot = Node(\
            KeySet([27,None]),\
            PointerSet([newNonRoot0,newNonRoot1,None]))
        expected_output = Index( newRoot )

        self.assertEqual( expected_output\
            , ImplementMe.InsertIntoIndex( \
                ImplementMe.InsertIntoIndex( btree, key1 )\
                , key2 ) )


# Boundary case: lookup smallest key in tree
# Note: fake value in leaf1 to test complexity
class TestCase08(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):

        leaf1 = Node(\
            KeySet([87, 9]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([3, 68]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        key = 3

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Boundary case: lookup largest key in middle sub-tree
# Fake data in first node to test complexity
class TestCase09(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):

        leaf5 = Node(\
            KeySet([97,99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf4 = Node(\
            KeySet([87, None]),\
            PointerSet([None,None,leaf5]))
        leaf3 = Node(\
            KeySet([68,None]),\
            PointerSet([None,None,leaf4]))
        leaf2 = Node(\
            KeySet([27,None]),\
            PointerSet([None,None,leaf3]))
        leaf1 = Node(\
            KeySet([7,9]),\
            PointerSet([None,None,leaf2]))
        leaf0 = Node(\
            KeySet([5,None]),\
            PointerSet([None,None,leaf1]))
        parent2 = Node(\
            KeySet([97,None]),\
            PointerSet([leaf4,leaf5,None]))
        parent1 = Node(\
            KeySet([66,None]),\
            PointerSet([leaf2,leaf3,None]))
        parent0 = Node(\
            KeySet([7,None]),\
            PointerSet([leaf0,leaf1,None]))
        root = Node(\
            KeySet([27,87]),\
            PointerSet([parent0,parent1,parent2]))
        btree = Index(root)

        key = 68

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Lookup key used in directory node but not indexed in tree
class TestCase10(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):

        leaf5 = Node(\
            KeySet([97,99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf4 = Node(\
            KeySet([87, None]),\
            PointerSet([None,None,leaf5]))
        leaf3 = Node(\
            KeySet([68,None]),\
            PointerSet([None,None,leaf4]))
        leaf2 = Node(\
            KeySet([27,None]),\
            PointerSet([None,None,leaf3]))
        leaf1 = Node(\
            KeySet([7,9]),\
            PointerSet([None,None,leaf2]))
        leaf0 = Node(\
            KeySet([5,None]),\
            PointerSet([None,None,leaf1]))
        parent2 = Node(\
            KeySet([97,None]),\
            PointerSet([leaf4,leaf5,None]))
        parent1 = Node(\
            KeySet([66,None]),\
            PointerSet([leaf2,leaf3,None]))
        parent0 = Node(\
            KeySet([7,None]),\
            PointerSet([leaf0,leaf1,None]))
        root = Node(\
            KeySet([27,87]),\
            PointerSet([parent0,parent1,parent2]))
        btree = Index(root)

        key = 66

        expected_output = False

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Lookup key with scrambled key order to test algorithmic precision
class TestCase11(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):

        leaf2 = Node(\
            KeySet([5, None]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None, None, leaf2]))
        leaf0 = Node(\
            KeySet([66, None]),\
            PointerSet([None, None, leaf1]))
        # should not read second key!
        newRoot = Node(\
            KeySet([87, 5]),\
            PointerSet([leaf0, leaf1, leaf2]))
        btree = Index( newRoot )

        key = 5

        expected_output = False

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )

# Lookup key in very tall tree
class TestCase12(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_lookup(self):

        newLeaf7 = Node(\
            KeySet([97,99]),\
            PointerSet([None]*Index.FAN_OUT))
        newLeaf6 = Node(\
            KeySet([87, None]),\
            PointerSet([None,None,newLeaf7]))
        newLeaf5 = Node(\
            KeySet([66,None]),\
            PointerSet([None,None,newLeaf6]))
        newLeaf4 = Node(\
            KeySet([28,None]),\
            PointerSet([None,None,newLeaf5]))
        newLeaf3 = Node(\
            KeySet([9,12]),\
            PointerSet([None,None,newLeaf4]))
        newLeaf2 = Node(\
            KeySet([8,None]),\
            PointerSet([None,None,newLeaf3]))
        newLeaf1 = Node(\
            KeySet([7,None]),\
            PointerSet([None,None,newLeaf2]))
        newLeaf0 = Node(\
            KeySet([5,None]),\
            PointerSet([None,None,newLeaf1]))
        newParent3 = Node(\
            KeySet([97,None]),\
            PointerSet([newLeaf6,newLeaf7,None]))
        newParent2 = Node(\
            KeySet([66,None]),\
            PointerSet([newLeaf4,newLeaf5,None]))
        newParent1 = Node(\
            KeySet([9,None]),\
            PointerSet([newLeaf2,newLeaf3,None]))
        newParent0 = Node(\
            KeySet([7,None]),\
            PointerSet([newLeaf0,newLeaf1,None]))
        newNonRoot1 = Node(\
            KeySet([87,None]),\
            PointerSet([newParent2,newParent3, None]))
        newNonRoot0 = Node(\
            KeySet([8,None]),\
            PointerSet([newParent0,newParent1,None]))
        newRoot = Node(\
            KeySet([27,None]),\
            PointerSet([newNonRoot0,newNonRoot1,None]))
        btree = Index( newRoot )

        key = 28

        expected_output = True

        self.assertEqual( expected_output\
            , ImplementMe.LookupKeyInIndex( btree, key ) )


# Range query fully contained in one leaf node
class TestCase13(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):

        leaf1 = Node(\
            KeySet([87, 66]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([41, 68]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        lower_bound = 41
        upper_bound = 68

        expected_output = [41]

        self.assertEqual( expected_output\
            , ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Range query half-open to the left
class TestCase14(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):

        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([41, 68]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        lower_bound = 0
        upper_bound = 41

        expected_output = []

        self.assertEqual( expected_output\
            , ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Range query half-open to the right
class TestCase15(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):

        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([41, 68]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        lower_bound = 99
        upper_bound = 1024

        expected_output = [99]

        self.assertEqual( expected_output\
            , ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Range query with matching upper and lower bound
class TestCase16(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):

        leaf1 = Node(\
            KeySet([87, 99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf0 = Node(\
            KeySet([41, 68]),\
            PointerSet([None, None, leaf1]))
        root = Node(\
            KeySet([87, None]),\
            PointerSet([leaf0, leaf1, None]))
        btree = Index( root )

        lower_bound = 41
        upper_bound = 41

        expected_output = []

        self.assertEqual( expected_output\
            , ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Multi-leaf range query in middle of tree
class TestCase17(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_range(self):

        newLeaf7 = Node(\
            KeySet([97,99]),\
            PointerSet([None]*Index.FAN_OUT))
        newLeaf6 = Node(\
            KeySet([87, None]),\
            PointerSet([None,None,newLeaf7]))
        newLeaf5 = Node(\
            KeySet([66,60]),\
            PointerSet([None,None,newLeaf6]))
        newLeaf4 = Node(\
            KeySet([28,None]),\
            PointerSet([None,None,newLeaf5]))
        newLeaf3 = Node(\
            KeySet([9,12]),\
            PointerSet([None,None,newLeaf4]))
        newLeaf2 = Node(\
            KeySet([8,None]),\
            PointerSet([None,None,newLeaf3]))
        newLeaf1 = Node(\
            KeySet([7,None]),\
            PointerSet([None,None,newLeaf2]))
        newLeaf0 = Node(\
            KeySet([5,None]),\
            PointerSet([None,None,newLeaf1]))
        newParent3 = Node(\
            KeySet([97,None]),\
            PointerSet([newLeaf6,newLeaf7,None]))
        newParent2 = Node(\
            KeySet([66,None]),\
            PointerSet([newLeaf4,newLeaf5,None]))
        newParent1 = Node(\
            KeySet([9,None]),\
            PointerSet([newLeaf2,newLeaf3,None]))
        newParent0 = Node(\
            KeySet([7,None]),\
            PointerSet([newLeaf0,newLeaf1,None]))
        newNonRoot1 = Node(\
            KeySet([87,None]),\
            PointerSet([newParent2,newParent3, None]))
        newNonRoot0 = Node(\
            KeySet([8,None]),\
            PointerSet([newParent0,newParent1,None]))
        newRoot = Node(\
            KeySet([27,None]),\
            PointerSet([newNonRoot0,newNonRoot1,None]))
        btree = Index( newRoot )

        lower_bound = 13
        upper_bound = 66

        expected_output = [28]

        self.assertEqual( expected_output\
            , ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Lookup recently added key
class TestCase18(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_unknown(self):

        leaf5 = Node(\
            KeySet([97,99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf4 = Node(\
            KeySet([87, None]),\
            PointerSet([None,None,leaf5]))
        leaf3 = Node(\
            KeySet([66,None]),\
            PointerSet([None,None,leaf4]))
        leaf2 = Node(\
            KeySet([27,None]),\
            PointerSet([None,None,leaf3]))
        leaf1 = Node(\
            KeySet([7,9]),\
            PointerSet([None,None,leaf2]))
        leaf0 = Node(\
            KeySet([5,None]),\
            PointerSet([None,None,leaf1]))
        parent2 = Node(\
            KeySet([97,None]),\
            PointerSet([leaf4,leaf5,None]))
        parent1 = Node(\
            KeySet([66,None]),\
            PointerSet([leaf2,leaf3,None]))
        parent0 = Node(\
            KeySet([7,None]),\
            PointerSet([leaf0,leaf1,None]))
        root = Node(\
            KeySet([27,87]),\
            PointerSet([parent0,parent1,parent2]))
        btree = Index(root)

        key1 = 8
        key2 = 12

        expected_output = True

        self.assertEqual( expected_output\
            , ImplementMe.LookupKeyInIndex(\
                ImplementMe.InsertIntoIndex(\
                    ImplementMe.InsertIntoIndex( btree, key1 ),\
                    key2 ),\
                key1 ) )



# Lookup range that includes recently added key
class TestCase19(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_unknown(self):

        leaf4 = Node(\
            KeySet([97,99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf3 = Node(\
            KeySet([87, None]),\
            PointerSet([None,None,leaf4]))
        leaf2 = Node(\
            KeySet([66,None]),\
            PointerSet([None,None,leaf3]))
        leaf1 = Node(\
            KeySet([27,None]),\
            PointerSet([None,None,leaf2]))
        leaf0 = Node(\
            KeySet([7,9]),\
            PointerSet([None,None,leaf1]))
        parent1 = Node(\
            KeySet([97,None]),\
            PointerSet([leaf3,leaf4,None]))
        parent0 = Node(\
            KeySet([27,66]),\
            PointerSet([leaf0,leaf1,leaf2]))
        root = Node(\
            KeySet([87,None]),\
            PointerSet([parent0,parent1,None]))
        btree = Index(root)

        key = 5
        lower_bound = 1
        upper_bound = 68

        expected_output = [5,7,9,27,66]

        self.assertEqual( expected_output\
            , ImplementMe.RangeSearchInIndex(\
                ImplementMe.InsertIntoIndex( btree, key ), \
                lower_bound,\
                upper_bound ) )


# Lookup range with nearly matching lower and upper bound equal to recently added key
class TestCase20(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_unknown(self):

        leaf5 = Node(\
            KeySet([97,99]),\
            PointerSet([None]*Index.FAN_OUT))
        leaf4 = Node(\
            KeySet([87, None]),\
            PointerSet([None,None,leaf5]))
        leaf3 = Node(\
            KeySet([66,None]),\
            PointerSet([None,None,leaf4]))
        leaf2 = Node(\
            KeySet([27,None]),\
            PointerSet([None,None,leaf3]))
        leaf1 = Node(\
            KeySet([7,9]),\
            PointerSet([None,None,leaf2]))
        leaf0 = Node(\
            KeySet([5,None]),\
            PointerSet([None,None,leaf1]))
        parent2 = Node(\
            KeySet([97,None]),\
            PointerSet([leaf4,leaf5,None]))
        parent1 = Node(\
            KeySet([66,None]),\
            PointerSet([leaf2,leaf3,None]))
        parent0 = Node(\
            KeySet([7,None]),\
            PointerSet([leaf0,leaf1,None]))
        root = Node(\
            KeySet([27,87]),\
            PointerSet([parent0,parent1,parent2]))
        btree = Index(root)

        key1 = 8
        key2 = 12

        lower_bound = 8
        upper_bound = 13

        expected_output = [8,9,12]

        self.assertEqual( expected_output\
            , ImplementMe.RangeSearchInIndex(\
                ImplementMe.InsertIntoIndex(\
                    ImplementMe.InsertIntoIndex( btree, key1 ),\
                    key2 ),\
                lower_bound,\
                upper_bound ) )


# Run all unit tests above.
unittest.main(argv=[''],verbosity=2, exit=False)
