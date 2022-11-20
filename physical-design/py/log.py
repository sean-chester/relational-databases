# Definition of a REDO log.
#
# This file will not be submitted; so, you are encouraged
# not to make functional changes to it.

# A record is an atomic unit of a log file. It corresponds to one
# line of the log file and indicates that either a new transaction
# has been started, an existing transaction has aborted or committed,
# or that a transaction has updated the value of some database element
# (in this assignment, the primary key of a given tuple)
# Records are aliases for 2- or 3-tuples.
# This class is a static factory class that generates records.
class Record:
    def start_transaction( transaction_id ):
        return ("START", transaction_id)
    def rollback_transaction( transaction_id ):
        return ("ABORT", transaction_id)
    def commit_transaction( transaction_id ):
        return ("COMMIT", transaction_id)
    def update( transaction_id, tuple_id, val ):
        return (transaction_id, tuple_id, val)

# A Log is just a wrapper for a list of Records.
class Log:
    def __init__(self, records = None):
        self.records = records if records else []
    def __str__(self):
        return str(self.records)
    def __repr__(self):
        return str(self)
    def __eq__(self, other):
        return self.records == other.records
