class Subject:
    def __init__(self, name, workloads):
        self._name = name
        self._workloads = workload

    @property
    def name(self):
        return self._name

    @property
    def workloads(self):
        return self._workloads

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

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
