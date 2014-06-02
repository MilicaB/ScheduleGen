class SchoolClass:
    def __init__(self, grade, subjects, label, workload):
        self._grade = grade
        self._label = label
        self._subjects = subjects
        self._workload = workload

    @property
    def grade(self):
        return self._grade

    @property
    def label(self):
        return self._label

    @property
    def subjects(self):
        return self._subjects

    @property
    def workload(self):
        return self._workload

    def __str__(self):
        return str(self.grade) + str(self.label) + " " + str(self.subjects)
    
    def __repr__(self):
        return str(self)
