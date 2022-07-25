import random
life=3
def add(a, b):
    return a+b
while True:
    num1=random.randint(0,100)
    num2=random.randint(0,100)
    print(f'{num1}과 {num2}를 더하세요')


    answer=int(input("정답은?"))
    actual=add(num1,num2)
    if answer==actual:
        print("정답!")
    else:
        life=life-1
        print(f"틀렸습니다,{life}명의 가족이 남았습니다.")
    if life==0:
        print("당신의 주소는 이미 노출되었고 조금있으면 죽이러 찾아옵니다")
        break
