class User:
    active_users = 0



    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
        #self.__name = "Hello"  #_name private attribute
                               #__name real private
    def full_name(self):
        return self.first + " " + self.last

    def likes(self, obj):
        return f'{self.first} likes {obj}'


user1 = User("David","Lu",28)
user2 = User("Leo","Chen",32)

print(User.active_users,id(User.active_users))
print(user1.active_users,id(user1.active_users))
print(user2.active_users,id(user2.active_users))

user1.active_users = 300
print("------------------")

print(User.active_users,id(User.active_users))
print(user1.active_users,id(user1.active_users))
print(user2.active_users,id(user2.active_users))

user1.sex = 'man'
print(user1.sex)
#Daivd like Woman
