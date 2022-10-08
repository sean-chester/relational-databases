# Test cases for calculate_bounds() method.
#
# Not all test cases have been provided; part of this assignment
# is to write a good test suite for the problem.
# However, pre-grading will be performed on the final set of
# test cases; so, it is possible to know in advance whether
# your test coverage matches ours.
# The final evaluation will contain twenty test cases.
#
# Most test cases will be modified slightly to prevent
# hard-coding; e.g., a (0,1) could be changed to a (1,inf)

from erd import *
from cardinalities_bounds import calculate_bounds

import unittest


# Two entity sets in a one-to-many or many-to-one relationship.
class TestCase01(unittest.TestCase):
    def test_converter(self):
        erd = ERD()
        erd.add_entity_set("A")
        erd.add_attribute("a")
        erd.add_entity_set("B")
        erd.add_attribute("b")
        erd.add_relationship("R")
        erd.connect("A", "R", 0, math.inf)
        erd.connect("B", "R", 1, 1)
        erd.attach('a', "A")
        erd.attach('b', "B")
        erd.add_identifier('A', ['a'])
        erd.add_identifier('B', ['b'])

        expected_bounds = (0,math.inf)

        self.assertEqual( expected_bounds, calculate_bounds( erd, ["a"], ["b"] ) )



# Two entity sets in a one-to-one relationship but also connected via a superclass.
class TestCase02(unittest.TestCase):
    def test_converter(self):
        erd = ERD()
        erd.add_entity_set("A")
        erd.add_attribute("a")
        erd.add_entity_set("B")
        erd.add_attribute("b")
        erd.add_relationship("R")
        erd.connect("A", "R", 1, 1)
        erd.connect("B", "R", 1, 1)
        erd.attach('a', "A")
        erd.attach('b', "B")
        erd.add_generalisation("C", ["A","B"], "(t,e)")
        erd.add_attribute("c")
        erd.attach('c', "C")
        erd.add_identifier("C", ["c"])

        expected_bounds = (1,math.inf)

        self.assertEqual( expected_bounds, calculate_bounds( erd, ["a"], ["b"] ) )



# Three entity sets are connected in series.
class TestCase03(unittest.TestCase):
    def test_converter(self):
        erd = ERD()
        erd.add_entity_set("A")
        erd.add_attribute("a")
        erd.add_entity_set("B")
        erd.add_attribute("b")
        erd.add_entity_set("C")
        erd.add_attribute("c")
        erd.add_relationship("R1")
        erd.add_relationship("R2")
        erd.connect("A", "R1", 1, math.inf)
        erd.connect("B", "R1", 0, 1)
        erd.connect("B", "R2", 0, 1)
        erd.connect("C", "R2", 1, 1)
        erd.attach('a', "A")
        erd.attach('b', "B")
        erd.attach('c', "C")
        erd.add_identifier('A', ['a'])
        erd.add_identifier('B', ['b'])
        erd.add_identifier('C', ['c'])

        expected_bounds = (0,math.inf)

        self.assertEqual( expected_bounds, calculate_bounds( erd, ["a"], ["c"] ) )


# Two entity sets are connected via relationships in parallel.
class TestCase04(unittest.TestCase):
    def test_converter(self):
        erd = ERD()
        erd.add_entity_set("A")
        erd.add_attribute("a")
        erd.add_entity_set("B")
        erd.add_attribute("b")
        erd.add_relationship("R1")
        erd.add_relationship("R2")
        erd.connect("A", "R1", 1, 2)
        erd.connect("B", "R1", 0, 1)
        erd.connect("A", "R2", 0, 1)
        erd.connect("B", "R2", 1, 1)
        erd.attach('a', "A")
        erd.attach('b', "B")
        erd.add_identifier('A', ['a'])
        erd.add_identifier('B', ['b'])

        expected_bounds = (1,3)

        self.assertEqual( expected_bounds, calculate_bounds( erd, ["a"], ["b"] ) )

# Two entity sets in a many-to-one relationship.
# Check for non-identifier attribute and relationship attribute 
class TestCase05(unittest.TestCase):
    def test_converter(self):
        erd = ERD()
        erd.add_entity_set("A")
        erd.add_entity_set("B")
        erd.add_attribute("a1")
        erd.add_attribute("a2")
        erd.add_attribute("b")
        erd.add_attribute("r")
        erd.add_relationship("R")
        erd.connect("A", "R", 1, math.inf)
        erd.connect("B", "R", 1, 1)
        erd.attach('a1', "A")
        erd.attach('a2', "A")
        erd.attach('b', "B")
        erd.attach('r', "R")
        erd.add_identifier('A', ['a1','a2'])
        erd.add_identifier('B', ['b'])

        expected_bounds = (1,math.inf)

        self.assertEqual( expected_bounds, calculate_bounds( erd, ["a1"], ["r"] ) )


