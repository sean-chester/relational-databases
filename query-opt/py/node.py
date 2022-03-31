# Definition of a B+-tree node class with fan-out 3.
# The keys are unsigned (i.e., non-negative) integers.
#
# This file will not be submitted; so, you are encouraged
# not to make functional changes to it.


# Arbitrarily chosen prime number for use in hash functions
class Constants:
    arbitrary_prime = 7879

# Defines the set of keys in a ternary B+-tree. Observe that there are always
# two such keys, though some may hold the sentinel value of -1.
# The only member variable is a 2-tuple of integer values. Order is important.
class KeySet:
    keys = (-1,-1)
    def __init__(self, keys):
        self.keys = keys
    def __str__(self):
        return str(self.keys)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return ( keys[ 0 ] * Constants.arbitrary_prime ) \
        ^ ( keys[ 1 ] * Constants.arbitrary_prime )
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
        return str(self.pointers)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return ( pointers[ 0 ] * Constants.arbitrary_prime ) \
        ^ ( pointers[ 1 ] * Constants.arbitrary_prime ) \
        ^ ( pointers[ 2 ] * Constants.arbitrary_prime )
    def __eq__(self, other):
        return self.pointers == other.pointers

# A B+-tree node consists of a set of keys and pointers. If this is a leaf
# node, all pointers should be sentinel values (-1). If this is a directory
# node, only those pointers that correspond to child sub-trees should be non-zero.
class Node:
    keys = KeySet((-1,-1))
    pointers = PointerSet((0,0,0))
    def __init__(self, keys = KeySet((-1,-1)), pointers = PointerSet((0,0,0))):
        self.keys = keys 
        self.pointers = pointers
    def __str__(self):
        return str(self.keys) + "|" + str(self.pointers)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return hash(keys) ^ hash(pointers)
    def __eq__(self, other):
        return self.keys == other.keys and self.pointers == other.pointers
