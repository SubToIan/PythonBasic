age=13
print(age)
a='Hello Python!'
b="Hello Python"
c='''Hello Python'''
a='Hello Python!\nHelloJavascript'
print(a)
#오류
# a='Hello Python!
# Hello Javascript!'
#오류해결
a='''Hello Python!
Hello Javascript!'''
b="""Hello Python!"""
print(a)
print(b)
print('a\nb\tc\'d\"e\\')
head='오늘 날씨는'
tail=' 맑음'
print(head+tail)
print('='*50)
print('My Program')
print('='*50)
s1="python"
s2="java"
print((s1+' '+s2+" ")*4)
hello='Hello!'
a= hello[4]
print(a)
b=hello[-2]
print(b)
s= 'Life is too short, you need Python'
a= s[0]
b=s[8]
c=s[2]
d=s[9]
e=s[19]
f=s[28]
g=s[-17]
print(a, b, c, d, e, f, g)
t_index=s.find('t')
d=s[t_index:t_index+3]
print(d)
h=s[8:11]
print(h)
v=s[-6:]
print(v)
v=s[:]
print(v)
year1=2022
year2='2022'
# print(year1[0])
print(year2[0])#실행
a=3
b=4
print(a+b)
a='3'
b='4'
print(a+b)
sentence= "나는 사탕{0}개를 먹었다";
print(sentence.format(5000))
print(sentence.format(10000))
print(sentence.format(100000))

#---------------------------------------------------------------

name='홍길동'
age=13
print("당신의 이름은 {0}입니다. 올해 {1}살입니다.".format(name, age))
print("내년에 {0}살입니다".format(age+1))
print("당신의 이름은 {}입니다. 올해 {}살입니다.".format(name, age))

print(f'당신의 이름은 {name}입니다. 올해 {age}살입니다.')
number="14가 1234"
print(number[4:])
date='2022-07-14'
year=(date[0:4])
month=(date[5:7])
day=(date[-2:])
print(f'{year}년 {month}월 {day}일')

Typer= input('사과의 개수는?')
print(Typer)
name=input('당신의 이름은?')
print(f'반갑습니다{name}님')
ssid=input('당신의 ssid는')
print(f'해킹당했습니다')
ccd=input('1+1은?')
print("아닙니다")
ccd=int(ccd)
print(ccd+1)
print(f'{year}년 {month}월 {day}일')






date=input('aaaa')
year=(date[0:4])
month=(date[5:7])
day=(date[-2:])
print(f'{year}년 {month}월 {day}일')