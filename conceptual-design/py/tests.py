from erd import *
from table import *
from erd_converter import convert_to_table

import unittest

def wrap_student_call( func, input ) :
    actual_result = func( input )

    Table.__eq__ = lambda self,other : self.name == other.name and \
        self.attributes == other.attributes and \
        self.primary_key == other.primary_key and \
        self.foreign_keys== other.foreign_keys
    Database.__eq__ = lambda self,other : set( self.tables ) == set( other.tables )

    return actual_result



# Check that the `__eq__` function works correctly on the sample table
# Not included in assignment test cases
class TestEquality(unittest.TestCase):
	def test_equal_db(self):
		sample_db2 = Database([ \
			Table('A', set(['a1','a2']), set(['a1']), set()), \
			Table('B', set(['b1','b2']), set(['b1']), set()), \
			Table('R1', set(['a1','b1', 'x']), set(['a1','b1']), \
				set([(('a1',), 'A', ('a1',)), (('b1',), 'B', ('b1',))]))])
		self.assertEqual( sample_db, sample_db2 )


# Single entity set with a single attribute which is the PK
class TestCase1(unittest.TestCase):
	def test_converter(self):
		erd1 = ERD( \
            [], \
            [EntitySet('A', ['a1'], ['a1'], [], [], [])])

		db1 = Database([ \
			Table('A', set(['a1']), set(['a1']), set())])

		self.assertEqual( db1, wrap_student_call( convert_to_table, erd1 ) )


# Single entity set with two attributes, which are both part of the PK
class TestCase2(unittest.TestCase):
    def test_converter(self):
        erd2 = ERD( \
            [], \
            [EntitySet('A', ['a1', 'a2'], ['a1', 'a2'], [], [], [])])

        db2 = Database([ \
            Table('A', set(['a1', 'a2']), set(['a1', 'a2']), set())])

        self.assertEqual( db2, wrap_student_call( convert_to_table, erd2 ) )


# Single entity set with two attributes, in which only one is part of the PK
class TestCase3(unittest.TestCase):
	def test_converter(self):
		erd3 = ERD( \
            [], \
            [EntitySet('A', ['a1', 'a2'], ['a1'], [], [], [])])

		# Not provided
		db3 = Database([])

		self.assertEqual( db3, wrap_student_call( convert_to_table, erd3 ) )


# Two entity sets, each with two attributes, one of which is the PK attribute.
# Also a many-many relationship between them with no attributes
class TestCase4(unittest.TestCase):
	def test_converter(self):
		erd4 = ERD( \
            [Relationship('ShopsAt',[],[])], \
            [EntitySet('Customer', ['customer_id', 'customer_name'], ['customer_id'], [('ShopsAt', Multiplicity.MANY)], [], []), \
            EntitySet('Store', ['store_id', 'store_name'], ['store_id'], [('ShopsAt', Multiplicity.MANY)], [], [])])

		db4 = Database([ \
			Table('Customer', set(['customer_id','customer_name']), set(['customer_id']), set()), \
			Table('Store', set(['store_id','store_name']), set(['store_id']), set()), \
			Table('ShopsAt', set(['customer_id','store_id']), set(['customer_id','store_id']), \
                set([(('customer_id',), 'Customer', ('customer_id',)), (('store_id',), 'Store', ('store_id',))]))])

		self.assertEqual( db4, wrap_student_call( convert_to_table, erd4 ) )


