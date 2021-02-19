# print('hello world')
# name = 'Tom'
# age = 50
# is_male = False

# phrase = 'nicky variable'
# print(phrase.replace('nicky', 'new'))

# print(phrase.index('var'))
# print(phrase.upper())
# print(phrase.lower().islower())

# print(3 * (4+5))
# print(10 % 3)
# my_num = 5
# my_num_as_str = str(my_num)
# print(my_num_as_str + ' is a string')
# neg_num = -5
# print(abs(neg_num))
# square = pow(5,2)
# print(square)
# nums = [1, 2, 3, 4, 5]
# print(max(nums))

# from math import *
# float = 3.7
# print(floor(float))
# print(ceil(float))
# print(sqrt(float))

# name = input("Enter your name: ")
# age = input('enter your age: ')
# print('hello ' + name + '! You are: ' + age)

# num1 = float(input('Enter a number: '))
# num2 = input('Enter another number: ')
# result = num1 + float(num2)
# print(result)

# color = input('Enter a color: ')
# plural_noun = input('Enter a plural noun')
# celebrity = input('Enter a celebrity')
# print('Roses are ' + color)
# print(plural_noun + ' are blue')
# print('I love ' + celebrity)

# friends = ['jim', 'pam', 'dwight', 'andy', 'michael']
# print(friends[1:4])
# friends[1] = 'creed'
# print(friends)

# lucky_numbers = [4,5,6,7,8,9]
# friends = ['jim', 'pam', 'creed', 'pam', 'stanley', 'meredith']
# # friends.extend(lucky_numbers)
# friends.append('Toby')
# friends.insert(1, 'andy')
# friends.remove('stanley')
# # friends.clear()
# friends.pop()
# print(friends.index('pam'))
# print(friends.count('pam'))
# print(friends)
# friends.sort()
# print(friends)
# friends.reverse()
# print(friends)
# friends2 = friends.copy()
# print(friends2)

# list of tuples
# coords = [(4, 5, 6), (1, 2, 3), (7, 8, 9)]
# print(coords)

def say_hi():
    print('hello user')
say_hi()

def say_hi_params(name, age):
    print('hello ' + str(name) +'! You are: ' + str(age))
say_hi_params('nicky', 34)
say_hi_params('mike', 35)
