from erd import *

# This function calculates a range for combinations of two sets of attributes
# in an entity-relationship diagram (ERD).
# 
# Considering the cardinality constraints imposed by the ERD, this
# function determines how many different values from the set source_attributes
# can combine with values from destination_attributes.
# For example, if entity set A and entity set B are connected
# via a one-to-many relationship, R, with non-optional participation, then
# this function would return:
#   * (1,n) if source contained all attributes of B & dest, all of A
#   * (1,1) if source contained all attributes of A & dest, all of B
#
# @TODO: Implement me!
def calculate_bounds( erd, source_attributes, destination_attributes ):
    bounds = (0,0)
    return bounds