# Two entity sets, each with two attributes, one of which is the PK attribute.
# Also a many-many relationship between them with one PK attribute.
class TestCase5(unittest.TestCase):
    def test_converter(self):
        erd5 = ERD( \
            [Relationship('ShopsAt',['date'],['date'])], \
            [EntitySet('Customer', ['customer_id', 'customer_name'], ['customer_id'], [('ShopsAt', Multiplicity.MANY)], [], []), \
            EntitySet('Store', ['store_id', 'store_name'], ['store_id'], [('ShopsAt', Multiplicity.MANY)], [], [])])

        db5 = Database([ \
            Table('Customer', set(['customer_id','customer_name']), set(['customer_id']), set()), \
            Table('Store', set(['store_id','store_name']), set(['store_id']), set()), \
            Table('ShopsAt', set(['customer_id','store_id', 'date']), set(['customer_id','store_id', 'date']), \
                set([(('customer_id',), 'Customer', ('customer_id',)), (('store_id',), 'Store', ('store_id',))]))])

        self.assertEqual( db5, wrap_student_call(convert_to_table, erd5 ) )


# Two entity sets, each with two attributes, one of which is the PK attribute.
# Also a many-many relationship between them with one PK attribute and one non-PK attribute
class TestCase6(unittest.TestCase):
    def test_converter(self):
        erd6 = ERD( \
            [Relationship('ShopsAt',['date', 'purchase_amount'],['date'])], \
            [EntitySet('Customer', ['customer_id', 'customer_name'], ['customer_id'], [('ShopsAt', Multiplicity.MANY)], [], []), \
            EntitySet('Store', ['store_id', 'store_name'], ['store_id'], [('ShopsAt', Multiplicity.MANY)], [], [])])

        # Not provided
        db6 = Database([])

        self.assertEqual( db6, wrap_student_call(convert_to_table, erd6 ) )


# Two entity sets, each with two attributes, one of which is the PK attribute.
# Also a one-many or many-one relationship between them with no attributes
class TestCase7(unittest.TestCase):
    def test_converter(self):
        erd7 = ERD( \
            [Relationship('Prefers',[],[])], \
            [EntitySet('Customer', ['customer_id', 'customer_name'], ['customer_id'], [('Prefers', Multiplicity.MANY)], [], []), \
            EntitySet('Store', ['store_id', 'store_name'], ['store_id'], [('Prefers', Multiplicity.ONE)], [], [])])

        # Not provided
        db7 = Database([])

        self.assertEqual( db7, wrap_student_call( convert_to_table, erd7 ) )


# Two entity sets, each with two attributes, one of which is the PK attribute.
# Also a one-many or many-one relationship between them with one PK attribute
class TestCase8(unittest.TestCase):
    def test_converter(self):
        erd8 = ERD( \
            [Relationship('Prefers',['since'],['since'])], \
            [EntitySet('Customer', ['customer_id', 'customer_name'], ['customer_id'], [('Prefers', Multiplicity.MANY)], [], []), \
            EntitySet('Store', ['store_id', 'store_name'], ['store_id'], [('Prefers', Multiplicity.ONE)], [], [])])

        # Not provided
        db8 = Database([])

        self.assertEqual( db8, wrap_student_call( convert_to_table, erd8 ) )


# Two entity sets, one of which is designated as a parent of the other.
class TestCase9(unittest.TestCase):
    def test_converter(self):
        erd9 = ERD( \
            [Relationship('ManagerIsAnEmployee',[],[])], \
            [EntitySet('Employee', ['employee_id', 'employee_name'], ['employee_id'], [('ManagerIsAnEmployee', Multiplicity.ONE)], [], []), \
            EntitySet('Manager', [], [], [], ['Employee'], [])])

        db9 = Database([ \
            Table('Employee', set(['employee_id','employee_name']), set(['employee_id']), set()), \
            Table('Manager', set(['employee_id']), set(['employee_id']), \
                set([(('employee_id',), 'Employee', ('employee_id',))]))])

        self.assertEqual( db9, wrap_student_call(convert_to_table, erd9 ) )


