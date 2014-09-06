from dataBase import *
import itertools

create_school_classes_database()
create_subjects_database()

school_classes = get_school_classes_content()

subjects = get_subjects_content()

def make_schedule_for_one_class(school_class):
    all_subjects = list([itertools.repeat(subject, \
    	            subject.workloads[school_class.grade]) \
                    for subject in subjects])
    sorted_subjects = sorted(all_subjects, key = lambda subject: \
    	                    subject.coefficient, reverse = True)
    schedule = [[],[],[],[],[]]
    for index, subject in enumerate(sorted_subjects):
    	schedule[index%5].append(subject.name)
    return Schedule(school_class, schedule)

def make_schedule_for_all_classes():
	return [make_schedule_for_one_classes(school_class) \
	        for school_class in school_classes]
