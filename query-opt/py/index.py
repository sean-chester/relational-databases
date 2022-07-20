# Definition of a B+-tree index class with fan-out 3
# The keys are integers.
#
# This B+-tree class does not have any (non-builtin) member functions,
# but all member variables are public. You will implement the functionality
# in another (implementation) file.

from node import *
from functools import reduce

class Index:
    root = Node()
    def __init__(self, root = Node()):
        self.root = root
    def __str__(self):
        return str(self.root)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return hash(root)
    def __eq__(self, other):
        return self.root == other.root
