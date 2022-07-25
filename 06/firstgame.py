import random
while True:
    start = input("게임을 시작합니다. 종료를 원하면 x를 입력하세요(o/x)")
    if start=="x":
        break
    com=random.randint(0,100)
    min=0
    max=100
    a=0
    print ("0-100까지의 숫자 입력")
    while True:
        user= input('숫자는?')
        if not user.lstrip('-').isdecimal():
            print("숫자를 입력해주세요")
            continue
        
        user=int(user)
        a=a+1
        if user>100 or user<0: print("0-100의 숫자를 입력해주세요")
        elif user>com:
            max=user-1
            print (f"선택한 숫자보다 낮습니다,{a}번 시도했습니다.{min}부터 {max}의 숫자를 선택해주세요")
        elif user<com:
            min=user+1
            print(f"선택한 숫자보다 높습니다,{a}번 시도했습니다.{min}부터 {max}의 숫자를 선택해주세요")
        else:  
            print (f"정답!{a}번만에 맞췄습니다")
            break
            

while True:
    pass