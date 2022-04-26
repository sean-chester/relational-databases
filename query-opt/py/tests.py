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
        key = 99

        expected_output = Index([Node()]*1)
        expected_output.nodes[ 0 ] = Node(\
            KeySet((99, -1)),\
            PointerSet((0,0,0)))

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert existing key
class TestCase02(unittest.TestCase):
    def test_insertion(self):
        btree = Index([Node()]*1)
        btree.nodes[ 0 ] = Node(\
            KeySet((99, -1)),\
            PointerSet((0,0,0)))
        key = 99

        expected_output = Index([Node()]*1)
        expected_output.nodes[ 0 ] = Node(\
            KeySet((99, -1)),\
            PointerSet((0,0,0)))

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into existing node that is not full
class TestCase03(unittest.TestCase):
    def test_insertion(self):
        btree = Index([Node()]*1)
        btree.nodes[ 0 ] = Node(\
            KeySet((87, -1)),\
            PointerSet((0,0,0)))
        key = 66

        expected_output = Index([Node()]*1)
        expected_output.nodes[ 0 ] = Node(\
            KeySet((66, 87)),\
            PointerSet((0,0,0)))

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into full node.
class TestCase04(unittest.TestCase):
    def test_insertion(self):
        btree = Index([Node()]*1)
        btree.nodes[ 0 ] = Node(\
            KeySet((66, 99)),\
            PointerSet((0,0,0)))
        key = 87

        expected_output = Index([Node()]*4)
        expected_output.nodes[0] = Node(\
                KeySet((87, -1)),\
                PointerSet((1,2,0)))
        expected_output.nodes[1] = Node(\
                KeySet((66,-1)),\
                PointerSet((0,0,2)))
        expected_output.nodes[2]=Node(\
                KeySet((87,99)),\
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
                KeySet((66,87)),\
                PointerSet((0,0,0)))
        key = 99

        expected_output = Index([Node()]*13)
        expected_output.nodes[0] = Node(\
                KeySet((66, -1)),\
                PointerSet((1,2,0)))
        expected_output.nodes[1] = Node(\
                KeySet((42,-1)),\
                PointerSet((4,5,0)))
        expected_output.nodes[2]=Node(\
                KeySet((87,-1)),\
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
                KeySet((87,99)),\
                PointerSet((0,0,0)))

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insert into full node with full parent, but does not cause a root split.
# Note that only the path that should be affected has correct data (testing complexity)
# Linearisation forces copy of some nodes to new addresses
class TestCase06(unittest.TestCase):
    def test_insertion(self):
        btree = Index([Node()]*13)
        btree.nodes[0] = Node(\
                KeySet((7, -1)),\
                PointerSet((1,2,0)))
        btree.nodes[2]=Node(\
                KeySet((27,66)),\
                PointerSet((7,8,9)))
        btree.nodes[6]=Node(\
                KeySet((11,11)),\
                PointerSet((0,0,90))) # Dummy data for test
        btree.nodes[7]=Node(\
                KeySet((7,9)),\
                PointerSet((0,0,8)))
        btree.nodes[8]=Node(\
                KeySet((27,-1)),\
                PointerSet((0,0,9)))
        btree.nodes[9]=Node(\
                KeySet((66,88)),\
                PointerSet((0,0,0)))
        key = 12


        expected_output = Index([Node()]*13)
        expected_output.nodes[0] = Node(\
                KeySet((7, 27)),\
                PointerSet((1,2,3)))
        expected_output.nodes[2] = Node(\
                KeySet((9,-1)),\
                PointerSet((4,5,0)))
        expected_output.nodes[3]=Node(\
                KeySet((66,-1)),\
                PointerSet((7,8,0)))
        expected_output.nodes[6]=Node(\
                KeySet((11,11)),\
                PointerSet((0,0,90))) # Dummy data for test
        expected_output.nodes[7]=Node(\
                KeySet((7,-1)),\
                PointerSet((0,0,8)))
        expected_output.nodes[8]=Node(\
                KeySet((9,12)),\
                PointerSet((0,0,10)))
        expected_output.nodes[10]=Node(\
                KeySet((27,-1)),\
                PointerSet((0,0,11)))
        expected_output.nodes[11]=Node(\
                KeySet((66,88)),\
                PointerSet((0,0,0)))

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Insertion causes splits that propagates at least three times
# Note that only the path that should be affected has correct data (testing complexity)
# Linearisation forces copy of some nodes to new addresses
class TestCase07(unittest.TestCase):
    def test_insertion(self):
        btree = Index([Node()]*13)
        btree.nodes[0] = Node(\
                KeySet((7, 99)),\
                PointerSet((1,2,0)))
        btree.nodes[2]=Node(\
                KeySet((27,66)),\
                PointerSet((7,8,9)))
        btree.nodes[7]=Node(\
                KeySet((7,9)),\
                PointerSet((0,0,8)))
        btree.nodes[8]=Node(\
                KeySet((27,-1)),\
                PointerSet((0,0,9)))
        btree.nodes[9]=Node(\
                KeySet((66,88)),\
                PointerSet((0,0,0)))
        key = 12

        expected_output = Index([Node()]*40)
        expected_output.nodes[0] = Node(\
                KeySet((27, -1)),\
                PointerSet((1,2,0)))
        expected_output.nodes[1] = Node(\
                KeySet((7, -1)),\
                PointerSet((4,5,0)))
        expected_output.nodes[2] = Node(\
                KeySet((99, -1)),\
                PointerSet((7,8,0)))
        expected_output.nodes[5] = Node(\
                KeySet((9,-1)),\
                PointerSet((16,17,0)))
        expected_output.nodes[7]=Node(\
                KeySet((66,-1)),\
                PointerSet((22,23,0)))
        expected_output.nodes[16]=Node(\
                KeySet((7,-1)),\
                PointerSet((0,0,17)))
        expected_output.nodes[17]=Node(\
                KeySet((9,12)),\
                PointerSet((0,0,22)))
        expected_output.nodes[22]=Node(\
                KeySet((27,-1)),\
                PointerSet((0,0,23)))
        expected_output.nodes[23]=Node(\
                KeySet((66,88)),\
                PointerSet((0,0,0)))

        self.assertEqual( expected_output, ImplementMe.InsertIntoIndex( btree, key ) )


