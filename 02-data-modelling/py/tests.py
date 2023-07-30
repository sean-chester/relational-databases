# Test cases for ImplementMe class.
# The mocked objects (and therefore expected output) may change
# at the point of evaluation, including into a more complex object,  
# and the functionality tested by each test case may increase in difficulty.
# Your implementation should anticipate ways in which these mocks
# or tests could be more complex, as well as design mocks
# for some disclosed but not written test cases.

import unittest
import time
import timeout_decorator

from DataModelChecker import *
from DataTypes import *


# confirmSuperkey() simple case: check the primary key
class TestCase01(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        # with R(e,f,g,h) and f as primary key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        attributes = Attributes('R1', ['f'])
        expected_output = True

        self.assertEqual( expected_output, checker.confirmSuperkey( attributes ) )


# confirmSuperkey() sort of easy case: check a proper superset of the primary key
class TestCase02(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        # with R(e,f,g,h) and f as primary key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        attributes = Attributes('R2', ['g', 'f'])
        expected_output = True

        self.assertEqual( expected_output, checker.confirmSuperkey( attributes ) )


# confirmSuperkey() simple case: check a proper subset of the primary key
class TestCase03(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        # with R(e,f,g,h) and {f,g} as primary key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        attributes = Attributes('R3', ['g'])
        expected_output = False

        self.assertEqual( expected_output, checker.confirmSuperkey( attributes ) )



# confirmSuperkey() tougher case: check non-primary key unique attribute
class TestCase04(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        # with R(e,f,g,h) and f as primary key and g as unique
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        attributes = Attributes('R4', ['g'])
        expected_output = True

        self.assertEqual( expected_output, checker.confirmSuperkey( attributes ) )


# confirmSuperkey() tougher case
# Not provided in advance
class TestCase05(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        attributes = Attributes('', [])
        expected_output = True

        self.assertEqual( expected_output, checker.confirmSuperkey( attributes ) )


# confirmForeignKey() simple case: check single attribute referencing single other attribute
class TestCase06(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        # with R(x,y,z) and x as primary key
        # with S(v,w,x) and v as primary key and x as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R6', ['x'])
        referencing_attributes = Attributes('S6', ['x'])
        expected_output = True

        self.assertEqual( expected_output, checker.confirmForeignKey( referencing_attributes, referenced_attributes ) )


# confirmForeignKey() moderate case: check dual attribute referencing dual other attribute as weak entity set
class TestCase07(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        # with R(x,y,z) and {x,y} as primary key
        # with S(a,b,c) and {a,b,c} as primary key and {b,c} as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R7', ['x', 'y'])
        referencing_attributes = Attributes('S7', ['b', 'c'])
        expected_output = True

        self.assertEqual( expected_output, checker.confirmForeignKey( referencing_attributes, referenced_attributes ) )


# confirmForeignKey() simple case: size mismatch
class TestCase08(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        # with R(x,y,z) and {x,y} as primary key
        # with S(a,b,c) and a as primary key and b as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R8', ['x', 'y'])
        referencing_attributes = Attributes('S8', ['b'])
        expected_output = False

        self.assertEqual( expected_output, checker.confirmForeignKey( referencing_attributes, referenced_attributes ) )


# confirmForeignKey() moderate case: order mismatch on multi-attribute
class TestCase09(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        # with R(x,y,z) and {x,y} as primary key
        # with S(a,b,c) and a as primary key and {b,c} as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R9', ['x', 'y'])
        referencing_attributes = Attributes('S9', ['c', 'b'])
        expected_output = False

        self.assertEqual( expected_output, checker.confirmForeignKey( referencing_attributes, referenced_attributes ) )


# confirmForeignKey() tough case
# Not provided in advance
class TestCase10(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('' [])
        referencing_attributes = Attributes('', [])
        expected_output = True

        self.assertEqual( expected_output, checker.confirmForeignKey( referencing_attributes, referenced_attributes ) )

# confirmReferentialIntegrity(): reject case on delete
class TestCase11(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        # with R(x,y,z) and x as primary key
        # with S(a,b,c) and a as primary key and c as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R11', ['x'])
        referencing_attributes = Attributes('S11', ['c'])
        policy = RefIntegrityPolicy('DELETE', 'REJECT')
        expected_output = True

        self.assertEqual( expected_output, checker.confirmReferentialIntegrity( referencing_attributes, referenced_attributes, policy ) )


# confirmReferentialIntegrity(): cascade case on delete
class TestCase12(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        # with R(x,y,z) and x as primary key
        # with S(a,b,c) and a as primary key and c as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R12', ['x'])
        referencing_attributes = Attributes('S12', ['c'])
        policy = RefIntegrityPolicy('DELETE', 'CASCADE')
        expected_output = True

        self.assertEqual( expected_output, checker.confirmReferentialIntegrity( referencing_attributes, referenced_attributes, policy ) )


# confirmReferentialIntegrity(): reject case on update
class TestCase13(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        # with R(x,y,z) and x as primary key
        # with S(a,b,c) and a as primary key and c as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R13', ['x'])
        referencing_attributes = Attributes('S13', ['c'])
        policy = RefIntegrityPolicy('UPDATE', 'REJECT')
        expected_output = True

        self.assertEqual( expected_output, checker.confirmReferentialIntegrity( referencing_attributes, referenced_attributes, policy ) )


# confirmReferentialIntegrity(): cascade case on update
class TestCase14(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        # with R(x,y,z) and x as primary key
        # with S(a,b,c) and a as primary key and c as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R14', ['x'])
        referencing_attributes = Attributes('S14', ['c'])
        policy = RefIntegrityPolicy('UPDATE', 'CASCADE')
        expected_output = True

        self.assertEqual( expected_output, checker.confirmReferentialIntegrity( referencing_attributes, referenced_attributes, policy ) )



# confirmReferentialIntegrity(): set null case on delete
class TestCase15(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        # with R(x,y,z) and x as primary key
        # with S(a,b,c) and a as primary key and c as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R15', ['x'])
        referencing_attributes = Attributes('S15', ['c'])
        policy = RefIntegrityPolicy('DELETE', 'SET NULL')
        expected_output = True

        self.assertEqual( expected_output, checker.confirmReferentialIntegrity( referencing_attributes, referenced_attributes, policy ) )

# confirmFunctionalDependency(): easy case, PK and other attribute in same table
class TestCase16(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        # with R(x,y,z) and x as primary key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        determined_attributes = Attributes('R16', ['z'])
        determining_attributes = Attributes('R16', ['x'])
        expected_output = True

        self.assertEqual( expected_output, checker.confirmFunctionalDependency( determining_attributes, determined_attributes ) )


# confirmFunctionalDependency(): easy case
# Not provided in advance
class TestCase17(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        determined_attributes = Attributes('', [])
        determining_attributes = Attributes('', [])
        expected_output = True

        self.assertEqual( expected_output, checker.confirmFunctionalDependency( determining_attributes, determined_attributes ) )


# confirmFunctionalDependency(): moderate case, PK and attribute in other relation with FK relationship
class TestCase18(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        # with R(x,y,z) and x as primary key
        # with S(a,b,c) and a as primary key and c as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        determined_attributes = Attributes('R18', ['z'])
        determining_attributes = Attributes('S18', ['a'])
        expected_output = True

        self.assertEqual( expected_output, checker.confirmFunctionalDependency( determining_attributes, determined_attributes ) )


# confirmFunctionalDependency(): difficult case
# Not provided in advance
class TestCase19(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        determined_attributes = Attributes('', [])
        determining_attributes = Attributes('', [])
        expected_output = True

        self.assertEqual( expected_output, checker.confirmFunctionalDependency( determining_attributes, determined_attributes ) )


# confirmFunctionalDependency(): very difficult case
# Not provided in advance
class TestCase20(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        determined_attributes = Attributes('', [])
        determining_attributes = Attributes('', [])
        expected_output = True

        self.assertEqual( expected_output, checker.confirmFunctionalDependency( determining_attributes, determined_attributes ) )

# Flip database schema for all unit tests for True/False neutrality




# confirmSuperkey() simple case: check the primary key
class TestCase01Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_superkey(self):

        # with R(a,b,c,d) and a as primary key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        attributes = Attributes('R1N', ['b'])
        expected_output = False

        self.assertEqual( expected_output, checker.confirmSuperkey( attributes ) )


# confirmSuperkey() sort of easy case: check a proper superset of the primary key
class TestCase02Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_superkey(self):

        # with R(a,b,c,d) and a as primary key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        attributes = Attributes('R2N', ['b', 'c'])
        expected_output = False

        self.assertEqual( expected_output, checker.confirmSuperkey( attributes ) )


# confirmSuperkey() simple case: check a proper subset of the primary key
class TestCase03Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_superkey(self):

        # with R(e,f,g,h) and {f,g} as primary key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        attributes = Attributes('R3N', ['f', 'g'])
        expected_output = True

        self.assertEqual( expected_output, checker.confirmSuperkey( attributes ) )



# confirmSuperkey() tougher case: check non-primary key unique attribute
class TestCase04Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_superkey(self):

        # with R(e,f,g,h) and f as primary key and e as unique
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        attributes = Attributes('R4N', ['g'])
        expected_output = False

        self.assertEqual( expected_output, checker.confirmSuperkey( attributes ) )


# confirmSuperkey() tougher case
# Not provided in advance
class TestCase05Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        attributes = Attributes('', [])
        expected_output = False

        self.assertEqual( expected_output, checker.confirmSuperkey( attributes ) )


# confirmForeignKey() simple case: check single attribute referencing single other attribute
class TestCase06Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_foreignkey(self):

        # with R(x,y,z) and x as primary key
        # with S(v,w,x) and v as primary key and x as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R6N', ['y'])
        referencing_attributes = Attributes('S6N', ['x'])
        expected_output = False

        self.assertEqual( expected_output, checker.confirmForeignKey( referencing_attributes, referenced_attributes ) )


# confirmForeignKey() moderate case: check dual attribute referencing dual other attribute as weak entity set
class TestCase07Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_foreignkey(self):

        # with R(x,y,z) and {x,y} as primary key
        # with S(a,b,c) and {a,b,c} as primary key and {b,c} as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R7N', ['x', 'y'])
        referencing_attributes = Attributes('S7N', ['a', 'b'])
        expected_output = False

        self.assertEqual( expected_output, checker.confirmForeignKey( referencing_attributes, referenced_attributes ) )


# confirmForeignKey() simple case: size mismatch
class TestCase08Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_foreignkey(self):

        # with R(x,y,z) and {x,y} as primary key
        # with S(a,b,c) and a as primary key and b as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R8N', ['x'])
        referencing_attributes = Attributes('S8N', ['b'])
        expected_output = True

        self.assertEqual( expected_output, checker.confirmForeignKey( referencing_attributes, referenced_attributes ) )


# confirmForeignKey() moderate case: order mismatch on multi-attribute
class TestCase09Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_foreignkey(self):

        # with R(x,y,z) and {x,y} as primary key
        # with S(a,b,c) and a as primary key and {b,c} as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R9N', ['y', 'x'])
        referencing_attributes = Attributes('S9N', ['c', 'b'])
        expected_output = True

        self.assertEqual( expected_output, checker.confirmForeignKey( referencing_attributes, referenced_attributes ) )


# confirmForeignKey() tough case
# Not provided in advance
class TestCase10Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('' [])
        referencing_attributes = Attributes('', [])
        expected_output = False

        self.assertEqual( expected_output, checker.confirmForeignKey( referencing_attributes, referenced_attributes ) )


# confirmReferentialIntegrity(): reject case on delete
class TestCase11Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_refintegrity(self):

        # with R(x,y,z) and x as primary key
        # with S(a,b,c) and a as primary key and c as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R11N', ['x'])
        referencing_attributes = Attributes('S11N', ['c'])
        policy = RefIntegrityPolicy('DELETE', 'REJECT')
        expected_output = True

        self.assertEqual( expected_output, checker.confirmReferentialIntegrity( referencing_attributes, referenced_attributes, policy ) )


# confirmReferentialIntegrity(): cascade case on delete
class TestCase12Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_refintegrity(self):

        # with R(x,y,z) and x as primary key
        # with S(a,b,c) and a as primary key and c as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R12N', ['x'])
        referencing_attributes = Attributes('S12N', ['c'])
        policy = RefIntegrityPolicy('DELETE', 'CASCADE')
        expected_output = False

        self.assertEqual( expected_output, checker.confirmReferentialIntegrity( referencing_attributes, referenced_attributes, policy ) )


# confirmReferentialIntegrity(): reject case on update
class TestCase13Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_refintegrity(self):

        # with R(x,y,z) and x as primary key
        # with S(a,b,c) and a as primary key and c as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R13N', ['x'])
        referencing_attributes = Attributes('S13N', ['c'])
        policy = RefIntegrityPolicy('UPDATE', 'REJECT')
        expected_output = False

        self.assertEqual( expected_output, checker.confirmReferentialIntegrity( referencing_attributes, referenced_attributes, policy ) )


# confirmReferentialIntegrity(): cascade case on update
class TestCase14Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_refintegrity(self):

        # with R(x,y,z) and x as primary key
        # with S(a,b,c) and a as primary key and c as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R14N', ['x'])
        referencing_attributes = Attributes('S14N', ['c'])
        policy = RefIntegrityPolicy('UPDATE', 'CASCADE')
        expected_output = False

        self.assertEqual( expected_output, checker.confirmReferentialIntegrity( referencing_attributes, referenced_attributes, policy ) )



# confirmReferentialIntegrity(): set null case on delete
class TestCase15Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_refintegrity(self):

        # with R(x,y,z) and x as primary key
        # with S(a,b,c) and a as primary key and c as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        referenced_attributes = Attributes('R15N', ['x'])
        referencing_attributes = Attributes('S15N', ['c'])
        policy = RefIntegrityPolicy('DELETE', 'SET NULL')
        expected_output = False

        self.assertEqual( expected_output, checker.confirmReferentialIntegrity( referencing_attributes, referenced_attributes, policy ) )

# confirmFunctionalDependency(): easy case, PK and other attribute in same table
class TestCase16Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_funcdependency(self):

        # with R(x,y,z) and z as primary key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        determined_attributes = Attributes('R16N', ['z'])
        determining_attributes = Attributes('R16N', ['x'])
        expected_output = False

        self.assertEqual( expected_output, checker.confirmFunctionalDependency( determining_attributes, determined_attributes ) )


# confirmFunctionalDependency(): easy case
# Not provided in advance
class TestCase17Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        determined_attributes = Attributes('', [])
        determining_attributes = Attributes('', [])
        expected_output = False

        self.assertEqual( expected_output, checker.confirmFunctionalDependency( determining_attributes, determined_attributes ) )


# confirmFunctionalDependency(): moderate case, PK and attribute in other relation with FK relationship
class TestCase18Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_funcdependency(self):

        # with R(x,y,z) and x as primary key
        # with S(a,b,c) and a as primary key and c as foreign key
        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        determined_attributes = Attributes('R18N', ['a'])
        determining_attributes = Attributes('S18N', ['x'])
        expected_output = False

        self.assertEqual( expected_output, checker.confirmFunctionalDependency( determining_attributes, determined_attributes ) )


# confirmFunctionalDependency(): difficult case
# Not provided in advance
class TestCase19Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        determined_attributes = Attributes('', [])
        determining_attributes = Attributes('', [])
        expected_output = False

        self.assertEqual( expected_output, checker.confirmFunctionalDependency( determining_attributes, determined_attributes ) )


# confirmFunctionalDependency(): very difficult case
# Not provided in advance
class TestCase20Negated(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_insertion(self):

        checker = DataModelChecker('localhost', 'student', 'stud3nt', 'assignment2')

        determined_attributes = Attributes('', [])
        determining_attributes = Attributes('', [])
        expected_output = False

        self.assertEqual( expected_output, checker.confirmFunctionalDependency( determining_attributes, determined_attributes ) )

# Run all unit tests above.
unittest.main(argv=[''],verbosity=2, exit=False)