# Involving a weak entity set
class TestCase06(unittest.TestCase):
    def test_converter(self):
        erd = ERD()
        erd.add_entity_set("A")
        erd.add_entity_set("B")
        erd.add_entity_set("C")
        erd.add_attribute("a1")
        erd.add_attribute("a2")
        erd.add_attribute("b")
        erd.add_attribute("c")
        erd.add_relationship("R1")
        erd.add_relationship("R2")
        erd.connect("A", "R1", 1, 1)
        erd.connect("B", "R1", 1, math.inf)
        erd.connect("A", "R2", 0, 1)
        erd.connect("C", "R2", 0, math.inf)
        erd.attach('a1', "A")
        erd.attach('a2', "A")
        erd.attach('b', "B")
        erd.attach('c', "C")
        erd.add_identifier('A', ['a1','b'])
        erd.add_identifier('B', ['b'])
        erd.add_identifier('C', ['c'])

        expected_bounds = (0,1)

        self.assertEqual( expected_bounds, calculate_bounds( erd, ["a1", "b"], ["c"] ) )

# Involves a subset hierarchy
class TestCase07(unittest.TestCase):
    def test_converter(self):
        erd = ERD()
        erd.add_entity_set("A")
        erd.add_entity_set("C")
        erd.add_attribute("a")
        erd.add_attribute("b")
        erd.add_attribute("c")
        erd.add_generalisation("B", ["C"], "(p,e)")
        erd.attach('c', "C")
        erd.attach('b', "B")
        erd.attach('a', "A")

        erd.add_identifier("A", ["a"])
        erd.add_identifier("B", ["b"])

        erd.add_relationship("R")
        erd.connect("A", "R", 1, 1)
        erd.connect("B", "R", 1, 1)

        expected_bounds = (1,math.inf)

        self.assertEqual( expected_bounds, calculate_bounds( erd, ["c"], ["a"] ) )



# Two entity sets are related to each other across a generalisation hierarchy.
class TestCase09(unittest.TestCase):
    def test_converter(self):
        erd = ERD()
        erd.add_entity_set("A")
        erd.add_entity_set("B")
        erd.add_entity_set("D")
        erd.add_attribute("d")
        erd.add_attribute("c")
        erd.add_generalisation("C", ["A","B"], "(t,e)")
        erd.attach('c', "C")
        erd.attach('d', "D")

        erd.add_identifier("C", ["c"])
        erd.add_identifier("D", ["d"])

        erd.add_relationship("R1")
        erd.add_relationship("R2")
        erd.connect("A", "R1", 1, 1)
        erd.connect("B", "R2", 0, 1)
        erd.connect("D", "R1", 1, math.inf)
        erd.connect("D", "R2", 1, math.inf)

        expected_bounds = (0,1)

        self.assertEqual( expected_bounds, calculate_bounds( erd, ["c"], ["d"] ) )



# Two entity sets are related to each other across a generalisation hierarchy.
class TestCase10(unittest.TestCase):
    def test_converter(self):
        erd = ERD()
        erd.add_entity_set("A")
        erd.add_entity_set("B")
        erd.add_entity_set("D")
        erd.add_attribute("b")
        erd.add_attribute("a")
        erd.add_attribute("d")
        erd.add_attribute("c")
        erd.add_generalisation("C", ["A","B"], "(t,o)")
        erd.attach('a', "A")
        erd.attach('b', "B")
        erd.attach('c', "C")
        erd.attach('d', "D")

        erd.add_identifier("C", ["c"])
        erd.add_identifier("D", ["d"])


        erd.add_relationship("R")
        erd.connect("A", "R", 1, 1)
        erd.connect("B", "R", 0, 3)
        erd.connect("D", "R", 1, 1)

        expected_bounds = (0,4)

        self.assertEqual( expected_bounds, calculate_bounds( erd, ["c"], ["d"] ) )

# Two entity sets are connected via length-2 paths in parallel.
class TestCase11(unittest.TestCase):
    def test_converter(self):
        erd = ERD()
        erd.add_entity_set("A")
        erd.add_entity_set("B")
        erd.add_entity_set("C")
        erd.add_entity_set("D")

        erd.add_attribute("a")
        erd.add_attribute("b")
        erd.add_attribute("c")
        erd.add_attribute("d")

        erd.add_relationship("R1")
        erd.add_relationship("R2")
        erd.add_relationship("R3")
        erd.add_relationship("R4")

        erd.connect("A", "R1", 1, 2)
        erd.connect("B", "R1", 1, math.inf)
        erd.connect("C", "R2", 0, 1)
        erd.connect("B", "R2", 3, 4)
        erd.connect("A", "R3", 1, 3)
        erd.connect("D", "R3", 1, 1)
        erd.connect("C", "R4", 1, 1)
        erd.connect("D", "R4", 2, 5)

        erd.attach('a', "A")
        erd.attach('b', "B")
        erd.attach('c', "C")
        erd.attach('d', "D")

        erd.add_identifier('A', ['a'])
        erd.add_identifier('B', ['b'])
        erd.add_identifier('C', ['c'])
        erd.add_identifier('D', ['d'])

        expected_bounds = (3,23)

        self.assertEqual( expected_bounds, calculate_bounds( erd, ["a"], ["c"] ) ) 

