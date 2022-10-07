# Definition of a set of relations for a relational database.
#
# These classes do not have any (non-builtin) member functions,
# but all member variables are public. You will implement the functionality
# in another (implementation) file.

from functools import reduce

# A simplified relation for a relational database.
#
# A relation is typically defined by a name
# and a set of attributes. For simplicity,
# instances of this class are unnamed and
# consist only of a set of attributes.
# Attributes can be of any type, but are generally
# assumed to be single characters.
# For example, an instance of this class
# could be declared with:
#   r1 = Relation(set(['A','B']))
# and this is equal to an instance declared as:
#   r2 = Relation(set(['B','A']))
class Relation:
    def __init__(self, attributes = set()):
        self.attributes = attributes
    def __str__(self):
        return str(self.attributes)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        if len( self.attributes ) == 0:
            return 0
        return reduce(lambda x,y: x^y, [hash(x) for x in self.attributes])
    def __eq__(self, other):
        return self.attributes == other.attributes

# A set of relations that together define
# the structure of a relational database
class RelationSet:
    def __init__(self, relations = set()):
        self.relations = relations
    def __str__(self):
        return str(self.relations)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        if len( self.relations ) == 0:
            return 0
        return reduce(lambda x,y: x^y, [hash(x) for x in self.relations])
    def __eq__(self, other):
        return self.relations == other.relations
