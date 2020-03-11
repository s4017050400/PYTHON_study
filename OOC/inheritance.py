class Aquatic:
    def __init__(self, name):
        self.name = name
    def swim(self):
        return f"{self.name} is swimming"
    def greet(self):
        return f"I am {self.name} of the sea!"

class Ambulatory:
    def __init__(self, name):
        self.name = name
    def walk(self):
        return f"{self.name} is walking"
    def greet(self):
        return f"I am {self.name} of the land"


class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        super().__init__(name = name)


a_penguin = Penguin("hello")

print(a_penguin.swim())
print(a_penguin.walk())

