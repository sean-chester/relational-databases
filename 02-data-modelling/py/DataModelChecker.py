from DataTypes import *


# Bundles together functions for probing a MySQL database to confirm
# whether or not it adheres to specific properties of a logical/relational schema.
# Can be used to verify that a MySQL database correctly implements a design.
class DataModelChecker:

    # Ctor sets the connection details for this model checker
    def __init__( self, host, username, password, database ):
        # TODO: Implement me!

    # Predicate function that connects to the database and confirms
    # whether or not a list of attributes is set up as a (super)key for a given table
    # For example, if attributes contains table_name R and attributes [x, y],
    # this function returns true if (x,y) is enforced as a key in R
    # @see Util.Attributes
    # @pre the tables and attributes in attributes must already exist
    def confirmSuperkey( self, attributes ):
        # TODO: Implement me!
        return true

    # Predicate function that connects to the database and confirms
    # whether or not `referencing_attributes` is set up as a foreign
    # key that reference `referenced_attributes`
    # For example, if referencing_attributes contains table_name R and attributes [x, y]
    # and referenced_attributes contains table_name S and attributes [a, b]
    # this function returns true if (x,y) is enforced as a foreign key that references
    # (a,b) in R
    # @see Util.Attributes
    # @pre the tables and attributes in referencing_attributes and referenced_attributes must already exist
    def confirmForeignKey( self, referencing_attributes, referenced_attributes ):
        # TODO: Implement me!
        return true

    # Predicate function that connects to the database and confirms
    # whether or not `referencing_attributes` is set up as a foreign key
    # that reference `referenced_attributes` using a specific referential integrity `policy`
    # For example, if referencing_attributes contains table_name R and attributes [x, y]
    # and referenced_attributes contains table_name S and attributes [a, b]
    # this function returns true if (x,y) the provided policy is used to manage that foreign key
    # @see Util.Attributes, Util.RefIntegrityPolicy
    # @pre The foreign key is valid
    # @pre policy must be a valid Util.RefIntegrityPolicy
    def confirmReferentialIntegrity( self, referencing_attributes, referenced_attributes, policy ):
        # TODO: Implement me!
        return true

    # Predicate function that connects to the database and confirms
    # whether or not `referencing_attributes` is set up in such as way as to
    # functionally determine `referenced_attributes`
    # For example, if referencing_attributes contains table_name R and attributes [x, y]
    # and referenced_attributes contains table_name S and attributes [a, b]
    # this function returns true if (x,y) is enforced to functionally determine (a,b) in R
    # @see Util.Attributes
    # @pre the tables and attributes in referencing_attributes and referenced_attributes must already exist
    def confirmFunctionalDependency( self, referencing_attributes, referenced_attributes ):
        # TODO: Implement me!
        return true

    # Predicate function that connects to the database and confirms
    # whether or not any tuples in a given table are permitted to violate
    # a constraint expressed as a SQL snippet.
    # For example, given `R` and `x >= 0`, this function would return
    # true if it is not possible to add tuples to `R` with negative `x` values.
    # @pre sql_predicate must be valid SQL syntax that can be used as is in a WHERE condition
    # @pre table_name must exist in the database already
    def confirmArbitraryConstraint( self, table_name, sql_predicate ):
        # TODO: Implement me!
        return true


