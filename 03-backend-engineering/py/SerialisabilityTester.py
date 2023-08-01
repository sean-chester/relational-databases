# Methods for checking whether an execution schedule is serialisable.

from Schedule import *


# Takes as input a Schedule of IOOperations and returns the lexicographically
# smallest serial SimpleSchedule that is conflict-equivalent to it. If the provided
# schedule is not conflict-serialisable, then this methods returns None (i.e., the python
# built-in type that represents a null value) 
def to_serial( schedule = Schedule() ):

    # Implement me!
    return SimpleSchedule()
