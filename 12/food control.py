import random
rng=random.randint(1,5)
menus=[]

f=open('foodlist.txt','r',encoding="UTF-8")
for line in f.readlines():
    menus.append(line.rstrip())
f.close
title= """1. 메뉴추가
2. 메뉴 삭제
3. 메뉴 보기
4. 메뉴 추천
5. 종료"""




while True:
    print (title)
    try:
        choice=int (input(""))
    except ValueError:
        print ("1-5까지의 숫자를 입력해주세요")
        continue
    if choice==1:
        add_menu=input("추가하고 싶은 메뉴의 이름을 입력해주세요")
        menus.append(add_menu)
        print (menus)
        print (f'{add_menu}이 성공정으로 추가됐습니다.')
    elif choice==2:
        delete_menu=input("삭제하고 싶은 메뉴의 이름을 입력해주세요")
        menus.remove(delete_menu)
        print (menus)
        print (f'{add_menu}이 성공정으로 삭제됐습니다.')
    elif choice==3:
        print(menus)
    elif choice==4:
        if rng<=4:
            print("메그넘을 추천합니다")
        else:
            a=random.randint(0, len(menus))
            print(f'{menus[a]}을 추천합니다')

    elif choice==5:
        f=open('foodlist.txt','w',encoding="UTF-8")
        for menu in menus:
            f.write(menu+"\n")
        f.close()
        break
    else:
        print ("1-5까지의 숫자를 입력해주세요")