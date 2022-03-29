# Test cases for ImplementMe class.
# The mocked objects (and therefore expected output) may change
# at the point of evaluation, including into a more complex object,  
# but the functionality tested by each test case will not.
# Your implementation should anticipate ways in which these mocks could
# be more complex.
#
# Three cases are not yet disclosed; they will be challenging combinations
# of existing test cases.

import unittest
from node import *
from index import *
from implement_me import ImplementMe


# Insert into an empty tree
class TestCase01(unittest.TestCase):
    def test_insertion(self):
        btree = Index([])
        key = 42

        expected_output = Index([Node()]*1)
        expected_output.nodes[ 0 ] = Node(\
            KeySet((42, -1)),\
            PointerSet((0,0,0)))

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert existing key
class TestCase02(unittest.TestCase):
    def test_insertion(self):
        btree = Index([Node()]*1)
        btree.nodes[ 0 ] = Node(\
            KeySet((42, -1)),\
            PointerSet((0,0,0)))
        key = 42

        expected_output = Index([Node()]*1)
        expected_output.nodes[ 0 ] = Node(\
            KeySet((42, -1)),\
            PointerSet((0,0,0)))

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into existing node that is not full
class TestCase03(unittest.TestCase):
    def test_insertion(self):
        btree = Index([Node()]*1)
        btree.nodes[ 0 ] = Node(\
            KeySet((42, -1)),\
            PointerSet((0,0,0)))
        key = 99

        expected_output = Index([Node()]*1)
        expected_output.nodes[ 0 ] = Node(\
            KeySet((42, 99)),\
            PointerSet((0,0,0)))

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into full node.
class TestCase04(unittest.TestCase):
    def test_insertion(self):
        btree = Index([Node()]*1)
        btree.nodes[ 0 ] = Node(\
            KeySet((42, -1)),\
            PointerSet((0,0,0)))
        key = 7

        expected_output = Index([Node()]*4)
        expected_output.nodes[0] = Node(\
                KeySet((42, -1)),\
                PointerSet((1,2,0)))
        expected_output.nodes[1] = Node(\
                KeySet((7,-1)),\
                PointerSet((0,0,2)))
        expected_output.nodes[2]=Node(\
                KeySet((42,99)),\
                PointerSet((0,0,0)))

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into full node with full parent, causing root split.
class TestCase05(unittest.TestCase):
    def test_insertion(self):
        btree = Index([Node()]*4)
        btree.nodes[0] = Node(\
                KeySet((42, 66)),\
                PointerSet((1,2,3)))
        btree.nodes[1] = Node(\
                KeySet((7,-1)),\
                PointerSet((0,0,2)))
        btree.nodes[2]=Node(\
                KeySet((42,-1)),\
                PointerSet((0,0,3)))
        btree.nodes[3]=Node(\
                KeySet((66,99)),\
                PointerSet((0,0,0)))
        key = 68

        expected_output = Index([Node()]*13)
        expected_output.nodes[0] = Node(\
                KeySet((66, -1)),\
                PointerSet((1,2,0)))
        expected_output.nodes[1] = Node(\
                KeySet((42,-1)),\
                PointerSet((4,5,0)))
        expected_output.nodes[2]=Node(\
                KeySet((68,-1)),\
                PointerSet((7,8,0)))
        expected_output.nodes[4]=Node(\
                KeySet((7,-1)),\
                PointerSet((0,0,5)))
        expected_output.nodes[5]=Node(\
                KeySet((42,-1)),\
                PointerSet((0,0,7)))
        expected_output.nodes[7]=Node(\
                KeySet((66,-1)),\
                PointerSet((0,0,8)))
        expected_output.nodes[8]=Node(\
                KeySet((68,99)),\
                PointerSet((0,0,0)))

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into full node with full parent, but does not cause a root split.
class TestCase06(unittest.TestCase):
    def test_insertion(self):
        btree = Index([]) # not provided
        key = 87

        expected_output = Index([]) # Not provided

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insertion causes splits that propagates at least three times
class TestCase07(unittest.TestCase):
    def test_insertion(self):
        btree = Index([]) # not provided
        key = 87

        expected_output = Index([]) # Not provided

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Lookup key outside range of tree's keys
class TestCase08(unittest.TestCase):
    def test_lookup(self):
        btree = Index([Node()]*1)
        btree.nodes[ 0 ] = Node(\
            KeySet((42, 99)),\
            PointerSet((0,0,0)))
        key = 7

        expected_output = False

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Lookup key within tree's range but not in tree
class TestCase09(unittest.TestCase):
    def test_lookup(self):
        btree = Index([Node()]*1)
        btree.nodes[ 0 ] = Node(\
            KeySet((42, 99)),\
            PointerSet((0,0,0)))
        key = 66

        expected_output = False

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Boundary case: lookup smallest key in tree
class TestCase10(unittest.TestCase):
    def test_lookup(self):
        btree = Index([Node()]*1)
        btree.nodes[ 0 ] = Node(\
            KeySet((42, 99)),\
            PointerSet((0,0,0)))
        key = 42

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Boundary case: lookup largest key in tree
class TestCase11(unittest.TestCase):
    def test_lookup(self):
        btree = Index([Node()]*1)
        btree.nodes[ 0 ] = Node(\
            KeySet((42, 99)),\
            PointerSet((0,0,0)))
        key = 99

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Lookup key strictly within the tree's range
class TestCase12(unittest.TestCase):
    def test_lookup(self):
        btree = Index([Node()]*4)
        btree.nodes[0] = Node(\
                KeySet((42, 66)),\
                PointerSet((1,2,3)))
        btree.nodes[1] = Node(\
                KeySet((7,-1)),\
                PointerSet((0,0,2)))
        btree.nodes[2]=Node(\
                KeySet((42,-1)),\
                PointerSet((0,0,3)))
        btree.nodes[3]=Node(\
                KeySet((66,99)),\
                PointerSet((0,0,0)))
        key = 42

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Range query fully contained in one leaf node
class TestCase13(unittest.TestCase):
    def test_range(self):
        btree = Index([Node()]*4)
        btree.nodes[0] = Node(\
                KeySet((42, 66)),\
                PointerSet((1,2,3)))
        btree.nodes[1] = Node(\
                KeySet((7,-1)),\
                PointerSet((0,0,2)))
        btree.nodes[2]=Node(\
                KeySet((42,-1)),\
                PointerSet((0,0,3)))
        btree.nodes[3]=Node(\
                KeySet((66,99)),\
                PointerSet((0,0,0)))
        lower_bound = 66
        upper_bound = 87

        expected_output = [66,]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Range query half-open to the left 
