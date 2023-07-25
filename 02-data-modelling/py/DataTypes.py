# Sum type to group together a table name and a list of
# attributes contained therein
class Attributes:
    def __init__( self, table_name, attributes ):
        self.table_name = table_name
        self.attributes = attributes

# Sum type representing a referential integrity policy
# as a database operation and a policy for handling violations
class RefIntegrityPolicy:
    def __init__( self, operation, policy ):
    	assert operation == "UPDATE" or operation == "DELETE" or operation == "INSERT", "Invalid operation"
    	assert policy == "CASCADE" or policy == "REJECT" or policy == "SET NULL", "Invalid policy"
        self.operation = operation
        self.policy = policy
