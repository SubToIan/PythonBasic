# date=input('오늘날짜:')
# year=date[0:4]
# month=date[5:7]
# day=date[-2:]
# print (f'{year}년 {month}월 {day}일2022')

from operator import truth


def 시리얼먹기():
    print("준비물을 준비합니다.")
    print("우유를 그릇에 따릅니다")
    print("시리얼을 그릇에 넣습니다")
    print("숟가락으로 시리얼과 우유를 떠서먹습니다")

시리얼먹기()
시리얼먹기()
시리얼먹기()
시리얼먹기()
시리얼먹기()

def 시리얼먹기(우유, 시리얼, 그릇, 숟가락):
    # print("준비물을 준비합니다.")
    print(f'"{우유}를 따릅니다"')
    print(f'"{시리얼}을 {그릇}에 넣습니다"')
    print(f'"{숟가락}으로 {시리얼}과 {우유}를 떠서먹습니다"')


시리얼먹기('매일우유', '코코볼', '일회용그릇', '플라스틱숟가락')
시리얼먹기('그냥우유', '아무 시리얼', '초거대그릇','초거대 플래티넘 숟가락')
    


def 시리얼공장(우유, 시리얼, 그릇, 숟가락):
    # print("준비물을 준비합니다.")
    print(f'"{우유}를 따릅니다"')
    print(f'"{시리얼}을 {그릇}에 넣습니다"')
    print(f'"{숟가락}으로 {시리얼}과 {우유}를 떠서먹습니다"')
    return f"{우유}5.87억gallons, {시리얼} 9382천만 톤 남았습니다"

시리얼공장('매일우유', '코코볼', '일회용그릇', '플라스틱숟가락')
시리얼공장('그냥우유', '아무 시리얼', '초거대그릇','초거대 플래티넘 숟가락')

결과 = 시리얼공장("그냥우유", "아무 시리얼", "초거대그릇","초거대 플래티넘 숟가락")

print(결과)


def add(a, b):
    return a+b


a=4
b=4
c=add(a, b)
print (c)
print(add(10, 15))
print(add(2345889, 194943))
print(add(3, 1000000000000000000000000000000000000000000000))




def say1(name):
    string= '안녕하세요?' + name + '님'
    return string

name= "홍길동"
print(say1(name))

def say2(name):
    string= '안녕하세요?' + name + '님'
    print (string)


def add(a,b):
    결과= a+b
    print(f'{a} + {b} = {결과}')

add(10,5)
    



def smile(a):
    string= a +" :D"
    print(string)

smile("hi")
smile("window")

var='전역'

print(var)

def scope():
    global var
    var= '글로벌'
    print(var)

scope()




global_var= '글로벌'

def scope():
    local_var='지역'
    print(global_var)
    print(local_var)

scope()

print(global_var)
# print(local_var)




print('='*100)
var='전역'
print (var) #전역
def scope():
    var='지역'  
    print(var) #지역

scope()

print (var)#전역