# Definition of a set of functional dependencies to apply to a relational database.
#
# These classes do not have any (non-builtin) member functions,
# but all member variables are public. You will implement the functionality
# in another (implementation) file.

from functools import reduce

# Arbitrarily chosen prime number for use in hash functions
class Constants:
    arbitrary_prime = 7879

# A functional dependency of the form:
# left_hand_side → right_hand_side
#
# Both the left_hand_side and right_hand_side are
# (not necessarily disjoint) sets of attributes 
class FunctionalDependency:
    def __init__(self, lhs = set(), rhs = set()):
        self.left_hand_side = lhs
        self.right_hand_side = rhs
    def __str__(self):
        return str(self.left_hand_side) + "→" + str(self.right_hand_side)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        lhs_hash = 0
        rhs_hash = 0
        if len( self.left_hand_side ) > 0:
            lhs_hash = reduce(lambda x,y: x^y, [hash(x) for x in self.left_hand_side])
        if len( self.right_hand_side ) > 0:
            rhs_hash = reduce(lambda x,y: x^y, [hash(x) for x in self.right_hand_side])
        return ( lhs_hash + 1 ) ^ ( rhs_hash * Constants.arbitrary_prime )
    def __eq__(self, other):
        return self.left_hand_side == other.left_hand_side \
        and self.right_hand_side == other.right_hand_side


# A set of FunctionalDependency instances that together
# define the functional constraints of a relational database
class FDSet:
    def __init__(self, fds = set()):
        self.functional_dependencies = fds
    def __str__(self):
        return str(self.functional_dependencies)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        if len( self.functional_dependencies ) == 0:
            return 0
        return reduce(lambda x,y: x^y, [hash(x) for x in self.functional_dependencies])
    def __eq__(self, other):
        return self.functional_dependencies == other.functional_dependencies

