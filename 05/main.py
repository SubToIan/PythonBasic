
# num1=input("숫자 1?")
# num2=input("숫자 2?")
# num3=input("숫자 3?")

# if num1>num2 and num1>num3:
#     print ("숫자 1 이 가장 크다")
# elif num2>num1 and num2>num3:
#     print ("숫자 2 이 가장 크다")
# elif num1==num2 and num2==num3:
#     print ("모든 수가 다 같다")
# else:
#     print("숫자 3이 가장 크다")

 
 
 
 
 
# hit = 0
# while hit<10:
#     hit = hit+1
#     print(f'나무를 {hit}번 찍었습니다')
#     if hit==8:
#         print("나무가 곧 너머갈것같다")
#     elif hit==3:
#      print("나무가 흔들린다")

# print("나무가 너머갔습니다")





# number=0
# while number!=100:
#     print("100=종료")
#     number=int(input())


# number=0
# while number < 10:
#     number=number+1
#     print(number)

# number=1
# while number <= 10:
#     print(number)
#     number=number+1

# while 3<5:
#     print("a")
# if 3<5:
#     print("B")


# number=int(input("숫자1 은?"))
# numbar=int(input("숫자2 는?"))
# while number<=numbar:
#         print (number)
#         number=number+1
    
# for number in range(1, 13, 1):
#     print (f"{number}월")

# for i in range(4):
    # print('Hi')

# number=int(input("숫자1?"))
# nunnber=int(input("숫자2?"))
# for number in range(number,nunnber+1, 1):
#     print(number)

# number=int(input("숫자1?"))
# nunnber=int(input("숫자2?"))
# for number in range(number-1,nunnber, 3):
#     print(number)

# for i in range(1,7,1):
#    print(i)
#    print("-"*7)


# for 단 in range (2,10,1):
#     for i in range(1,10):
#         string=f'{단}x{i}={단*i}'
#         print (string)

# for i in range(4):
#     if i==2:
#         continue
#     print (i)

# for i in range(4):
#     if i==2:
#         break
#     print (i)

# def f():
#     pass

# while True:
#     점수= int(input("시험점수는?"))
#     if 점수<0:
#         break
#     elif 점수>60:
#         print("합격")
#     else:
#         print("불합격")
# gkj=int(input('숫자입력'))
# for i in range(1,gkj+1):
#     print ("*"*i)


while True:
    hga=int(input("숫자입력"))
    hga%7
    if hga < 0 :
        break
    elif hga%7>0:
        print("배수가 아니다")
    elif hga%7==0:
        print("배수다")
    
