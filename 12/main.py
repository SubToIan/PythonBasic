try:
    int('hi')
except:
    print ("aaaaaa")
try:
    a=[1,2]
    print (a[3])
    4/0
except ZeroDivisionError:
    print("hi")
except IndexError:
    print("trf")

try:
    int('qwerty')
except ValueError as e:
    print (e)
