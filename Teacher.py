class Teacher:
    def __init__(self, name, subject):
        self._name = name
        self._subject = subject
        self.teach_classes = []

    @property
    def name(self):
        return self._name

    @property
    def subject(self):
        return self._subject

    def add_teach_classes(self, school_class):
        self.teach_classes.append(school_class)
