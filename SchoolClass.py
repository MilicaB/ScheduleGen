class SchoolClass:
    def __init__(self, grade, subjects, label):
        self._grade = grade
        self._label = label
        self._subjects = subjects

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

    def __str__(self):
        return str(self.grade) + str(self.label) + " " + str(self.subjects)
    
    def __repr__(self):
        return str(self)
