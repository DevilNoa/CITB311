# print("Hello World") # ред 1

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

numbers = [100,34,678]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print("~~"*10)
print(max(2,3))
print(min(9,3,2,5))
print("~~"*10)
print(list('Hello'))  # създаване на списък от редица #118/126
