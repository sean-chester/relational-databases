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

from Schedule import *
from SerialisabilityTester import *


# empty schedule
class TestCase01(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_superkey(self):

        schedule = Schedule()

        expected_simple_schedule = SimpleSchedule()

        self.assertEqual( expected_simple_schedule, to_serial( schedule ) )


# simple serial schedule, T1, T2
class TestCase02(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_superkey(self):

        operation1 = IOOperation(1, "READ", "A")
        operation2 = IOOperation(1, "WRITE", "A")
        operation3 = IOOperation(2, "READ", "A")
        operation4 = IOOperation(2, "WRITE", "A")
        schedule = Schedule([operation1, operation2, operation3, operation4])

        expected_simple_schedule = SimpleSchedule([1,2])

        self.assertEqual( expected_simple_schedule, to_serial( schedule ) )


# inverted serial schedule, T2 T1, with writes
class TestCase03(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_superkey(self):

        operation1 = IOOperation(2, "READ", "A")
        operation2 = IOOperation(2, "WRITE", "A")
        operation3 = IOOperation(1, "READ", "A")
        operation4 = IOOperation(1, "WRITE", "A")
        schedule = Schedule([operation1, operation2, operation3, operation4])

        expected_simple_schedule = SimpleSchedule([2,1])

        self.assertEqual( expected_simple_schedule, to_serial( schedule ) )



# inverted serial schedule, T2 T1, with only reads
class TestCase04(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_superkey(self):

        operation1 = IOOperation(2, "READ", "A")
        operation2 = IOOperation(2, "READ", "B")
        operation3 = IOOperation(1, "READ", "A")
        operation4 = IOOperation(1, "READ", "B")
        schedule = Schedule([operation1, operation2, operation3, operation4])

        expected_simple_schedule = SimpleSchedule([1,2])

        self.assertEqual( expected_simple_schedule, to_serial( schedule ) )


# blended schedule with only reads
class TestCase05(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_superkey(self):

        operation1 = IOOperation(2, "READ", "A")
        operation3 = IOOperation(1, "READ", "A")
        operation2 = IOOperation(3, "READ", "B")
        operation4 = IOOperation(1, "READ", "B")
        operation5 = IOOperation(2, "READ", "A")
        operation6 = IOOperation(3, "READ", "B")
        schedule = Schedule([operation1, operation2, operation3, operation4, operation5, operation6])

        expected_simple_schedule = SimpleSchedule([1,2,3])

        self.assertEqual( expected_simple_schedule, to_serial( schedule ) )


# blended schedule with writes but to unique elements
class TestCase06(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_foreignkey(self):

        operation1 = IOOperation(2, "READ", "A")
        operation2 = IOOperation(1, "READ", "B")
        operation3 = IOOperation(3, "READ", "C")
        operation4 = IOOperation(3, "WRITE", "C")
        operation5 = IOOperation(1, "WRITE", "B")
        operation6 = IOOperation(2, "WRITE", "A")
        schedule = Schedule([operation1, operation2, operation3, operation4, operation5, operation6])

        expected_simple_schedule = SimpleSchedule([1,2,3])

        self.assertEqual( expected_simple_schedule, to_serial( schedule ) )


# blended schedule with writes, non-serialisable
class TestCase07(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_foreignkey(self):

        operation1 = IOOperation(2, "READ", "B")
        operation2 = IOOperation(1, "READ", "B")
        operation3 = IOOperation(3, "READ", "C")
        operation4 = IOOperation(3, "WRITE", "C")
        operation5 = IOOperation(1, "WRITE", "B")
        operation6 = IOOperation(2, "WRITE", "B")
        schedule = Schedule([operation1, operation2, operation3, operation4, operation5, operation6])

        expected_simple_schedule = None

        self.assertEqual( expected_simple_schedule, to_serial( schedule ) )


# blended schedule with writes, serialisable as T3 T1 T2
class TestCase08(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_foreignkey(self):

        operation1 = IOOperation(2, "READ", "A")
        operation2 = IOOperation(1, "READ", "B")
        operation3 = IOOperation(3, "READ", "B")
        operation4 = IOOperation(3, "READ", "C")
        operation5 = IOOperation(3, "WRITE", "C")
        operation6 = IOOperation(1, "WRITE", "B")
        operation7 = IOOperation(2, "WRITE", "B")
        schedule = Schedule([operation1, operation2, operation3, operation4, operation5, operation6, operation7])

        expected_simple_schedule = SimpleSchedule([3,1,2])

        self.assertEqual( expected_simple_schedule, to_serial( schedule ) )


# blended schedule with writes, not serialisable
class TestCase09(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_foreignkey(self):

        operation1 = IOOperation(3, "READ", "A")
        operation2 = IOOperation(2, "READ", "A")
        operation3 = IOOperation(1, "READ", "A")
        operation4 = IOOperation(3, "READ", "B")
        operation5 = IOOperation(2, "READ", "B")
        operation6 = IOOperation(1, "READ", "B")
        operation7 = IOOperation(2, "WRITE", "A")
        operation8 = IOOperation(1, "WRITE", "B")
        operation9 = IOOperation(3, "WRITE", "B")
        schedule = Schedule([operation1, operation2, operation3, operation4, operation5, operation6, operation7, operation8, operation9])

        expected_simple_schedule = None

        self.assertEqual( expected_simple_schedule, to_serial( schedule ) )


# blended schedule with writes, multiple serialisable schedules
class TestCase10(unittest.TestCase):
    @timeout_decorator.timeout(15)
    def test_foreignkey(self):

        operation1 = IOOperation(2, "READ", "A")
        operation2 = IOOperation(1, "READ", "B")
        operation3 = IOOperation(3, "READ", "B")
        operation4 = IOOperation(3, "READ", "C")
        operation5 = IOOperation(3, "WRITE", "B")
        operation6 = IOOperation(1, "READ", "A")
        operation7 = IOOperation(2, "WRITE", "B")
        schedule = Schedule([operation1, operation2, operation3, operation4, operation5, operation6, operation7])

        expected_simple_schedule = SimpleSchedule([1,3,2])

        self.assertEqual( expected_simple_schedule, to_serial( schedule ) )


# Run all unit tests above.
unittest.main(argv=[''],verbosity=2, exit=False)