# Two entity sets connected via parallel paths that temporarily merge
class TestCase16(unittest.TestCase):
    def test_converter(self):
        erd = ERD()
        erd.add_entity_set("A")
        erd.add_entity_set("B")
        erd.add_entity_set("C")
        erd.add_entity_set("D")

        erd.add_attribute("a")
        erd.add_attribute("b")
        erd.add_attribute("c")
        erd.add_attribute("d")

        erd.add_relationship("R1")
        erd.add_relationship("R2")
        erd.add_relationship("R3")
        erd.add_relationship("R4")
        erd.add_relationship("R5")

        erd.connect("A", "R1", 0, 1)
        erd.connect("B", "R1", 2, 4)
        erd.connect("A", "R2", 1, 4)
        erd.connect("B", "R2", 0, 3)
        erd.connect("B", "R3", 1, 1)
        erd.connect("C", "R3", 1, 2)
        erd.connect("C", "R4", 2, 3)
        erd.connect("D", "R4", 1, 2)
        erd.connect("C", "R5", 1, 1)
        erd.connect("D", "R5", 1, 2)

        erd.attach('a', "A")
        erd.attach('b', "B")
        erd.attach('c', "C")
        erd.attach('d', "D")

        erd.add_identifier('A', ['a'])
        erd.add_identifier('B', ['b'])
        erd.add_identifier('C', ['c'])
        erd.add_identifier('D', ['d'])

        expected_bounds = (2,20)

        self.assertEqual( expected_bounds, calculate_bounds( erd, ["a"], ["d"] ) )

# Two entity sets are related to each other across a
# two-level generalisation hierarchy with inconsistent types.
class TestCase19(unittest.TestCase):
    def test_converter(self):
        erd = ERD()
        erd.add_entity_set("B")
        erd.add_entity_set("C")
        erd.add_entity_set("E")
        erd.add_entity_set("F")
        erd.add_entity_set("G")

        erd.add_attribute("b")
        erd.add_attribute("a")
        erd.add_attribute("g")

        erd.add_generalisation("D", ["E","F"], "(t,e)")
        erd.add_generalisation("A", ["C","D"], "(t,o)")

        erd.attach('a', "A")
        erd.attach('b', "B")
        erd.attach('g', "G")

        erd.add_identifier("A", ["a"])
        erd.add_identifier("B", ["b"])
        erd.add_identifier("G", ["g"])

        erd.add_relationship("R1")
        erd.add_relationship("R2")
        erd.add_relationship("R3")

        erd.connect("A", "R1", 0, math.inf)
        erd.connect("B", "R1", 1, 2)
        erd.connect("E", "R2", 1, 1)
        erd.connect("G", "R2", 0, math.inf)
        erd.connect("F", "R3", 1, 2)
        erd.connect("G", "R3", 1, 1)

        expected_bounds = (0,4)

        self.assertEqual( expected_bounds, calculate_bounds( erd, ["b"], ["g"] ) )

# Hardest test case.
# Involves multiple components
# (parallel paths, subsets, multi-level generalisation hierarchies, and weak entity sets)
class TestCase20(unittest.TestCase):
    def test_converter(self):
        erd = ERD()
        erd.add_entity_set("B")
        erd.add_entity_set("E")
        erd.add_entity_set("F")
        erd.add_entity_set("H")

        erd.add_attribute("a")
        erd.add_attribute("b")
        erd.add_attribute("e")
        erd.add_attribute("f")
        erd.add_attribute("g1")
        erd.add_attribute("g2")
        erd.add_attribute("h")

        erd.add_generalisation("C", ["E"], "(p,e)")
        erd.add_generalisation("D", ["F"], "(p,e)")
        erd.add_generalisation("G", ["H"], "(p,e)")
        erd.add_generalisation("A", ["B", "C", "D"], "(p,o)")

        erd.attach('a', "A")
        erd.attach('b', "B")
        erd.attach('e', "E")
        erd.attach('f', "F")
        erd.attach('g1', "G")
        erd.attach('g2', "G")
        erd.attach('h', "H")

        erd.add_identifier("G", ["g1"])
        erd.add_identifier("A", ["a", "g1"])
        erd.add_identifier("F", ["f"])


        erd.add_relationship("R1")
        erd.add_relationship("R2")
        erd.connect("A", "R1", 1, 1)
        erd.connect("G", "R1", 0, math.inf)
        erd.connect("F", "R2", 1, 1)
        erd.connect("H", "R2", 0, math.inf)

        expected_bounds = (1,2)

        self.assertEqual( expected_bounds, calculate_bounds( erd, ["f"], ["h"] ) )


# Run all unit tests above.
unittest.main(argv=[''],verbosity=2, exit=False)
