class Subject:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class HardSubject(Subject):
    _coefficient = 3
    @property
    def coefficient(self):
        return self._coefficient

class MediumSubject(Subject):
    _coefficient = 2
    @property
    def coefficient(self):
        return self._coefficient

class EasySubject(Subject):
    _coefficient = 1
    @property
    def coefficient(self):
        return self._coefficient
