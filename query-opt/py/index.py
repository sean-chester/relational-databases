# Definition of a Linearised B+-tree index class with fan-out 3
# The keys are unsigned (i.e., non-negative) integers.
#
# This is a *linearised* tree, i.e., it is implemented as an array rather
# than with pointers. As you have seen in previous classes, one can
# implement a binary tree of height *h* with an array of length *2^h-1* as follows:
#   * the root (if it exists) is at index 0
#   * the left child of the node at index i is at 2i + 1
#   * the right child of the node at index i is at 2i + 2
# This corresponds to a breadth-first search of a full binary tree.
#
# In this assignment, you will use a fan-out of three, i.e., a ternary tree.
# We can apply the same logic, and represent a ternary tree of height *h*
# with an array of length *(1-3^h)/-2* as follows:
#   * the root (if it exists) is at index 0
#   * the left child of the node at index i is at 3i + 1
#   * the middle child of the node at index i is 3i + 2
#   * the right child of the node at index i is at 3i + 3
# This corresponds to a breadth-first search of a full ternary tree.
#
# This B+-tree class does not have any (non-builtin) member functions,
# but all member variables are public. You will implement the functionality
# in another (implementation) file.

from node import *
from functools import reduce

# A B+-tree index is thus just an ordered list of nodes. Array position
# implies position in the tree. The length of the list should be exactly
# *3^h*, where *h* is the height of the tree. The last nodes may very well be
# full of nothing but sentinel values (-1 for keys and 0 for pointers).
class Index:
    nodes = []
    def __init__(self, nodes):
        self.nodes = nodes
    def __str__(self):
        return str(self.nodes)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return reduce(lambda x,y: x^y, [hash(x) for x in self.nodes])
    def __eq__(self, other):
        return self.nodes == other.nodes
