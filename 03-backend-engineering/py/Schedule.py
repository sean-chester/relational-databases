# Definitions of concurrency schedules. 
#
# There are two types of schedules: a "simple" schedule that
# only contains a list of transaction ids and a "normal" schedule
# that contains a list of operations that specify a read or write
# to a database element by a specific transaction.

# An IOOperation represents a single read/write operation on a database.
# It is a struct/sum type of three components:
#   * a transaction id, which is an integer that uniquely identifies a transaction
#   * an operation, which is an enum that can take on only the values "READ" and "WRITE",
#     indicating whether this particular operation merely accesses data or modifies it, respectively
#   * an element, which is a string that uniquely identifies some atomic element of a database, such
#     as an I/O block. Reads and writes occur to entire elements and reads and writes to distinct
#     elements are independent.
class IOOperation:
    def __init__(self, transaction = 1, operation = "READ", element = "A"):
        assert operation == "READ" or operation == "WRITE", "Invalid read/write operation"
        self.transaction_id = transaction
        self.operation = operation
        self.database_element = element
    def __str__(self):
        return str((self.transaction_id, self.operation, self.database_element))
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return self.transaction_id ^ hash(self.operation) ^ hash(self.database_element)
    def __eq__(self, other):
        return self.transaction_id == other.transaction_id \
        and self.operation == other.operation \
        and self.database_element == other.database_element


# A Schedule is an (ordered) list of IOOperations.
# It represents the order in which a series of read/write operations occur in a database
class Schedule:
    def __init__(self, operations = list()):
        self.operations = operations
    def __str__(self):
        return str(self.operations)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return hash(self.operations)
    def __eq__(self, other):
        return self.operations == other.operations


# A SimpleSchedule is an (ordered) list of transaction ids, i.e., integers.
# It represents the order in which a series of transactions are (serially) executed.
class SimpleSchedule:
    def __init__(self, transactions = list()):
        self.transactions = transactions
    def __str__(self):
        return str(self.transactions)
    def __repr__(self):
        return str(self)
    def __hash__(self):
        return hash(self.transactions)
    def __eq__(self, other):
        return self.transactions == other.transactions
