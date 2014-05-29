import unittest

from SchoolClass import *


class SchoolClassTest(unittest.TestCase):
    def test_immutability_of_grade(self):
        fifth_a_grade = SchoolClass(5, ["Math", "Literature", "Phisics", "Sport", "Art"], 'A')
        self.assertRaises(AttributeError, fifth_a_grade.__setattr__, 'grade', 6)

    def test_immutability_of_subjects(self):
        fifth_a_grade = SchoolClass(5, ["Math", "Literature", "Phisics", "Sport", "Art"], 'A')
        self.assertRaises(AttributeError, fifth_a_grade.__setattr__, 'subjects', ["English", "Philosophy", "Geography"])

    def test_immutability_of_label(self):
        fifth_a_grade = SchoolClass(5, ["Math", "Literature", "Phisics", "Sport", "Art"], 'A')
        self.assertRaises(AttributeError, fifth_a_grade.__setattr__, 'label', 'B')


if __name__ == '__main__':
    unittest.main()