# Boundary case: lookup smallest key in tree
# Fake data in last node to test complexity
class TestCase08(unittest.TestCase):
    def test_lookup(self):
        btree = Index([Node()]*4)
        btree.nodes[0] = Node(\
                KeySet((42, 66)),\
                PointerSet((1,2,3)))
        btree.nodes[1] = Node(\
                KeySet((9,-1)),\
                PointerSet((0,0,2)))
        btree.nodes[2]=Node(\
                KeySet((42,-1)),\
                PointerSet((0,0,3)))
        btree.nodes[3]=Node(\
                KeySet((66,7)),\
                PointerSet((0,0,0)))
        key = 9

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Boundary case: lookup largest key in tree
# Fake data in first node to test complexity
class TestCase09(unittest.TestCase):
    def test_lookup(self):
        btree = Index([Node()]*4)
        btree.nodes[0] = Node(\
                KeySet((42, 66)),\
                PointerSet((1,2,3)))
        btree.nodes[1] = Node(\
                KeySet((7,99)),\
                PointerSet((0,0,2)))
        btree.nodes[2]=Node(\
                KeySet((42,-1)),\
                PointerSet((0,0,3)))
        btree.nodes[3]=Node(\
                KeySet((66,87)),\
                PointerSet((0,0,0)))
        key = 42

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )




# Lookup key outside range of tree's keys
# Fake data in middle leaf to test complexity
class TestCase10(unittest.TestCase):
    def test_lookup(self):
        btree = Index([Node()]*4)
        btree.nodes[0] = Node(\
                KeySet((42, 66)),\
                PointerSet((1,2,3)))
        btree.nodes[1] = Node(\
                KeySet((9,-1)),\
                PointerSet((0,0,2)))
        btree.nodes[2]=Node(\
                KeySet((7,-1)),\
                PointerSet((0,0,3)))
        btree.nodes[3]=Node(\
                KeySet((66,99)),\
                PointerSet((0,0,0)))
        key = 7

        expected_output = False

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )


# Lookup key within tree's range but not in tree
# Fake data in one leaf to test complexity
class TestCase11(unittest.TestCase):
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
                KeySet((66,9)),\
                PointerSet((0,0,0)))
        key = 9

        expected_output = False

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex( btree, key ) )

# Lookup key strictly within the tree's range
class TestCase12(unittest.TestCase):
    def test_lookup(self):
        btree = Index([Node()]*4)
        btree.nodes[0] = Node(\
                KeySet((41, 66)),\
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
# Fake data in other node to test complexity
class TestCase13(unittest.TestCase):
    def test_range(self):
        btree = Index([Node()]*4)
        btree.nodes[0] = Node(\
                KeySet((42, 66)),\
                PointerSet((1,2,3)))
        btree.nodes[1] = Node(\
                KeySet((7,68)),\
                PointerSet((0,0,2)))
        btree.nodes[2]=Node(\
                KeySet((42,-1)),\
                PointerSet((0,0,3)))
        btree.nodes[3]=Node(\
                KeySet((66,99)),\
                PointerSet((0,0,0)))
        lower_bound = 66
        upper_bound = 87

        expected_output = [66]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Range query half-open to the left
# Fake data in one node to test complexity.
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
                KeySet((66,9)),\
                PointerSet((0,0,0)))
        lower_bound = 0
        upper_bound = 42

        expected_output = [7]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Range query half-open to the right 
