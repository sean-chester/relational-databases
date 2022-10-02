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


# Two entity sets in a many-to-one relationship.
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

        expected_bounds = (1,1)

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

        expected_bounds = (0,1)

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

        expected_bounds = (0,3)

        self.assertEqual( expected_bounds, calculate_bounds( erd, ["c"], ["d"] ) )



# Run all unit tests above.
unittest.main(argv=[''],verbosity=2, exit=False)
