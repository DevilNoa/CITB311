# print("Hello World") # ред 1
from cmath import pi

# 4/8 ред
# print(2+2)
# print(34287+2348972)
# print(1/2)
# print(1//2)
# print(1.0//2.0)

# print(1000000000000000000 / 2)  # ред 10

# print(0xAF)  # ред 12

# print(0o10)  # ред 14

# x = 3
# x = x * 2
# print(x)  # 16/18

# input("the meaning of life")
#  # чете от конолата след текста
# print("But what is the question then ")

# print(pow(2, 3))
# print(10 + pow(2, 3 * 5) / 3.0)
# print(abs(-10))  # 24/26


# import math
# print(math.floor(32.9))


# lec 2


# answer = 42
# question = "about the life, universe and everything"
#
# print("the answer of the question", question, "is", answer) #36/39

# a, b, c = 1, 2, 3
# print(a, b, c)
# a, c = c, a
# print(a, b, c)


# password = 123456
# if password == 123456:
#     print("welcome!")
# else:
#     print("wrong pass")  #47/51

# num=int(input('enter a number: '))
# if num>0:
#     print(num," The number is positive")
# elif num<0:
#     print("the number is negative")
# else:
#     print("the number is zero")  #53/59

# a = [1, 2, 3, 'four']
# b = [1, 2, 3]
# print(a == b)
# b.append('four')
# print(a == b)  # 62/65

# Ivan=['Ivan Andonov', 35]
# Toni=['Antoaneta petkova', 41]
# database = [Ivan , Toni]
# print(database)  #67/70

# greeting = "Hello"
# print(greeting[0], greeting[1], greeting[2], greeting[3], greeting[4])
# print(greeting[-1], greeting[-2], greeting[-3], greeting[-4], greeting[-5])
# print(greeting[-0],greeting[0])  #72/75

# tag = '<a href="http://www.python.org">Python web site</a>'
# print(tag[9:30])
# print(tag[32:-4])
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[7:10])
# print(numbers[-3:-1])  #Липсва стойността 10
# print(numbers[-3:0])  #Последователността е празна
# print(numbers[-3:]) #трикът е тук в :
# print(numbers[:3])
# print(numbers[:])  #можем да го използваме ако ни се налага да копираме списък
# ## 77/86

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[0:10:1])
# print(numbers[0:10:2])
# print(numbers[::4])
# print(numbers[8:3:-1])
# print(numbers[10:0:-2]) #89/94

# print([1,2,3]+[4,5,6])
# print('hello '+'world')
# #print([1,2,3+'world']) ако направим нещо такова ще ни изхвърли проблем #96/98

# print('pytone'*5)
# print([420]*10) #100/101

# sequence = [None]*10
# print(sequence)  #103/104
#  #ще излолзвам print("~~"*10) за разделяща линия
# permissions = 'rw'
# print('w' in permissions)
# print('x' in permissions)
# print("~~"*10)
# users = ['Ivan', 'Petkan', 'Dragan']
# students = ['Ivan', 'Petkan', 'Dragan']
# print('Stpyan' in users)
# print('Ivan' in users)
# print("~~"*10)
# mailSubject='buy cheap viagra now!!!'
# print('viagra' in mailSubject)  #106/116

# numbers = [100,34,678]
# print(len(numbers))  #дължина на редицата
# print(max(numbers))  #най-голямото число от редицата
# print(min(numbers))  #най-малкото число от редицата
# print("~~"*10)
# print(max(2,3))
# print(min(9,3,2,5))
# print("~~"*10)
# print(list('Hello'))  # създаване на списък от редица #118/126

# students = ['Ivan','Petkan', 'Dragan']
# print(students[0])
# students[0]='Stoyan'
# print(students[0])
# print(students)  #128/132

# subjects = ['summer vacation offer','your salary for september','report for new students ASAP']
# print(subjects)
# del subjects[2]
# print(subjects)  #134/137

# name = list ('Nikola Bukov')
# print(name)
# name[6:]=list('Schwarzenegger')
# print(name) #139/142

# a = [1,2,3]
# b=a
# print(a)
# print(b)
# print('~~'*10)
# a.append(4)
# print(a)
# print(b) # 144/151

# chores=['clean the blackboard','open the windows','throw the garbage']
# chores.append('close he door')
# print(chores) #153/155

# print(['to', 'bee', 'or', 'not', 'to', 'bee'].count('to'))
# print([[1, 2], 1, 1, [1, 2]].count(1))  #157/158

# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print(a)  #160/163
space = '~~' * 10
innovationRating = ['Sweden', 'Germany', 'Denmark', 'Finland', 'Netherlands', 'Luxembourg', 'Belgium', 'UK', 'Austria',
                    'Ireland', 'France', 'Slovenia', 'Cyprus', 'Estonia', 'Italy', 'Spain', 'Portugal',
                    'Chech republic', 'Greece', 'Slovakia', 'Hungary', 'Malta', 'Litva', 'Poland', 'Latvia', 'Romania',
                    'Bulgaria']
# print("Bulgaria is on ", innovationRating.index('Bulgaria')+1,'place from',len(innovationRating))

# numbers = [1, 2, 3, 5, 6, 7]
# print(numbers)
# print('~~' * 10)
# numbers.insert(3, 'four')
# print(numbers)  #168/172

# print(innovationRating)
# print('~~' * 10)
# innovationRating.pop()
# print(innovationRating)  # 174/177

# h = ['two', 'bee', 'or', 'not', 'two', 'bee']
# print(h)
# print(space)
# h.remove('bee')
# print(h)  #179/183

# print(innovationRating)
# print(space)
# innovationRating.reverse()
# print(innovationRating)  # 185/188

# c = ['Italy', 'Bulgaria', 'Spain', 'Germany', 'France']
# print(c)
# print(space)
# c.sort(key=len, reverse=True)
# print(c) #193/197

# print(tuple([1, 2, 3]))
# print(space)
# print(tuple(['a', 'b', 'c']))
# print(space)
# print(tuple((1, 2, 3)))  #199/203

# countries = ['Iran', 'Iraq', 'France', 'Belgium', 'Poland', 'Czech Republic', 'Chechnya']
# for c in countries:
#     print("We should offer our support to", c, '\n')
# print(space)
# for i in range(1, 5):
#     print(i)
# print(space)
# product = []
# s=input('Enter product name:')
# while s:
#     product.append(s)
#     s = input('Enter product name:')
# print(product)
# print(space)
# names = ['Sulyo', 'Pulyo', 'Atanas', 'As']
# ages = ['19', '21', '24', '30']
# for i in range(len(names)):
#     print(names[i], 'is', ages[i], 'yearss old')
# data = zip(names, ages)
# for n, a in data:
#     print(n, 'is', a, 'years old')
# numlist = [1, 2, 3, 4, 5, ]
# for num in numlist:
#     num = num * 2
#     print(numlist)
#     for index, num, in enumerate(numlist):
#         numlist[index] = numlist[index] * 2
#     print(numlist)

# txt = "Cheap aaa pictures and aaa videos!"
# text = txt.split(' ')  # Split the string on whitespace
# for index, string in enumerate(text):
#     if 'aaa' in string:
#         text[index] = '[stuff]'
# txt = " ".join(text)
# print(txt)

# from math import sqrt
#
# for n in range(99, 0, -1):
#     root = sqrt(n)
#     if root == int(root):
#         print(n)
#         break
#     else:
#         print("not found")

# print([x * 2 for x in range(10, 20)])
# print(space)
# print([x * 2 for x in range(10, 20) if x % 3 == 0])

# низове

#
# single1 = 'test'
# single2= "test"
# duble1= """test
# test
# test
# """
# print(single1)
# print(space)
# print(single2)
# print(space)
# print(duble1)

# formattetString = "hello i study %s in %s"
# values = ("computer science", "nbu ")
# print(formattetString %values)  #271/273

# print("the answer is %d" % 54)
# print("65536 is %x" % 65536)#275/276

# print("%10f" % pi )
# print(space)
# print("%10.2f" % pi )
# print(space)
# print("%.2f" % pi )
# print(space)
# print('%.5s'%'Albus Percival Wulfric Brian Dumbledore''Albus')


# from blist import blist
#
# items = blist([5, 6, 2])

# single = 'test 1'
# single2= "test 2"
# multy= """test
#           test
#           test"""
# print(single)
# print(space)
# print(single2)
# print(space)
# print(multy)

# formattedString = "Hi ! i study %s in %s"
# values = ("computer sience" , "nbu")
# print(formattedString % values)

# print("the answer is %d" % 43)
# print(space)
# print( "65536 in HEX is %x" % 65536)

# print("%10f" % pi)
# print ("%10.2f" % pi)
# print ("%.2f" % pi)

# print ("%+5d" % 10)
# print ("%+5d" % -10)

