import random
points=0
lose="패배 𝐻𝑎 𝐻𝑎 𝐻𝑎 𝐻𝑎 𝐻𝑎, 정말 초보로군"
win='승리!'
draw="비겼습니다"
rps_dic = {1:"가위", 2:"바위",3:"보"}
while True:
    cpu=random.randint(1,3)
    player=input("가위, 바위, 보")

    print(f'{player} vs {rps_dic[cpu]}')





    if player=="가위":
        if cpu==1:
            print(draw)
        elif cpu==2:
            print(lose)
            points=points-1
        else:
            print(win)
            points=points+1
    elif player=="바위":
        if cpu==1:
            print(win)
            points=points+1
        elif cpu==2:
            print(draw)
        else:
            print(lose)
            points=points-1
    elif player=="보":
        if cpu==1:
            print(lose)
            points=points-1
        elif cpu==2:
            print(win)
            points=points+1
        else:
            print(draw)
    else:
        print("안냈으니 졌습니다.𝐻𝑎 𝐻𝑎 𝐻𝑎 𝐻𝑎 𝐻𝑎, 정말 초보로군")
        points=points-1

    print(f'현재 점수: {points}점.')