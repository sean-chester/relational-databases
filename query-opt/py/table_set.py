# Defines a set of table instances in a relational database


# Corresponds to an instance of a table in a relational database
# It consists of three member variables:
#   * [name] A unique string identifier for the table
#   * [attributes] An (ordered) tuple of column headers/attribute names
#   * [tuples] A list of tuples of integers of a fixed width
class Table:
    name = ''
    attributes = ()
    tuples = []
    def __init__(self, name, attributes, data):
        self.name = name
        self.attributes = attributes
        self.tuples = data

# Corresponds to a MySQL table that supports primary and foreign keys and only INT attributes.
# It consists of four member variables:
#   * [name] The name of the table (unique identifier/slug)
#   * [attributes] The set of string-valued attributes in this table
#   * [primary_key] The set of string-valued attributes that form the primary key of this table
#   * [foreign_keys] The set of foreign keys. Each foreign key is a three-tuple of:
#       - An ordered tuple of attributes in this table to which the FK is applied
#       - The name of the table that the foreign key should reference
#       - An ordered tuple of attributes in the foreign table that are being referenced 
class DatabaseInstance:
    tables = set()
    def __init__(self, tables):
        self.tables = tables


# An example instantiation of the DatabaseInstance class.
sample_db = DatabaseInstance([ \
    Table('R', ('A','B'), [(1,2), (2,3), (3,4)]), \
    Table('S', ('C','A'), [(4,1),(5,2),(6,1),(7,3)])])
