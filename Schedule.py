weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

class Schedule:
    def __init__(self, school_class, class_schedule):
        _school_class = school_class
        _class_schedule = {weekDays[i]:class_schedule[i] for i in range(5)}

    @property
    def school_class():
        return _school_class

    @property
    def class_schedule():
        return _class_schedule
    