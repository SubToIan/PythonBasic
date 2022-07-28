def print_command():
    print('''1. Add Ice Cream
2. Adjust Ice Cream Price
3. Delete Ice Cream
4. Print Ice Cream
5. Exit''')
ice={'tilamook': 4.34, 'magnum': 4.08, 'bluebell': 8.49, 'ben&jerry':5.49, "edy's/dreyer's":10.74}
def print_ice():
    print ("*"*80)
    # for key in ice.keys():
    #     print(f'{key}:{ice[key]}')
    for key, value in ice.items():
        print(f'{key}:{value}')
    print ("*"*80)

while True:
    print_command()
    command=input('Choose an option.')
    if command=='1':
        print ("Which Ice Cream do you wish to add?")
        add_ice=input("Enter the name of ice cream you want to add")
        add_price=input("Enter the price of the ice cream")
        ice[add_ice]=add_price
        print (ice)
    elif command=='2':
        print("Which Ice Cream would you like to adjust?")
        print_ice()
        adjust_ice=input("Enter the name of the Ice Cream you want to change.")
        adjust_amount=input(f"Enter the new price you want for {adjust_ice}")
        ice[adjust_ice]=adjust_amount
    elif command=='3':
        ice_del=input("Enter the name of the Ice Cream you want to delete.")
        del ice[ice_del]
        print(f'Successfully deleted {ice_del}')
    elif command=='4':
        print_ice()
    elif command=='5':
        confirm=input("Are you sure you want to exit?")
        if confirm=='yes' or confirm=='Yes':
            break
        else:
            print ("Aborted")