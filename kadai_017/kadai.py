class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 20

    def check_adult(self):
        if self.is_adult():
            print(f"{self.name}は大人である")
        else:
            print(f"{self.name}は大人ではない")

class HumanManager:
    def __init__(self):
        self.humans_list = []

    def add(self, human):
        self.humans_list.append(human)

    def add_many(self, human):
        self.humans_list.extend(human)

    def check_all_adult(self):
        for human in self.humans_list:
            human.check_adult()


humans = HumanManager()
humans.add_many([
    Human("Ruby", 30),
    Human("GO", 16),
    Human("Swift", 11),
    Human("Python", 34),
    Human("C", 53),
])
humans.check_all_adult()