# Fake data in one node to test complexity
class TestCase15(unittest.TestCase):
    def test_range(self):
        btree = Index([Node()]*4)
        btree.nodes[0] = Node(\
                KeySet((42, 66)),\
                PointerSet((1,2,3)))
        btree.nodes[1] = Node(\
                KeySet((7,68)),\
                PointerSet((0,0,2)))
        btree.nodes[2]=Node(\
                KeySet((42,-1)),\
                PointerSet((0,0,3)))
        btree.nodes[3]=Node(\
                KeySet((66,87)),\
                PointerSet((0,0,0)))
        lower_bound = 42
        upper_bound = 99

        expected_output = [9,42,66,87]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Range query with matching upper and lower bound
# Key not in tree but found as fake data in a different node to test complexity
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
                KeySet((66,7)),\
                PointerSet((0,0,0)))
        lower_bound = 7
        upper_bound = 7

        expected_output = []

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Multi-leaf range query in middle of tree
# Fake data in first node to test complexity
class TestCase17(unittest.TestCase):
    def test_range(self):
        btree = Index([Node()]*4)
        btree.nodes[0] = Node(\
                KeySet((42, 66)),\
                PointerSet((1,2,3)))
        btree.nodes[1] = Node(\
                KeySet((68,-1)),\
                PointerSet((0,0,2)))
        btree.nodes[2]=Node(\
                KeySet((42,-1)),\
                PointerSet((0,0,3)))
        btree.nodes[3]=Node(\
                KeySet((66,99)),\
                PointerSet((0,0,0)))
        lower_bound = 42
        upper_bound = 87

        expected_output = [42,66]

        self.assertEqual( expected_output, ImplementMe.RangeSearchInIndex( btree, lower_bound, upper_bound ) )


# Lookup recently added key
class TestCase18(unittest.TestCase):
    def test_unknown(self):
        btree = Index([Node()]*13)
        btree.nodes[0] = Node(\
                KeySet((7, 99)),\
                PointerSet((1,2,0)))
        btree.nodes[2]=Node(\
                KeySet((27,66)),\
                PointerSet((7,8,9)))
        btree.nodes[7]=Node(\
                KeySet((7,9)),\
                PointerSet((0,0,8)))
        btree.nodes[8]=Node(\
                KeySet((27,-1)),\
                PointerSet((0,0,9)))
        btree.nodes[9]=Node(\
                KeySet((66,88)),\
                PointerSet((0,0,0)))
        key = 12

        expected_output = True

        self.assertEqual( expected_output, ImplementMe.LookupKeyInIndex(\
        ImplementMe.InsertIntoIndex( btree, key ), key ) )



# Lookup range that includes recently added key
class TestCase19(unittest.TestCase):
    def test_unknown(self):
        btree = Index([Node()]*13)
        btree.nodes[0] = Node(\
                KeySet((7, 99)),\
                PointerSet((1,2,0)))
        btree.nodes[2]=Node(\
                KeySet((27,66)),\
                PointerSet((7,8,9)))
        btree.nodes[7]=Node(\
                KeySet((7,9)),\
                PointerSet((0,0,8)))
        btree.nodes[8]=Node(\
                KeySet((27,-1)),\
                PointerSet((0,0,9)))
        btree.nodes[9]=Node(\
                KeySet((66,88)),\
                PointerSet((0,0,0)))
        key = 12
        lower_bound = 12
        upper_bound = 66

        expected_output = [12,27]

        self.assertEqual( expected_output, expected_output )


# Lookup range with matching lower and upper bound equal to recently added key
class TestCase20(unittest.TestCase):
    def test_unknown(self):
        btree = Index([Node()]*13)
        btree.nodes[0] = Node(\
                KeySet((7, 99)),\
                PointerSet((1,2,0)))
        btree.nodes[2]=Node(\
                KeySet((27,66)),\
                PointerSet((7,8,9)))
        btree.nodes[7]=Node(\
                KeySet((7,9)),\
                PointerSet((0,0,8)))
        btree.nodes[8]=Node(\
                KeySet((27,-1)),\
                PointerSet((0,0,9)))
        btree.nodes[9]=Node(\
                KeySet((66,88)),\
                PointerSet((0,0,0)))
        key = 12
        lower_bound = 12
        upper_bound = 66

        expected_output = [12]

        self.assertEqual( expected_output, expected_output )


# Freebie for grinding out a tough semester
# Look up a key in an empty tree
class TestCaseB1(unittest.TestCase):
    def test_unknown(self):
        btree = Index([Node()]*1)
        key = 9

        expected_output = False

        self.assertEqual( expected_output, expected_output )



# Run all unit tests above.
unittest.main(argv=[''],verbosity=2, exit=False)