# Two entity sets, each with two attributes, one of which is the PK attribute.
# Also a one-many relationship between them is designated in the supporting_relationship list
# instead of the relationship list for one of the tables (the weak entity set).
class TestCase10(unittest.TestCase):
    def test_converter(self):
        erd10 = ERD( \
            [Relationship('FoundIn',[],[])], \
            [EntitySet('Building', ['building_id', 'building_name'], ['building_id'], [('FoundIn', Multiplicity.ONE)], [], []), \
            EntitySet('Room', ['room_number', 'max_capacity'], ['room_number'], [], [], ['FoundIn'])])

        # Not provided
        db10 = Database([])

        self.assertEqual( db10, wrap_student_call(convert_to_table, erd10 ) )


# Two entity sets, each with two attributes, both of which are PK attributes for one E.S.
# Also a many-many relationship between them with no attributes
class TestCase11(unittest.TestCase):
    def test_converter(self):
        erd11 = ERD( \
            [Relationship('R',[],[])], \
            [EntitySet('A', ['a1', 'a2'], ['a1',], [('R', Multiplicity.MANY)], [], []), \
            EntitySet('B', ['b1', 'b2'], ['b1', 'b2'], [('R', Multiplicity.MANY)], [], [])])

        db11a = Database([ \
            Table('A', set(['a1','a2']), set(['a1',]), set()), \
            Table('B', set(['b1','b2']), set(['b1', 'b2']), set()), \
            Table('R', set(['a1', 'b1', 'b2']), set(['a1', 'b1', 'b2']), \
                set([(('a1',), 'A', ('a1',)), (('b1','b2'), 'B', ('b1','b2'))]))])

        db11b = Database([ \
            Table('A', set(['a1','a2']), set(['a1',]), set()), \
            Table('B', set(['b1','b2']), set(['b1', 'b2']), set()), \
            Table('R', set(['a1', 'b1', 'b2']), set(['a1', 'b1', 'b2']), \
                set([(('a1',), 'A', ('a1',)), (('b2','b1'), 'B', ('b2','b1'))]))])

        actual_result = wrap_student_call(convert_to_table, erd11 )
        self.assertTrue( ( db11a == actual_result ) or ( db11b == actual_result ), "Matches one of two valid orderings")


# Two entity sets, each with two attributes, both of which are PK attributes for both E.S.
# Also a many-many relationship between them with no attributes
class TestCase12(unittest.TestCase):
    def test_converter(self):
        erd12 = ERD( \
            [Relationship('R',[],[])], \
            [EntitySet('A', ['a1', 'a2'], ['a1','a2'], [('R', Multiplicity.MANY)], [], []), \
            EntitySet('B', ['b1', 'b2'], ['b1', 'b2'], [('R', Multiplicity.MANY)], [], [])])

        db12a = Database([ \
            Table('A', set(['a1','a2']), set(['a1','a2']), set()), \
            Table('B', set(['b1','b2']), set(['b1', 'b2']), set()), \
            Table('R', set(['a1', 'b1', 'b2']), set(['a1', 'b1', 'b2']), \
                set([(('a1','a2'), 'A', ('a1','a2')), (('b1','b2'), 'B', ('b1','b2'))]))])

        db12b = Database([ \
            Table('A', set(['a1','a2']), set(['a1','a2']), set()), \
            Table('B', set(['b1','b2']), set(['b1', 'b2']), set()), \
            Table('R', set(['a1', 'b1', 'b2']), set(['a1', 'b1', 'b2']), \
                set([(('a1','a2'), 'A', ('a1','a2')), (('b2','b1'), 'B', ('b2','b1'))]))])

        db12c = Database([ \
            Table('A', set(['a1','a2']), set(['a1','a2']), set()), \
            Table('B', set(['b1','b2']), set(['b1', 'b2']), set()), \
            Table('R', set(['a1', 'b1', 'b2']), set(['a1', 'b1', 'b2']), \
                set([(('a2', 'a1'), 'A', ('a2', 'a1')), (('b1','b2'), 'B', ('b1','b2'))]))])

        db12d = Database([ \
            Table('A', set(['a1','a2']), set(['a1','a2']), set()), \
            Table('B', set(['b1','b2']), set(['b1', 'b2']), set()), \
            Table('R', set(['a1', 'b1', 'b2']), set(['a1', 'b1', 'b2']), \
                set([(('a2','a1'), 'A', ('a2','a1')), (('b2','b1'), 'B', ('b2','b1'))]))])

        actual_result = wrap_student_call(convert_to_table, erd12 )
        self.assertTrue( ( db12a == actual_result ) or ( db12b == actual_result ) \
            or ( db12c == actual_result ) or ( db12d == actual_result ), "Matches one of four valid orderings")


