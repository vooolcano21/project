# spisok = ['a', 'ab', 'asdf']

# spisok.append('last')
# deleted = spisok.pop(0)
# spisok.insert(0, 'first')
# spisok[1] = 'abNEW'
# spisok.index('asdf')

# print(spisok, deleted)
# print(spisok.index('asdf'))
# spisok.reverse()
# print(spisok)

# students = {
# 	'alex': 250,
# 	'max': 227,
# 	'anna': 221,
# }

# print(students)
# print(students['alex'])
# students['marya'] = 234
# print(students)
# students.setdefault('kostya') # добавляет ключ с пустым значением
# print(students)
# students.pop('kostya')
# print(students)
# print(students.keys())

# key_list = list(students.keys())
# print(key_list)

# print(students.values())

# print('max' in students)
# print('kostya' not in students)


# a = ('alex', 22, True)

# print(a)
# print(type(a))
# print(a[0])
# print(a[0:3])

# b = list(a)
# print(b)
# c = tuple(b)
# print(c)

#####
# first_set = {'Alex', 'John', 'Georg', 'Alex'}
# print(type(first_set))
# print(first_set)
# print(len(first_set))

# first_set.add('Maxim')
# print(first_set)
# print('Maxim' in first_set)
# first_set.remove('Alex')
# print(first_set)
# first_set.clear()
# print(first_set)

# second_set = {'Anton', 'Tom', 'Anna', 'Alex'}

# third_set = first_set.union(second_set)
# print(third_set)

# fourth_set = first_set.intersection(second_set)
# print(fourth_set)

# fifth_set = first_set.difference(second_set)
# print(fifth_set)

# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}

# print(set1.issubset(set2))
# print(set2.issuperset(set1))
# print(set1[0]) # ERROR


# numbers = range(1, 25)

# newBegin = []
# newLast = []

# for each in numbers:
# 	newBegin.insert(0, each)
# 	newLast.append(each)

# print(newBegin)
# print(newLast)

# for each in numbers:
# 	if each % 2 == 0:
# 		print(f'{each} четное число')
# 	else:
# 		print(f'{each} нечетное число')

# numbers = [1, 2, 3, 4, 5]

# for x, item in enumerate(numbers):
# 	numbers[x] += 10
# x += 2
# print(x, item)
# 2 1
# 3 2
# 4 3
# 5 4
# 6 5
# print(numbers)

# for _ in range(1, 5):
# 	print('wo')

# some_tuple = (11, 'Alex', 3.14)

# for each in some_tuple:
# 	print(each)

# dictionary = {
# 	'sveta' : 67,
# 	'svera' : 41,
# 	'svgea' : 32,
# }

# print(dictionary)

# for each in dictionary.items():
# 	print(each)

# for each in dictionary.values():
# 	print(each)


# import time

# x = 0
# while True:
# 	x = x+x
# 	print(x)
# 	time.sleep(1)

# while x < 6:
# 	print(f'x равно {x}')
# 	x += 1
# 	time.sleep(0.5)
# else:
# 	print('Завершено')


#################

# def some(a, b, c):
# 	'''
# 	:param a: Комент
# 	'''
# 	return a + b + c

# help(some)

# a, *b, c = 14, 20, 2, 5, 7, 4

# print(a, b, c)

# s = [3, 12]
# print(list(range(*s)))

# def func(*args):
# 	print(sum(args)*0.06)

# func(1, 333, 555, 232, 4234) # 321.3

# def funk(**kwargs):
# 	print(kwargs)

# funk(a=1, b=2, c=3, d=4) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# def sq(x):
# 	return x**2

# a = [-2, -1, 4, 8 , 2]

# b = map(sq, a)
# print(b)

# c = list(map(sq, a))
# print(c)

# a = ['hello', 'honey']

# b = list(map(str.upper, a))
# print(b)

# age = [11, 20, 33, 18, 14, 12]

# def isAdalt(age):
# 	return age >= 18

# is_adalt = lambda age: age >= 18 # скрытый return

# fil = filter(is_adalt, age) # filter object at 0x00000178BC12AEF0>
# f = list(filter(is_adalt, age)) # [20, 33, 18]
# print(f)


# def tagMaker(func):
# 	def wrapper(*args, **kwargs):
# 		print('<div>')
# 		func(*args, **kwargs)
# 		print('</div>')
	
# 	return wrapper

# @tagMaker
# def printText(text):
# 	print(text)

# # tag1 = tagMaker(printText)
# # tag1('hello')

# printText('hello world')


# while True:
# 	try:
# 		a = int(input('what'))
# 		b = int(input('now'))
# 		c = a // b
# 		print(c)
# 	# except ZeroDivisionError:
# 	# 	print('не используй ноль')
# 	# 	break
# 	# except ValueError:
# 	# 	print('пиши числа')
# 	# 	break
# 	except Exception as e:
# 		print(e, type(e))
# 		break
# 	finally:
# 		print('операция завершена')


# class CommentFromWebsite():

# 	def __init__(self, data, text, likes):
# 		self.data = data
# 		self.text = text
# 		self.likes = int(likes)

# 	def showComment(self):
# 		'''Выводим коммент'''
# 		print(f'\nКомментарий с сайта, \n дата: {self.data},'
# 		f'\n текст: {self.text}, лайков: {self.likes}')

# 	def changeLikes(self):
# 		'''Изменяем лайк'''
# 		self.likes = self.likes + 1

# 	def changeComment(self, new_text):
# 		'''Изменяем коммент'''
# 		self.text = new_text


# newCom1 = CommentFromWebsite('11/02/11', 'Text1', '12')
# newCom2 = CommentFromWebsite('14/02/14', 'Text2', '7')

# newCom1.showComment()
# newCom2.changeComment('NewText2')
# newCom1.changeLikes()
# newCom1.showComment()
# newCom2.showComment()

# class CarsClass():
# 	def __init__(self, brand, model, year, probeg):
# 		self.brand = brand
# 		self.model = model
# 		self.year = year
# 		self.probeg = int(probeg)

# 	def showInfo(self):
# 		print(f'This car has probeg {self.probeg} km')

# 	def drowCar(self, km):
# 		self.probeg = self.probeg + km
# ###
# class Battery():
# 	def __init__(self, battery = 100):
# 		self.battery = battery

# 	def minusBat(self, minus):
# 		self.battery = self.battery - minus

# 	def batteryValue(self):
# 		print(f'This car has {self.battery}% of battery')
# ###
# class ElectroCar(CarsClass):
# 	def __init__(self, brand, model, year, probeg):
# 		super().__init__(brand, model, year, probeg)
# 		self.battery = Battery()

# 	def showInfo(self):
# 		print(f'This electro car has probeg {self.probeg} km')


# car = CarsClass('opel', 'astra', '2005', 10)
# car.drowCar(200)
# car.showInfo()

# elCar = ElectroCar('ravl', 'astra', '2077', 15)
# elCar.showInfo()
# elCar.battery.batteryValue()
# elCar.battery.minusBat(50)
# elCar.battery.batteryValue()


# from printer import text

# print(text)

# def loop(text, number):
# 	print(text, number)

# loop('know', 32)