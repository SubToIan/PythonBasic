# def operation(a,b):
#     add(a,b)
#     multiply(a, b)
#     divide(a, b)
#     subtract(a, b)


# def add(a,b):
#     c = a+b
#     print(f'{a} + {b} = {c}')

# add(2, 3)

# def subtract(a,b):
#     c = a-b
#     print(f'{a} - {b} = {c}')

# def divide(a,b):
#     c = a/b
#     print(f'{a} ÷ {b} = {c}')

# def multiply(a,b):
#     c = a*b
#     print(f'{a} x {b} = {c}')

# add(2, 3)
# subtract(3, 2)
# divide(6, 2)
# multiply(5, 4)

# operation(3, 7)

# a= int(input("당신이 가지고있는 사과의 수는?"))

# if a==3:
#     print ("먹는다")
# else:
#     print ("안먹어")

# money= int(input("돈이 얼마있습니까?"))

# if money>=10000:
#     print ("택시")
# else:
#     print ("안타")

# y=3
# x=4

# print(x>y)
# print(x<y)
# print(x==y)
# print(x!=y)
# print(x>=y)
# print(x<=y)

# 등수= int(input('몇등입니까?'))

# if 등수==1:
#     print("소파행")
# else:
#     print("매우 축하드립니다, 설거지에 당첨!")

# def checkWeather(weather):
#     if weather== '비' or weather== '우박' or weather== '눈' or weather== '토네이도':
#         return True
#     else:
#         return False

# money = int(input("가지고있는 $:"))
# distance= int(input("목적지와의 km 거리:"))
# weather=input("날씨:")

# if money>=10 and distance>=100 and checkWeather(weather):
#     print(""" _____  _    __  _____ 
# |_   _|/ \   \ \/ /_ _|
#   | | / _ \   \  / | | 
#   | |/ ___ \  /  \ | | 
#   |_/_/   \_\/_/\_\___|""")
# else:
#     print("""__        ___    _     _  __
# \ \      / / \  | |   | |/ /
#  \ \ /\ / / _ \ | |   | ' / 
#   \ V  V / ___ \| |___| . \ 
#    \_/\_/_/   \_\_____|_|\_\\
#                             """)


# grade = int(input("당신은 몇학년인가요?"))

# if grade==1 or grade==5:
#     print("김밥")
# else:
#     print("햄버거")

# pizza= input('피자가게가 열었나요?')
# chicken= input('치킨가게가 문을 열었나요?')
# cereal= input('시리얼박스가 문을 열었나요?')
# if pizza=='예':
#     print("피자 ㄱㄱ")
# elif chicken=='예'or chicken=="열었습니다":
#     print("치킨먹자")
# elif cereal=='예':
#     print("저녁은 시리얼")
# else:
#     print ("안먹어")
score=int(input("시험점수:"))
if score>80:
    print("A, 상장:https://progaming.monster/image.php?id=0M5EXX.png")
elif score>60: # score<=80 and score>60:
    print("B, 상장:https://progaming.monster/image.php?id=0M5EXX.png")
elif score>40: # score<=60 and score>40:
    print("C, 상장:https://progaming.monster/image.php?id=0M5EXX.png")
elif score<=40 and score>20:
    print("D상장:https://progaming.monster/image.php?id=0M5EXX.png")
else:
    print("F, 상장:https://progaming.monster/image.php?id=0M5EXX.png")