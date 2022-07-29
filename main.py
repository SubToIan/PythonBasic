

# year=2002
# while True:
#     print (year)
#     year=year+4
#     if year>2050:
#         break

# for year in range(2022,2051,4):
#     print (year)




# class Dog:
#     name="cosmic doge"
#     age="∞"
#     def bark(self):
#         print(f"{self.name} 왈")

#     def move(self):
#         print('움직인다')
    
# cosmic_doge=Dog()
# cosmic_doge2=Dog()
# cosmic_doge3=Dog()
# cosmic_doge4=Dog()
# cosmic_doge5=Dog()
# cosmic_doge6=Dog()
# cosmic_doge7=Dog()
# cosmic_doge8=Dog()
# cosmic_doge9=Dog()
# cosmic_doge10=Dog()
# cosmic_doge11=Dog()


# cosmic_doge.bark()
# cosmic_doge.move()
# print(type(cosmic_doge))
# while True:
#     cosmic_doge5.bark()

# cosmic_doge2.name="cosmic_doggo"
# cosmic_doge2.age="∞+1"
# cosmic_doge2.weight="비만"
# print(cosmic_doge.name, cosmic_doge.age)
# print(cosmic_doge2.name, cosmic_doge2.age, cosmic_doge2.weight)

# cosmic_doge.bark()
# cosmic_doge2.bark()

# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
   
#     def bark(self):
#         print(f"{self.name} 왈")

#     def move(self):
#         print('움직인다')
    
    
# cosmic_doggo=Dog("Cosmic Doggo", "∞")
# cosmic_doggo2=Dog("Cosmic Doge", "∞+1")
# print (cosmic_doggo.name, cosmic_doggo.age)
# print (cosmic_doggo2.name, cosmic_doggo2.age)
# cosmic_doggo.bark()

# class Dog:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
   
#     def bark(self):
#         print(f"{self.name} 왈")

#     def move(self):
#         print('움직인다')

#     def __str__(self):
#         sentence= f'Name:{self.name} Age:{self.age}'
#         return sentence


# cosmic_doggo=Dog('Cosmic Doggo', "∞")
# cosmic_doge=Dog("Cosmic Doge", "∞")
# print(cosmic_doggo)
# print(cosmic_doge)

# a=10
# print(type(a))
# b="10"
# print(type(b))
# c=[10]
# print(type(c))

# def func(x):
#     return x+1
# print(type(func))

# class Cat:
#     def __init__(self,age,name):
#         self.name=name
#         self.age=age

#     def meow(self):
#         print("냐옹")

#     def scratch(self):
#         print("고양이가 할퀴었다. 아프다.")


# Nyan_Cat=Cat("∞", "Nyan Cat")
# print (Nyan_Cat.meow)
# print (Nyan_Cat.name, Nyan_Cat.age)

class Human():
    def __init__(self,nickname,id,gender,email,phone_number):
        self.nickname=nickname
        self.id=id
        self.gender=gender
        self.email=email
        self.phone_number=phone_number
    
    def profile(self):
        print(f'{self.nickname},\n{self.id}, \n{self.gender}, \n{self.email}')
    def chat(self, message):
        print (f'{self.nickname} : {message}')

    
hu_man=Human("ALPHADA","whalecoding","Female","whalecoding@gmail.com","123-4567-8910")
# hu_man.profile()
hu_man.chat("hi")
hu_man2=Human("철수", "remorsefuleager","Male","HoodSaber@gmail.com","865-0217-4088")
# hu_man2.profile()
hu_man2.chat("If any cop asks you where you were, just say you were visiting Kansas.")
hu_man.chat("There are over 500 starfish in the bathroom drawer.")
hu_man2.chat("She was too busy always talking about what she wanted to do to actually do any of it.")
hu_man.chat("He created a pig burger out of beef.")