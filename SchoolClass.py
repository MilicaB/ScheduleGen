class SchoolClass:
    def __init__(self, grade, subjects, label, workload):
        self._grade = grade
        self._label = label
        self._subjects = subjects
        self._workload = workload

    def add_teacher(self, teacher):
        self.teacher = teacher

    @property
    def grade(self):
        return self._grade

    @property
    def label(self):
        return self._label

    @property
    def subjects(self):
        return self._subjects

    def workload(self):
        return workload

    def __str__(self):
        return str(self.grade) + str(self.label) + " " + str(self.subjects)
    
    def __repr__(self):
        return str(self)
