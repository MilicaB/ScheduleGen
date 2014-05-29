import unittest

from Subject import *


class SubjectTest(unittest.TestCase):
    def test_immutability_of_name(self):
        math = Subject("Math")
        self.assertRaises(AttributeError, math.__setattr__, 'name', "Art")


class HardSubjectTest(unittest.TestCase):
    def test_immutability_of_name(self):
        math = HardSubject("Math")
        self.assertRaises(AttributeError, math.__setattr__, 'name', "Art")

    def test_immutability_of_coefficient(self):
        math = HardSubject("Math")
        self.assertRaises(AttributeError, math.__setattr__, 'coefficient', 5)

class MediumSubjectTest(unittest.TestCase):
    def test_immutability_of_name(self):
        history = MediumSubject("History")
        self.assertRaises(AttributeError, history.__setattr__, 'name', "Art")

    def test_immutability_of_coefficient(self):
        history = HardSubject("History")
        self.assertRaises(AttributeError, history.__setattr__, 'coefficient', 1)

class EasySubjectTest(unittest.TestCase):
    def test_immutability_of_name(self):
        sport = MediumSubject("Sport")
        self.assertRaises(AttributeError, sport.__setattr__, 'name', "Art")

    def test_immutability_of_coefficient(self):
        sport = HardSubject("Sport")
        self.assertRaises(AttributeError, sport.__setattr__, 'coefficient', 1)


if __name__ == '__main__':
    unittest.main()
