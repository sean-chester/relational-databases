# Test cases for calculate_bounds() method.
#
# Not all test cases have been provided; part of this assignment
# is to write a good test suite for the problem.
# However, pre-grading will be performed on the final set of
# test cases; so, it is possible to know in advance whether
# your test coverage matches ours.
# The final evaluation will contain twenty test cases.

from erd import *
from cardinalities_bounds import calculate_bounds

import unittest


# Single entity set with a single attribute which is the PK
class TestCase1(unittest.TestCase):
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


# Run all unit tests above.
unittest.main(argv=[''],verbosity=2, exit=False)
