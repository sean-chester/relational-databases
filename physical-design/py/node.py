# Definition of a B+-tree node class with fan-out 3.
# The keys are integers. There are no values associated
# with the keys: the leaf pointers are null (except for
# the (k+1)'st pointer, which participates in the linked
# list)
#
# This file will not be submitted; so, you are encouraged
# not to make functional changes to it.


# Arbitrarily chosen prime number for use in hash functions
class Constants:
    a_prime = 7879

# Defines the set of keys in a ternary B+-tree. Observe that there are always
# two such keys, though some may hold the sentinel value of None.
# The only member variable is a 2-tuple of integer values. Order is important.
class KeySet:
    NUM_KEYS = 2
    def __init__(self, keys = None):
        self.keys = keys if keys else [None]*KeySet.NUM_KEYS
    def __str__(self):
        return str(self.keys)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        if keys[ 0 ] is None:
            return 0
        return reduce(lambda x, y: x^y, [x * Constants.a_prime for x in keys if x is not None])
    def __eq__(self, other):
        return self.keys == other.keys

# Defines the set of pointers in a ternary B+-tree. These should be references
# to Node objects at which the children can be found, or use the None sentinel value in the
# i'th position iff there is no (i+1)'st child. Order, again, is important.
class PointerSet:
    FAN_OUT = 3
    def __init__(self, pointers = None):
        self.pointers = pointers if pointers else [None]*PointerSet.FAN_OUT
    def __str__(self):
        return str(self.pointers)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        if pointers[ 0 ] is None:
            return 0
        return reduce(lambda x, y: x^y, [hash(x) * Constants.a_prime for x in pointers if x is not None]) 
    def __eq__(self, other):
        return self.pointers == other.pointers

# A B+-tree node consists of a set of keys and pointers. If this is a leaf
# node, the first pointer should have a sentinel value: None. If this is a directory
# node with k children, only the first k pointers should be non-None.
class Node:
    def __init__(self, keys = None, pointers = None):
        self.keys = keys if keys else KeySet()
        self.pointers = pointers if pointers else PointerSet()
    def __str__(self):
        return "Node(" + str(self.keys) + "|" + str(self.pointers) +")"
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return hash(keys) ^ hash(pointers)
    def __eq__(self, other):
        return self.keys == other.keys and self.pointers == other.pointers
    @staticmethod
    def get_num_keys():
        return KeySet.NUM_KEYS
    @staticmethod
    def get_fan_out():
        return KeySet.NUM_KEYS + 1
