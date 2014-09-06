import DataBase
from DataBase import *
import itertools
import time


SCHOOL_CLASSES = SchoolClass.select()
SUBJECTS = Subject.select()
MAX_SUBJECTS_PER_DAY = 3
MAX_SUBJECTS_PER_WEEK = MAX_SUBJECTS_PER_DAY * 5
FILE_NAME = "Schedule"

def create_schedule_table():
    classes_counter = 0
    for school_class in SCHOOL_CLASSES:
        classes_counter += 1
    return [["empty" for school_class in range(classes_counter)] for t in \
            range( MAX_SUBJECTS_PER_WEEK)]

def get_posion_left(school_class, schedule_table, subject, index):
    for position in range(MAX_SUBJECTS_PER_WEEK):
        if index == 0 and schedule_table[position][index] == 'empty':
            return position
        elif index > 0:
            flag = True
            for class_index in range(index):
                subject_teacher = Subject.select().where(Subject.school_class \
                                == school_class \
                                and Subject.name == subject).get().teacher
                if schedule_table[position][index] != 'empty' or \
                    (schedule_table[position][class_index] != 'empty' and \
                    schedule_table[position][class_index][0] \
                    == subject_teacher):
                    flag = False
            if flag == True:
                return position


def get_position_of_subject(school_class, schedule_table, subject, day, index):   
    for position in range(MAX_SUBJECTS_PER_DAY * day, MAX_SUBJECTS_PER_DAY * \
                        (day + 1)):
        if index == 0 and schedule_table[position][index] == 'empty':
            return position
        elif index > 0:
            flag = True
            for class_index in range(index):
                subject_teacher = Subject.select().where(Subject.school_class \
                    == school_class and Subject.name == subject).get().teacher
                if schedule_table[position][index] != 'empty' or \
                    (schedule_table[position][class_index] != 'empty' and \
                    schedule_table[position][class_index][0] \
                    == subject_teacher):
                    flag = False
            if flag == True:
                return position
    #return get_position_left()


def create_schedule_for_one_class(school_class, schedule_table, index):
    school_class_subjects = []
    for subject in Subject.select().where(Subject.school_class \
        == school_class):
        school_class_subjects += [repeated_subject for repeated_subject in \
        itertools.repeat(subject.name, subject.workload)]
    school_class_subjects.reverse()
    for subject_index in range(len(school_class_subjects)):
        subject_position = get_position_of_subject(school_class,schedule_table, \
                        school_class_subjects[subject_index], \
                        subject_index % 5, index)
        subject_teacher = Subject.select().where(Subject.school_class \
            == school_class and Subject.name \
            == school_class_subjects[subject_index]).get().teacher
        schedule_table[subject_position][index] = \
        [subject_teacher, school_class_subjects[subject_index]]

def create_schedule_for_all_classes():
    table = create_schedule_table()
    index = 0
    for school_class in SchoolClass.select():
        create_schedule_for_one_class(school_class, table, index)
        index+=1
    return table

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def create_schedule_file():
    file_name_with_date = FILE_NAME + time.strftime("%Y_%m_%d") + '.csv'
    table = create_schedule_for_all_classes()
    with open(file_name_with_date, 'w') as table_file:
        table_file.write('Day,Hour,')
        for school_class in SchoolClass.select():
            table_file.write(str(school_class.grade) + school_class.label + \
            ',')
        table_file.write('\n')
        for row in range(MAX_SUBJECTS_PER_WEEK):
            if row % MAX_SUBJECTS_PER_DAY == 0:
                table_file.write(WEEKDAYS[int(row / MAX_SUBJECTS_PER_DAY)] + \
                ',')
            else:
                table_file.write(" ,")
            table_file.write(str(row % MAX_SUBJECTS_PER_DAY + 1) + ',')
            for column in range(len(table[row])):
                if(table[row][column] == 'empty'):
                    table_file.write(" ,")
                else:
                    table_file.write(table[row][column][1] + ' - ' + \
                        table[row][column][0] + ',')
            table_file.write('\n')
    table_file.close()