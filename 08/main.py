# a= {1:'a'}
# a[2]='b'
# print (a)
# a["name"]='홍길동'
# print (a)
# a['key']=[1,2,3]
# print (a) 
# a["name"]='성춘향'
# print(a)
# del a[1]
# print (a)
# print (a['name'])
# print(a[2])

# dic={'name':'a', 'age':-1, 'gender': 'unknown', 'birthday': 'not born'}
# print (dic)




# ic={'tilamook': 4.34, 'magnum': 4.08, 'bluebell': 8.49}
# print(ic)
# ic['edy\'s/dreyer\'s']=10.74
# print (ic)
# ic["ben&jerry"]=5.49
# print (ic)
# print("ben&jerry price:", ic['ben&jerry'])

# ic["edy\'s/dreyer\'s"]=10.74*0.9
# print (ic)
# del ic["magnum"]
# print (ic)

# def print_command():
#     print('''1. Add Ice Cream
# 2. Adjust Ice Cream Price
# 3. Delete Ice Cream
# 4. Print Ice Cream
# 5. Exit''')
# ice={'tilamook': 4.34, 'magnum': 4.08, 'bluebell': 8.49, 'ben&jerry':5.49, "edy's/dreyer's":10.74}
# def print_ice():
#     print ("*"*80)
#     # for key in ice.keys():
#     #     print(f'{key}:{ice[key]}')
#     for key, value in ice.items():
#         print(f'{key}:{value}')
#     print ("*"*80)

# while True:
#     print_command()
#     command=input('Choose an option.')
#     if command=='1':
#         print ("Which Ice Cream do you wish to add?")
#         add_ice=input("Enter the name of ice cream you want to add")
#         add_price=input("Enter the price of the ice cream")
#         ice[add_ice]=add_price
#         print (ice)
#     elif command=='2':
#         print("Which Ice Cream would you like to adjust?")
#         print_ice()
#         adjust_ice=input("Enter the name of the Ice Cream you want to change.")
#         adjust_amount=input(f"Enter the new price you want for {adjust_ice}")
#         ice[adjust_ice]=adjust_amount
#     elif command=='3':
#         ice_del=input("Enter the name of the Ice Cream you want to delete.")
#         del ice[ice_del]
#         print(f'Successfully deleted {ice_del}')
#     elif command=='4':
#         print_ice()
#     elif command=='5':
#         confirm=input("Are you sure you want to exit?")
#         if confirm=='yes' or confirm=='Yes':
#             break
#         else:
#             print ("Aborted")

# scores=[90,25,67,45,80,1,1,1,1,1,1]
# number=0
# for score in scores:
#     number=number+1
#     if score>=60:
#         print(f'{number}번학생은 합격입니다')
#     else:
#         print(f"{number}학생은 불학격입니다")


# menus= ['ㄱㅂ','ㄹㅁ','ㅌㄱ']
# for menu in menus:
#     print(f'오늘밥은 {menu}이다')

# numbers=[3,-20,-3,44,-100,0,358]
# for number in numbers:
#     if number<0:
#         print ("음수")
#     else:
#         print("양수")
# a=100
# while a<104:
#     print (a)
#     print("------------------")
#     a=a+1

# for i in range(100,104,1):
#     print(i)
#     print("-------")

list=[100,101,102,103]
for number in list:
    print (number)
    print("-------")