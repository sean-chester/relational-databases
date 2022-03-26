# Definition of a Linearised B+-tree index class with fan-out 3
# The keys are unsigned (i.e., non-negative) integers.
#
# This is a *linearised* tree, i.e., it is implemented as an array rather
# than with pointers. As you have seen in previous classes, one can
# implement a binary tree of height *h* with an array of length *2^h* as follows:
#   * the root is at index 1
#   * the left child of the node at index i is at 2i
#   * the right child of the node at index i is at 2i + 1
# This corresponds to a breadth-first search of a full binary tree.
#
# In this assignment, you will use a fan-out of three, i.e., a ternary tree.
# We can apply the same logic, and represent a ternary tree of height *h*
# with an array of length *3^h* as follows:
#   * the root is at index 1
#   * the left child of the node at index i is at 3i
#   * the middle child of the node at index i is 3i + 1
#   * the right child of the node at index i is at 3i + 2
# This again corresponds to a breadth-first search of a full ternary tree,
# starting at index 1 (with cell 0 left empty/unused).
#
# You should implement a constructor for the B+-tree that constructs
# an index for a table. The complication is that you are also given a
# representation of a SQL query, and you should build not just any index,
# but the one best suited to that SQL query. As this logic is quite complex,
# we will use the Builder Pattern instead of a constructor

from functools import reduce

# Arbitrarily chosen prime number for use in hash functions
arbitrary_prime = 7879

# Defines the set of keys in a ternary B+-tree. Observe that there are always
# two such keys, though some may hold the sentinel value of -1.
# The only member variable is a 2-tuple of integer values. Order is important.
class KeySet:
    keys = (-1,-1)
    def __init__(self, keys):
        self.keys = keys
    def __str__(self):
        return str(keys)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return ( keys[ 0 ] * arbitrary_prime ) ^ ( keys[ 1 ] * arbitrary_prime )
    def __eq__(self, other):
        return self.keys == other.keys

# Defines the set of pointers in a ternary B+-tree. These should point to array
# indices at which the children can be found, or use the 0 sentinel value in the
# i'th positio iff there is no (i+1)'st child. Order, again, is important.
class PointerSet:
    pointers = (0,0,0)
    def __init__(self, pointers):
        self.pointers = pointers
    def __str__(self):
        return str(pointers)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return ( pointers[ 0 ] * arbitrary_prime ) \
        ^ ( pointers[ 1 ] * arbitrary_prime ) \
        ^ ( pointers[ 2 ] * arbitrary_prime )
    def __eq__(self, other):
        return self.pointers == other.pointers

# A B+-tree node consists of a set of keys and pointers. If this is a leaf
# node, all pointers should be sentinel values (-1). If this is a directory
# node, only those pointers that correspond to child sub-trees should be non-zero.
class Node:
    keys = KeySet([-1,-1])
    pointers = PointerSet([0,0,0])
    def __init__(self, keys, pointers):
        self.keys = keys 
        self.pointers = pointers
    def __str__(self):
        return str(keys) + "|" + str(pointers)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return hash(keys) ^ hash(pointers)
    def __eq__(self, other):
        return self.keys == other.keys and self.pointers == other.pointers

# A B+-tree index is thus just an ordered list of nodes. Array position
# implies position in the tree. The length of the list should be exactly
# *3^h*, where *h* is the height of the tree. The last nodes may very well be
# full of nothing but sentinel values (-1 for keys and 0 for pointers).
class Index:
    nodes = []
    def __init__(self, nodes):
        self.nodes = nodes
    def __str__(self):
        return str(nodes)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return reduce(lambda x,y: x^y, [hash(x) for x in self.nodes])
    def __eq__(self, other):
        return self.nodes == other.nodes


# @TODO Implement Me!!
# Returns the B+-tree ternary index that minimises I/O's for answering the given
# query on the given table instances, or None if no such tree exists.
def buildBestIndex(query, tables):
    return None