# ERD-to-DB worksheet, Q1
# many-one relationship with compound foreign key
class TestCase13(unittest.TestCase):
    def test_converter(self):
        erd13 = ERD( \
            [Relationship('Contains',[],[])], \
            [EntitySet('Room', ['room_name', 'floor'], ['room_name',], [('Contains', Multiplicity.MANY)], [], []), \
            EntitySet('Building', ['latitude', 'longitude', 'building_name'], ['latitude', 'longitude'], \
                [('Contains', Multiplicity.ONE)], [], [])])

        db13a = Database([ \
            Table('Building', set(['latitude','longitude','building_name']), set(['latitude','longitude']), set()), \
            Table('Room', set(['room_name', 'floor', 'latitude', 'longitude']), set(['room_name',]), \
                set([(('latitude','longitude'), 'Building', ('latitude','longitude'))]))])

        db13b = Database([ \
            Table('Building', set(['latitude','longitude','building_name']), set(['latitude','longitude']), set()), \
            Table('Room', set(['room_name', 'floor', 'latitude', 'longitude']), set(['room_name',]), \
                set([(('longitude','latitude'), 'Building', ('longitude','latitude'))]))])

        actual_result = wrap_student_call(convert_to_table, erd13 )
        self.assertTrue( ( db13a == actual_result ) or ( db13b == actual_result ), "Matches one of two valid orderings")


# ERD-to-DB worksheet, question 2
# many-many relationship with PK and one multi-attribute FK
class TestCase14(unittest.TestCase):
    def test_converter(self):
        erd14 = ERD( \
            [Relationship('PlaysFor',['start_date','end_date'],['start_date',])], \
            [EntitySet('Player', ['player_id', 'player_name'], ['player_id',], [('PlaysFor', Multiplicity.MANY)], [], []), \
            EntitySet('Team', ['team_name', 'city', 'league'], ['team_name', 'city'], \
                [('PlaysFor', Multiplicity.MANY)], [], [])])

        db14a = Database([ \
            Table('Player', set(['player_id','player_name']), set(['player_id',]), set()), \
            Table('Team', set(['city','team_name']), set(['city','team_name']), set()), \
            Table('PlaysFor', set(['start_date', 'end_date', 'player_id', 'city', 'team_name']), \
                set(['player_id','city','team_name','start_date']), \
                set([(('player_id',), 'Player', ('player_id',)),\
                    (('city','team_name'), 'Team', ('city','team_name'))]))])

        db14b = Database([ \
            Table('Player', set(['player_id','player_name']), set(['player_id',]), set()), \
            Table('Team', set(['city','team_name']), set(['city','team_name']), set()), \
            Table('PlaysFor', set(['start_date', 'end_date', 'player_id', 'city', 'team_name']), \
                set(['player_id','city','team_name','start_date']), \
                set([(('player_id',), 'Player', ('player_id',)),\
                    (('team_name','city'), 'Team', ('team_name','city'))]))])

        actual_result = wrap_student_call(convert_to_table, erd14 )
        self.assertTrue( ( db14a == actual_result ) or ( db14b == actual_result ), "Matches one of two valid orderings")


# Not provided
class TestCase15(unittest.TestCase):
    def test_converter(self):
        erd15 = ERD( \
            [], \
            [])

        # Not provided
        db15 = Database([])

        self.assertEqual( db15, wrap_student_call(convert_to_table, erd15 ) )


