class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.birthdate = None
        self.birthplace = None

    def __str__(self):
        return f'{self.name}, born on {self.birthdate}, works as {self.position}'

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person()
    
    def build(self):
        return self.person

class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self

class PersonJobBuilder(PersonInfoBuilder):
    def works_at(self, job):
        self.person.position = job
        return self


class PersonDateBuilder(PersonJobBuilder):
    def born(self, data):
        self.person.birthdate = data
        return self


builder = PersonDateBuilder().born('01.10.2000').works_at('freelancer').called('Ante')

print(builder.build())

