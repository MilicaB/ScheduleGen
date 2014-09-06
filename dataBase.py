import sqlite3
from SchoolClass import *
from Subject import *
from Schedule import *
from Teacher import *


school_classes = sqlite3.connect("SchoolClasses.db")


subjects = sqlite3.connect("Subjects.db")

SUBJECTS = [EasySubject, MediumSubject, HardSubject]

schedule = sqlite3.connect("Schedule.db")

teachers = sqlite3.connect("Teachers.db")

def create_school_classes_database():
    school_classes.execute('''CREATE TABLE SchoolClasses \
        (id INTEGER PRIMARY KEY, grade INTEGER, label TEXT, \
        subjects TEXT, workload INTEGER)''')

def add_new_school_class(school_class):
    school_classes.execute('''INSERT INTO \
        SchoolClasses (grade, label, subjects, workload) VALUES (?,?,?,?)''', \
        (school_class.grade, school_class.label, \
        ','.join(school_class.subjects),school_class.workload))
    school_classes.commit()

def get_school_class(school_class):
    class_identification = school_class.split()
    cursor = school_classes.execute(''' SELECT * FROM SchoolClasses WHERE \
            grade = ? AND label = ?'''(class_identification[0], class_identification[1]))
    return SchoolClass(cursor[1], cursor[2], cursor[3].split(','), cursor[4])

    
def get_school_classes_content():
    all_school_classes = []
    cursor = school_classes.execute(''' SELECT * FROM SchoolClasses ''')
    for row in cursor:
        all_school_classes.append(SchoolClass(row[1], row[2],\
                                   row[3].split(','), row[4]))
    return all_school_classes

def create_subjects_database():
    subjects.execute('''CREATE TABLE Subjects \
        (id INTEGER PRIMARY KEY, name TEXT, coefficient INTEGER, workloads TEXT)''')

def add_new_subject(subject):
    subjects.execute('''INSERT INTO Subjects (name, coefficient, workloads) \
        VALUES (?,?)''', (subject.name, subject.coefficient, ','.join(subject.workloads)))
    subjects.commit()


def get_subjects_content():
    all_subjects = []
    cursor = subjects.execute('''SELECT * FROM Subjects''')
    for row in cursor:
        all_subjects.append(SUBJECTS[row[2]-1](row[1], row[3].split(',')))
    return all_subjects

def create_schedule_database():
    school_classes.execute('''CREATE TABLE Schedule \
        (id INTEGER PRIMARY KEY, class TEXT, Monday TEXT, \
        Tuesday TEXT, Wednesday TEXT, Thursday TEXT, Friday TEXT)''')

def add_new_class_schedule(schedule):
    schedule.execute('''INSERT INTO Schedule (class, Monday, Tuesday, \ 
                    Wednesday, Thursday, Friday) VALUES (?,?,?,?,?,?)''', \
                    (schedule.school_class,\
                    ','.join(subject.class_schedule["Monday"]),\
                    ','.join(subject.class_schedule["Tuesday"]),\
                    ','.join(subject.class_schedule["Wednesday"]),\
                    ','.join(subject.class_schedule["Thursday"]),\
                    ','.join(subject.class_schedule["Friday"])))
    schedule.commit()

def get_schedule_content():
    schedule_all = []
    cursor = schedule.execute('''SELECT * FROM Schedule''')
    for row in cursor:
        schedule_all.append(Schedule(row[1], {WEEKDAYS[i]:row[i].split(',') for i in range(2, 6)}))
    return schedule_all

def get_school_class_schedule(school_class):
   cursor = schedule.execute('''SELECT * FROM Schedule WHERE class = ?''', (school_class,))
   return Schedule(school_class, {WEEKDAYS[i]:cursor[i].split(',') for i in range(2, 6)})

def create_teachers_database():
    teachers.execute('''CREATE TABLE Teachers (id INTEGER PRIMARY KEY, name TEXT,\
                    subject TEXT, classes TEXT) ''')

def add_new_teacher(teacher):
    teachers.execute(''' INSERT INTO Teachers (name, subject, classes)\
                    VALUES (?,?,?)''', (teacher.name, teacher.subject, \
                    ','.join(teacher.teach_classes)))