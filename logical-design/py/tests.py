# Test cases for ImplementMe class.
# The mocked objects (and therefore expected output) may undergo minor change
# at the point of evaluation, but the functionality tested by each test case will not.
# Minor changes that may occur include:
#   * adding or removing a relation or FD to change the expected output
#   * changing attribute labels
#   * toggling the result (e.g., swapping an incorrect one for a correct one or vice versa)
#
# Note that the final two cases, B1 and B2, are bonus test cases
# and the assignment is evaluated out of 20.

import unittest
import time
import timeout_decorator
 
from relation import *
from functional_dependency import *
from bcnf import ImplementMe


# A single attribute forms a key
class TestCase01(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'a','b','c'})})
        fds = FDSet({FunctionalDependency({'a'}, {'b','c'})})

        expected_output = 0

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# Decomposition misses a violation
class TestCase02(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'a','b','c'})})
        fds = FDSet({FunctionalDependency({'a'}, {'b'})})

        expected_output = -1

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# Uses combining rule to make key
class TestCase03(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'a','b','c'})})
        fds = FDSet({FunctionalDependency({'a'}, {'b'}), \
                FunctionalDependency({'a'}, {'c'})})

        expected_output = 0

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# Misses violation on second FD
class TestCase04(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'a','b','c'})})
        fds = FDSet({FunctionalDependency({'a'}, {'b'}), \
                FunctionalDependency({'b'}, {'c'})})

        expected_output = -1

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# Cycle. Everything's a key.
# Randomly changed: add a non-key attribute
class TestCase05(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'a','b','c','d','e'})})
        fds = FDSet({FunctionalDependency({'a'}, {'b'}), \
                FunctionalDependency({'b'}, {'c'}), \
                FunctionalDependency({'c'}, {'d'}), \
                FunctionalDependency({'d'}, {'a'}) })

        expected_output = -1

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# BCNF decomposition has already been done
# Randomly changed: omit one attribute 
class TestCase06(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'a','b'}), \
                Relation({'c','d'}) })
        fds = FDSet({FunctionalDependency({'a'}, {'b'}) })

        expected_output = -1

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# In BCNF but breaks up a prime
# Randomly changed: show correct decomposition
class TestCase07(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'a','b','c'}) })
        fds = FDSet({FunctionalDependency({'a'}, {'b','c'}), \
                FunctionalDependency({'b'}, {'a'}) })

        expected_output = 0

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# Decomposition not lossless
class TestCase08(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'a','b'}), \
                Relation({'c','d'}) })
        fds = FDSet({FunctionalDependency({'a'}, {'b'}) })

        expected_output = -1

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# Decomposition swaps FD
class TestCase09(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'a','b'}), \
                Relation({'b','d'}), \
                Relation({'c','d'}) })
        fds = FDSet({FunctionalDependency({'b'}, {'a'}), \
                FunctionalDependency({'c'}, {'d'}) })

        expected_output = -1

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )



# Need to calculate full closure with combining rule
class TestCase10(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'a','b','c','d'}), \
                Relation({'a','b','e'}) })
        fds = FDSet({FunctionalDependency({'b', 'a'}, {'c'}), \
                FunctionalDependency({'a','b'}, {'d'}) })

        expected_output = 1

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# Only one FD is a key
# Randomly changed: add another FD to split another relation
class TestCase11(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'b','c'}), \
                Relation({'c','a'}) , \
                Relation({'a','d'}) })
        fds = FDSet({FunctionalDependency({'b'}, {'a','c'}), \
                FunctionalDependency({'a'}, {'d'}), \
                FunctionalDependency({'c'}, {'a'}) })

        expected_output = 2

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )

# Forgets to calculate closure
# Randomly changed: split erroneously based on first FD
class TestCase12(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'a','b','c','e'}), \
                Relation({'b','a','d'}) })
        fds = FDSet({FunctionalDependency({'b', 'a'}, {'e','c'}), \
                FunctionalDependency({'a','b'}, {'d'}) })

        expected_output = -1

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# Standard multi-recursion case
class TestCase13(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'a','b'}), \
                Relation({'a','c'}), \
                Relation({'b','d'}) })
        fds = FDSet({FunctionalDependency({'b'}, {'d'}), \
                FunctionalDependency({'a'}, {'c'}) })

        expected_output = 2

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# First half of non-deterministic case 1
class TestCase14(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'e','f'}), \
                Relation({'a','b','e'}), \
                Relation({'a','b','c','d'}) })
        fds = FDSet({FunctionalDependency({'a','b'}, {'e'}), \
                FunctionalDependency({'c','d'}, {'e'}), \
                FunctionalDependency({'e'}, {'f'}) })

        expected_output = 2

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# Similar to above, but forgot a step and non-determinism removed
class TestCase15(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'c','e','f'}), \
                Relation({'a','b','d'}), \
                Relation({'a','b','e'}) })
        fds = FDSet({FunctionalDependency({'a','b'}, {'e'}), \
                FunctionalDependency({'f'}, {'c'}), \
                FunctionalDependency({'e'}, {'f'}) })

        expected_output = -1

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# similar to non-deterministic case,
# but completes up to the second-from-last step after random choice
# Randomly changed: show correct answer
class TestCase16(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'e','f'}), \
                Relation({'g','f'}), \
                Relation({'e','c','d'}), \
                Relation({'a','b','c','d'}) })
        fds = FDSet({FunctionalDependency({'a','b'}, {'e'}), \
                FunctionalDependency({'c','d'}, {'e'}), \
                FunctionalDependency({'e'}, {'f'}), \
                FunctionalDependency({'f'}, {'g'}) })

        expected_output = 3

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# Recursed too far, basically applied 3NF algorithm
# Randomly changed: show correct answer
class TestCase17(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'a','b','c'}), \
                Relation({'b','d'}), \
                Relation({'e','d'}) })
        fds = FDSet({FunctionalDependency({'a'}, {'b'}), \
                FunctionalDependency({'b'}, {'c'}), \
                FunctionalDependency({'c'}, {'a'}), \
                FunctionalDependency({'d'}, {'e'}) })

        expected_output = 2

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# Question 5 from the BCNF worksheet
# Simplified to eliminate non-determinism in assignment solution
class TestCase18(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'c','d','e'}), \
                Relation({'a','b','c'}) })
        fds = FDSet({FunctionalDependency({'a'}, {'b','c'}), \
                FunctionalDependency({'c'}, {'b', 'a'}) })

        expected_output = 1

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )



# Only one violation out of four
class TestCase19(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'a','b','c','d'}) })
        fds = FDSet({FunctionalDependency({'a','b'}, {'c'}), \
                FunctionalDependency({'a','c'}, {'b'}), \
                FunctionalDependency({'c'}, {'d'}), \
                FunctionalDependency({'d'}, {'a'}) })

        expected_output = -1

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# Recursion non-linear
class TestCase20(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'e','d','f','g'}), \
                Relation({'c','a','b','f','e','d'}) })
        fds = FDSet({FunctionalDependency({'f','e','d'}, {'c','a','b'}), \
                FunctionalDependency({'f'}, {'e'}), \
                FunctionalDependency({'c'}, {'b'}) })

        expected_output = -1

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# Non-deterministic -- side where second FD is chosen first (less likely)
class TestCase21(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'e','f'}), \
                Relation({'d','c','e'}), \
                Relation({'a','b','c','d'}) })
        fds = FDSet({FunctionalDependency({'a','b'}, {'e'}), \
                FunctionalDependency({'c','d'}, {'e'}), \
                FunctionalDependency({'e'}, {'f'}) })

        expected_output = 2

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# Non-deterministic -- side where second FD is chosen first (less likely)
# but last recursive step is missed
class TestCase22(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_is_bncf(self):
        relations = RelationSet({Relation({'d','c','e','f'}), \
                Relation({'a','b','c','d'}) })
        fds = FDSet({FunctionalDependency({'a','b'}, {'e'}), \
                FunctionalDependency({'c','d'}, {'e'}), \
                FunctionalDependency({'e'}, {'f'}) })

        expected_output = -1

        self.assertEqual( expected_output, ImplementMe.DecompositionSteps( relations, fds ) )


# Run all unit tests above.
unittest.main(argv=[''],verbosity=2, exit=False)