# Not provided
class TestCase16(unittest.TestCase):
    def test_converter(self):
        erd16 = ERD( \
            [], \
            [])

        # Not provided
        db16 = Database([])

        self.assertEqual( db16, wrap_student_call( convert_to_table, erd16 ) )


# Not provided
class TestCase17(unittest.TestCase):
    def test_converter(self):
        erd17 = ERD( \
            [], \
            [])

        # Not provided
        db17 = Database([])

        self.assertEqual( db17, wrap_student_call( convert_to_table, erd17 ) )


# A ternary relationship is provided.
# Multiplicity of many-one-one
class TestCase18(unittest.TestCase):
    def test_converter(self):
        erd18 = ERD( \
            [Relationship('Rel',[],[])], \
            [EntitySet('R', ['a1', 'a2'], ['a1',], [('Rel', Multiplicity.MANY)], [], []), \
            EntitySet('S', ['b1', 'b2'], ['b2',], [('Rel', Multiplicity.ONE)], [], []), \
            EntitySet('T', ['c1', 'c2'], ['c1',], [('Rel', Multiplicity.ONE)], [], [])])

        # Not provided
        db18 = Database([ \
            Table('R', set(['a1','a2','b2','c1']), set(['a1',]), \
                set([(('b2',), 'S', ('b2',)), (('c1',), 'T', ('c1',))])), \
            Table('S', set(['b1','b2']), set(['b2',]), set()), \
            Table('T', set(['c1','c2']), set(['c1',]), set())])

        self.assertEqual( db18, wrap_student_call(convert_to_table, erd18 ) )



# An entity set inherits from a subclass
class TestCase19(unittest.TestCase):
    def test_converter(self):
        erd19 = ERD( \
            [Relationship('LabIsACourse',[],[]), \
            Relationship('VirtualIsALab',[],[])], \
            [EntitySet('Course', ['crn', 'section'], ['crn',], [('LabIsACourse', Multiplicity.ONE)], [], []), \
            EntitySet('Lab', [], [], [('VirtualIsALab', Multiplicity.ONE)], ['LabIsACourse'], []), \
            EntitySet('Virtual', [], [], [], ['VirtualIsALab'], [])])

        db19 = Database([ \
            Table('Course', set(['crn','section']), set(['crn',]), set()), \
            Table('Lab', set(['crn',]), set(['crn',]), set([(('crn',), 'Course', ('crn',))])), \
            Table('Virtual', set(['crn',]), set(['crn',]), set([(('crn',), 'Lab', ('crn',))]))])


