from peewee import *

school_database = SqliteDatabase('school.db')

class BaseModel(Model):
    class Meta:
        database = school_database


class SchoolClass(BaseModel):
    grade = IntegerField()
    label = CharField()
    class Meta:
        order_by = ('grade','label',)


class Subject(BaseModel):
    name = TextField()
    coefficient = IntegerField()
    school_class = ForeignKeyField(SchoolClass)
    workload = IntegerField()
    teacher = TextField()
    class Meta:
        order_by = ('coefficient', 'workload',)

def create_tables():
    school_database.connect()
    school_database.create_tables([SchoolClass, Subject], True)