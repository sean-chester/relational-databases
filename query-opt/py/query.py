# Simplified SQL Query Definition

# An attribute of a table
# It consists of two member variables:
#  * [table] A string identifier of the table in which the attribute is found
#  * [attribute] A string identifier of the attribute
class Attribute:
    table = ''
    attribute = ''
    def __init__(self, table, attribute):
        self.table = table
        self.attribute = attribute
    def __str__(self):
        return table + '.' + attribute
    def __repr__(self):
        return hash(table) ^ hash(attribute)

# A simple range-based predicate. It indicates that a specific attribute must
# take a value within the closed interval [lower_bound, upper_bound]
# It consists of three member variables:
#  * [attribute] The attribute to which the range should be applied
#  * [lower_bound] The smallest value that the attribute can take
#  * [upper_bound] The largest valuethat the attribute can take. upperbound >= lower_bound.
class RangePredicate:
    attribute = Attribute('R','a')
    lower_bound = 0
    upper_bound = 0
    def __init__(self, attribute, lb, ub):
        self.attribute = attribute
        self.lower_bound = lb
        self.upper_bound = ub

# A simple equality predicate that requires two attributes to take the same value
# It consists of two member variables:
#  * [attribute1] The left-hand operand of the equality comparison
#  * [attribute2] The right-hand operand of the equality comparison 
class EqualityPredicate:
    attribute1 = Attribute('R','a')
    attribute2 = Attribute('S','b')
    def __init__(self, att1, att2):
        self.attribute1 = att1
        self.attribute2 = att2

# Corresponds to a simple SELECT-FROM-WHERE SQL DQL query
# It consists of three member variables:
#  * [projection] the set of attributes onto which the query is projected. Attribute names are always disambiguated.
#  * [selection] A set of predicates (a mixture of RangePredicates and EqualityPredicates)
#                that each result tuple must satisfy
#  * [tables] A set of tables, *declared* as a cross-product, from which the result will be taken
class Query:
    projection = set()
    selection = set()
    tables = set()
    def __init__(self, projection, selection, tables):
        self.projection = projection
        self.selection = selection
        self.tables = tables


# An example instantiation of the Query class.
sample_query = Query( \
    ([Attribute('R', 'B')]), \
    ([EqualityPredicate(Attribute('R', 'A'), Attribute('S', 'A')), \
        RangePredicate(Attribute('S','C'), 4, 4)]), \
    (['R','S']))