# An entity set inherits from a subclass with a two-attribute PK
class TestCase20(unittest.TestCase):
    def test_converter(self):
        erd20 = ERD( \
            [Relationship('LabIsACourse',[],[]), \
            Relationship('VirtualIsALab',[],[])], \
            [EntitySet('Course', ['course_code', 'semester'], ['course_code','semester'], \
                [('LabIsACourse', Multiplicity.ONE)], [], []), \
            EntitySet('Lab', ['TA'], [], [('VirtualIsALab', Multiplicity.ONE)], ['LabIsACourse'], []), \
            EntitySet('Virtual', ['zoom_link'], [], [], ['VirtualIsALab'], [])])

        db20a = Database([ \
            Table('Course', set(['course_code','semester']), set(['course_code','semester']), set()), \
            Table('Lab', set(['course_code','semester','TA']), set(['course_code','semester']), \
                set([(('course_code','semester'), 'Course', ('course_code','semester'))])), \
            Table('Virtual', set(['course_code','semester','zoom_link']), set(['course_code','semester']), \
                set([(('course_code','semester'), 'Lab', ('course_code','semester'))]))])

        db20b = Database([ \
            Table('Course', set(['course_code','semester']), set(['course_code','semester']), set()), \
            Table('Lab', set(['course_code','semester','TA']), set(['course_code','semester']), \
                set([(('course_code','semester'), 'Course', ('course_code','semester'))])), \
            Table('Virtual', set(['course_code','semester','zoom_link']), set(['course_code','semester']), \
                set([(('semester','course_code'), 'Lab', ('semester','course_code'))]))])

        db20c = Database([ \
            Table('Course', set(['course_code','semester']), set(['course_code','semester']), set()), \
            Table('Lab', set(['course_code','semester','TA']), set(['course_code','semester']), \
                set([(('semester','course_code'), 'Course', ('semester','course_code'))])), \
            Table('Virtual', set(['course_code','semester','zoom_link']), set(['course_code','semester']), \
                set([(('course_code','semester'), 'Lab', ('course_code','semester'))]))])

        db20d = Database([ \
            Table('Course', set(['course_code','semester']), set(['course_code','semester']), set()), \
            Table('Lab', set(['course_code','semester','TA']), set(['course_code','semester']), \
                set([(('semester','course_code'), 'Course', ('semester','course_code'))])), \
            Table('Virtual', set(['course_code','semester','zoom_link']), set(['course_code','semester']), \
                set([(('semester','course_code'), 'Lab', ('semester','course_code'))]))])

        actual_result = wrap_student_call(convert_to_table, erd20 )
        self.assertTrue( db20a == actual_result or db20b == actual_result or db20c == actual_result or db20d == actual_result, \
        "actual result matches one of four possible correct orderings" )


# A weak entity set is supported by a weak entity set,
# at least one of which is involved in a non-supporting relationship.
class TestCaseB1(unittest.TestCase):
    def test_converter(self):
        erdB1 = ERD( \
            [Relationship('FoundIn',[],[]), \
            Relationship('PlacedIn',[],[]), \
            Relationship('HeldIn',[],[])], \
            [EntitySet('Building', ['building_id', 'building_name'], ['building_id'], [('FoundIn', Multiplicity.ONE)], [], []), \
            EntitySet('Room', ['room_id', 'max_capacity'], ['room_id'], [('PlacedIn', Multiplicity.ONE), ('HeldIn', Multiplicity.ONE)], [], ['FoundIn']), \
            EntitySet('Desk', ['desk_id'], ['desk_id'], [], [], ['PlacedIn']), \
            EntitySet('Class', ['crn'], ['crn'], [('HeldIn', Multiplicity.MANY)], [], [])])

        # Not provided
        dbB1 = Database([])

        self.assertEqual( dbB1, wrap_student_call(convert_to_table, erdB1 ) )


# ERD-to-DB worksheet question 3 (simplified)
# Multiplicity of many-many-one.
class TestCaseB2(unittest.TestCase):
    def test_converter(self):
        erdB2 = ERD( \
            [Relationship('Rel',[],[])], \
            [EntitySet('R', ['a1', 'a2'], ['a1',], [('Rel', Multiplicity.MANY)], [], []), \
            EntitySet('S', ['b1', 'b2'], ['b2',], [('Rel', Multiplicity.MANY)], [], []), \
            EntitySet('T', ['c1', 'c2'], ['c1',], [('Rel', Multiplicity.ONE)], [], [])])

        # Not provided
        dbB2 = Database([ \
            Table('R', set(['a1','a2']), set(['a1',]), set()), \
            Table('S', set(['b1','b2']), set(['b2',]), set()), \
            Table('T', set(['c1','c2']), set(['c1',]), set()), \
            Table('Rel', set(['a1','b2','c1']), set(['a1','b2']), \
                set([(('a1',), 'R', ('a1',)), (('b2',), 'S', ('b2',)), (('c1',), 'T', ('c1',))]))])

        self.assertEqual( dbB2, wrap_student_call(convert_to_table, erdB2 ) )






# Run all unit tests above.
unittest.main(argv=[''],verbosity=2, exit=False)