class TestCase14(unittest.TestCase):
    def test_range(self):
        btree = Index([Node()]*4)
        btree.nodes[0] = Node(\
                KeySet((42, 66)),\
                PointerSet((1,2,3)))
        btree.nodes[1] = Node(\
                KeySet((7,-1)),\
                PointerSet((0,0,2)))
        btree.nodes[2]=Node(\
                KeySet((42,-1)),\
                PointerSet((0,0,3)))
        btree.nodes[3]=Node(\
                KeySet((66,99)),\
                PointerSet((0,0,0)))
        lower_bound = 0
        upper_bound = 42

        expected_output = [7,]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Range query half-open to the right 
class TestCase15(unittest.TestCase):
    def test_range(self):
        btree = Index([Node()]*4)
        btree.nodes[0] = Node(\
                KeySet((42, 66)),\
                PointerSet((1,2,3)))
        btree.nodes[1] = Node(\
                KeySet((7,-1)),\
                PointerSet((0,0,2)))
        btree.nodes[2]=Node(\
                KeySet((42,-1)),\
                PointerSet((0,0,3)))
        btree.nodes[3]=Node(\
                KeySet((66,87)),\
                PointerSet((0,0,0)))
        lower_bound = 7
        upper_bound = 99

        expected_output = [7,42,66,87,]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Range query with matching upper and lower bound 
class TestCase16(unittest.TestCase):
    def test_range(self):
        btree = Index([Node()]*4)
        btree.nodes[0] = Node(\
                KeySet((42, 66)),\
                PointerSet((1,2,3)))
        btree.nodes[1] = Node(\
                KeySet((7,-1)),\
                PointerSet((0,0,2)))
        btree.nodes[2]=Node(\
                KeySet((42,-1)),\
                PointerSet((0,0,3)))
        btree.nodes[3]=Node(\
                KeySet((66,87)),\
                PointerSet((0,0,0)))
        lower_bound = 7
        upper_bound = 7

        expected_output = []

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Multi-leaf range query in middle of tree
class TestCase17(unittest.TestCase):
    def test_range(self):
        btree = Index([Node()]*4)
        btree.nodes[0] = Node(\
                KeySet((42, 66)),\
                PointerSet((1,2,3)))
        btree.nodes[1] = Node(\
                KeySet((7,-1)),\
                PointerSet((0,0,2)))
        btree.nodes[2]=Node(\
                KeySet((42,-1)),\
                PointerSet((0,0,3)))
        btree.nodes[3]=Node(\
                KeySet((66,99)),\
                PointerSet((0,0,0)))
        lower_bound = 42
        upper_bound = 87

        expected_output = [42,66,]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Not disclosed
class TestCase18(unittest.TestCase):
    def test_unknown(self):
        btree = Index([]) # Not disclosed

        expected_output = False # Not disclosed, not even type

        self.assertEqual( expected_output, expected_output )



# Not disclosed
class TestCase19(unittest.TestCase):
    def test_unknown(self):
        btree = Index([]) # Not disclosed

        expected_output = False # Not disclosed, not even type

        self.assertEqual( expected_output, expected_output )


# Not disclosed
class TestCase20(unittest.TestCase):
    def test_unknown(self):
        btree = Index([]) # Not disclosed

        expected_output = False # Not disclosed, not even type

        self.assertEqual( expected_output, expected_output )



# Run all unit tests above.
unittest.main(argv=[''],verbosity=2, exit=False)
