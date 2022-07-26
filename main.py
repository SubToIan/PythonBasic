# list1=[1,2,3,4,5]
# print (list1)

# list=['안녕', '친구들', '만나서', '반가워']
# print (list[2:4])

# list= [1, 5, 3, 6]
# print (list[1:3])
# print (list[2:])
# print(list[:2])

# list=[1,5,3,6]
# length=len(list)
# print (length)

# a=[1,2,3]
# b=[4,5,6]
# print(a+b)
# a=[1,2,3]
# print(a*3)

# rainbow=['red', 'orange', 'yellow', 'green','blue', 'indigo', 'purple']
# first=rainbow[0]
# print(f'무지게의 첫번째 색은 {first}이다')
# last=rainbow[6]
# print(f'무지게의 첫번째 색은 {last}이다')

# animal=['강아지', '고양이', '새', '코끼리', '곰']
# plant=['소나무', '단풍나무', '장미꽃', '벚꽃']
# 생물=plant+animal
# print(생물)

# animal=['강아지', '고양이', '새', '코끼리', '곰']
# animal.append('사람')
# print (animal)

# animal=['강아지', '고양이', '새', '코끼리', '곰']
# animal.insert(3,'돼지')
# print(animal)

# animal=['강아지', '고양이', '새', '코끼리', '곰']
# animal.remove ('새')
# animal.insert(2,'참새')
# print (animal)

# animal=['강아지', '고양이', '새', '코끼리', '곰']
# del animal[1]
# print (animal)

# animal=['강아지', '고양이', '새', '코끼리', '곰']
# animal.remove('고양이')
# print (animal)

# t=(1,2,3,4,5,6,7,8,9,10)
# t2=(t*10)
# print(t2)
# print (len(t2))

# animal=('강아지', '고양이', '새', '코끼리', '곰')
# del animal[1]
# print (animal)

# list= []
# 영화=['보스베이비', '어벤져스','찰리와 초콜릿 공장','슈퍼배드']
# 영화.append('겨울왕국2')
# print (영화)
# 영화.insert(4,'겨울왕국')
# print(영화)
# del 영화[1]
# print(영화)
# 영화.remove ('찰리와 초콜릿 공장')
# print(영화)

# lan1=['C','C++','JAVA']
# lan2=['Python',"Go","C#"]
# lan=lan1+lan2
# print (lan)

# tuple=()
# t=1,2,3
# t[0]='a'


# while True:
#     data=int(input("1,2,3을 입력해주세요"))
#     t=('가위','바위','보')
#     if data==1:
#         print (t[0])
#     elif data==2:
#         print (t[1])
#     elif data==3:
#         print (t[2])
#     else:
#         break
    # print(t[data-1])

# t=('가위','바위','보')
# while True:
#     data=input("1,2,3을 입력해주세요")
#     if data==-1:
#         break
# total=[]
# while True:
#     food=input("무엇을 좋아하나요?")
#     if food=="-1":
#         break
#     total.append (food)
#     print (total)

# total=[]
# while True:
#     score=input("점수:")
#     if score=="-1":
#         break
#     total.append (score)
#     print (total)
# while True:
#     score=int(input("시험점수:"))
#     if score>80:
#         print("A, 상장:https://progaming.monster/image.php?id=0M5EXX.png")
#     elif score>60: # score<=80 and score>60:
#         print("B, 상장:https://progaming.monster/image.php?id=0M5EXX.png")
#     elif score>40: # score<=60 and score>40:
#         print("C, 상장:https://progaming.monster/image.php?id=0M5EXX.png")
#     elif score<=40 and score>20:
#         print("D상장:https://progaming.monster/image.php?id=0M5EXX.png")
#     elif score<20 and score>0:
#         print("F, 상장:https://progaming.monster/image.php?id=0M5EXX.png")
#     elif score==-1:
#         break
#     else:
#         print("???")
# holder=[]
# rank=("A","B","C","D","F")
# while True:
#     score=int(input("시험점수:"))
#     holder.append(score)
#     if score==-1:
#         break
#     elif score>80 and score<101:
#         print(rank[0])
#         print (holder)
#     elif score>60: # score<=80 and score>60:
#         print(rank[1])
#         print (holder)
#     elif score>40: # score<=60 and score>40:
#         print(rank[2])
#         print (holder)
#     elif score<=40 and score>=20:
#         print(rank[3])
#         print (holder)
#     elif score<20 and score>0:
#         print(rank[4])
#         print (holder)
#     else:
#         print("???")

# a={2,1,3,5,7}
# b={3,4,1,6}
# print (b-a)
# print(a&b)
# print (a|b)
# print(a-b)

# s1=set([1,2,3])
# s1.add(4)
# print(s1)

# s1=set([1,2,3])
# s1.update([4,5,6])
# print (s1)

# s1=set([1,2,3])
# s1.remove(2)
# print(s1)

s1=set([1,2,3])
l1=list(s1)
print(l1)
print (l1[0])

s1=set([1,2,3])
t1=tuple(s1)
print(t1)
print (t1[0])