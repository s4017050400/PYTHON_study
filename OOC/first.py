class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        self.__name = "Hello"  #_name private attribute
                               #__name real private
    def full_name(self):
        return self.first + " " + self.last


x = User("David","Lu",28)

print(x.full_name())
