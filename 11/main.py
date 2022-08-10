# s=5
# g=10
# v=15

# def sol(price, grade):
#     answer=0
#     if grade=="s":
#         answer=(price*(100-s)/100)
#     if grade=="g":
#         answer=(price*(100-g)/100)
#     if grade=="v":
#         answer=(price*(100-v)/100)
#     return answer

# price1=2500
# grade1="v"
# ret1=sol(price1,grade1)
# print (ret1)

# price2=96900
# grade2="s"
# ret2=sol(price2,grade2)
# print(ret2)

# class Animal:
#     def eat(self):
#         print('먹는다')
#     def move(self):
#         print('''           __
#       (___()'`;
#       /,    /`
#       \\"--\\''')

# class Dog(Animal):
#     def bark(self):
#         print('''  __      _
# o'')}____//
#  `_/      )
#  (_(_/-(_/''')
#     def shake(self):
#         print('''  __    __
# o-''))_____\\
# "--__/ * * * )
# c_c__/-c____/''')


# dog=Dog()
# dog.move()
# dog.eat()
# dog.bark()
# dog.shake()

class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def eat(self):
        print('먹는다')
    def move(self):
        print('움직인다')


class Dog(Animal):
    def __init__(self,name,age,owner):
        super().__init__(name,age)
        self.owner=owner
    def move(self):
        print('''           __
      (___()'`;
      /,    /`
      \\"--\\''')
    def bark(self):
        print('''  __      _
o'')}____//
 `_/      )
 (_(_/-(_/''')
    def shake(self):
        print('''  __    __
o-''))_____\\
"--__/ * * * )
c_c__/-c____/''')
    def __str__(self):
        sentence=f"Name:{self.name}, Age:{self.age} Owner:{self.owner}"
        return sentence
class Tiger(Animal):
    def __init__(self,name,age, stripes):
        super().__init__(name,age)
        self.striples=stripes

    def attack(self):
        print('''                                                                                        
                                                                                        
  ░░            ░░      ░░            ░░      ░░            ░░                    ░░    
                                                                                        
                                                                                        
  ░░    ░░    ░░░░  ░░░░░░    ░░░░  ░░░░  ░░░░░░    ░░  ████░░░░  ████    ░░    ░░░░    
  ░░            ░░      ░░            ░░      ░░        ██  ██████  ██            ░░    
                                                      ██░░░░░░░░░░██                    
                              ██████████████      ████░░░░░░░░░░░░░░██                  
░░  ░░░░░░  ░░    ░░      ░░██░░██░░██░░██░░██████░░░░░░░░██░░░░██░░██░░░░░░  ░░    ░░  
        ░░                ██░░░░██░░██░░██░░██░░██░░██░░░░░░░░░░░░░░██    ░░            
                        ████░░░░██░░██░░██░░██░░██░░░░██░░░░  ████████                  
                        ██░░██░░░░░░██░░██░░░░░░██░░░░░░░░░░    ████                    
  ░░    ░░      ░░      ██████░░░░██░░░░██░░░░░░░░░░██░░░░██      ██      ░░      ░░    
                        ██░░████░░░░░░░░░░░░░░██░░░░██░░░░░░██████                      
                        ██████  ██░░██░░░░░░██      ██░░██░░░░██                        
                        ██░░██  ████░░░░░░██  ██████████░░░░████                        
                      ██░░██    ████░░░░██    ░░  ██░░░░██░░░░██                        
                    ██░░██      ██░░░░██          ██░░██  ██░░██                        
                    ████      ██░░░░██░░██        ██████  ██████                        
                              ██░░██░░░░░░██      ██░░██  ██░░██                        
                              ██░░░░████  ██    ██░░░░██  ██    ██                      
                                ██    ██████    ██    ██    ████                        
                                  ████            ████                                  
                                                                                        
                                                                  ░░                    
                                                                                        
                                                                                        
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

''')

tiger=Tiger("Uguveuyveuyhefuig osas sr",53835193549254926492549318,9999999999999999999999)
tiger.attack()
tiger.move()
    
    
    
    
# dog = Dog('qwephg',53835193549254926492549264,'Uguveuyveuyhefuig osas')
# print(dog)
# a_n_i_m_a_l=Animal('Uguveuyveuyhefuig osas jr',53835193549254926492549210)
# a_n_i_m_a_l.move()