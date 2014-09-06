import unittest
from ScheduleCreator import *

class TestScheduleCreator(unittest.TestCase):

   

    def test_create_schedule_for_one_class(self):
        create_tables()
        class_fifth_a = SchoolClass(grade = 5, label = 'A')
        class_fifth_a.save()
        table = create_schedule_table()
        subjects = [["Math", 2, "Dimitrov", 3], \
                    ["Bulgarian and literature", 2, "Dimitrova", 3],\
                    ["Sport", 2, "Ivanov", 1],\
                    ["History", 2, "Petrova", 2],\
                    ["Chemistry", 1, "Ivanova", 2],\
                    ["Phisics", 1, "Petrov", 2],\
                    ["Art", 1, "Hristov", 1],
                    ["Music", 1, "Hristova", 1],
                    ["Biology", 2, "Koleva", 2]]
        for subject in subjects:
            s = Subject(name = subject[0], coefficient = subject[3],\
            	            school_class = class_fifth_a, workload = subject[1], \
            	            teacher = subject[2])
            s.save()
        table_expected = [[['Dimitrova', 'Bulgarian and literature']], \
                        [['Koleva', 'Biology']], [['Ivanov', 'Sport']], \
                        [['Dimitrova', 'Bulgarian and literature']], \
                        [['Petrova', 'History']], [['Ivanov', 'Sport']], \
                        [['Dimitrov', 'Math']], [['Petrova', 'History']], \
                        [['Hristova', 'Music']], [['Dimitrov', 'Math']], \
                        [['Petrov', 'Phisics']], [['Hristov', 'Art']], \
                        [['Koleva', 'Biology']], [['Ivanova', 'Chemistry']], \
                        ['empty']]
        create_schedule_for_one_class(class_fifth_a, table, 0)
        print(table)
        SchoolClass.delete().where(SchoolClass.grade == 5)
        Subject.delete().where(Subject.school_class == class_fifth_a)
        self.assertEqual(table_expected, table)
        






if __name__ == '__main__':
    unittest.main()