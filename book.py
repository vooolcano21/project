# b = [1,2,3,4,5,6]

# for countdown in b:
# 	print(countdown)

# spells = [
# 	"Riddikulus!",
# 	"Wingardium Leviosa!",
# 	"Avada Kedavra!",
# 	"Expecto Patronum!",
# 	"Nox!",
# 	"Lumos!",
# 	]
# print(spells[3])

# quotes = {
# 	"Moe": "A wise guy, huh?",
# 	"Larry": "Ow!",
# 	"Curly": "Nyuk nyuk!",
# }
# stooge = "Curly"
# print(stooge, "says:", quotes["Curly"])

#help('keywords')

# type(7) <class 'int'>
# isinstance(7, int) True

# why = bye = hi = 'what?'
# print(why, bye, hi)

# from this import

# x = 5
# print(x)

# y = x
# print(y)

# x = 29
# print(x)

# y = 28
# print(y)

# a = [2, 4, 6]
# b = a
# print(a, b)
# b = [2, 5, 6]
# b = a 
# print(a, b)
# print(type(b))

# c = {
# 	'one': 1,
# 	'2': 2,
# }

# print(c, type(c))

# c = {
# 	'one': 1,
# 	'2': 2,
# }


# d = c

# d = {
# 	'two': 2,
# }

# print(d)

# bool(True)
# bool(1)
# bool(0)
# bool(False)

# a = 4
# a *= 2
# a -= 4
# a += 8
# a %= 10
# a **= 2
# a //= 2
# print(a)
# print(divmod(10,8))

# int(True) #1
# int(False) #0

# print(True) #True
# print(+True) #1

# sum = 1 + \
# 	  2 + \
# 	  3 + \
# 	  4

# sum = (1 +
# 	  2 +
# 	  3 +
# 	  4)

# print(sum)


# disaster = False
# large = True

# if disaster:
# 	if large:
# 		print('Large amazing')
# 	else:
# 		print('normal disaster')
# else:
# 	if large:
# 		print('unknown large bad thing')
# 	else:
# 		print('normal thing')

# number = 4
# if number == 1:
# 	print('Number 1')
# elif number == 2:
# 	print('Number 2')
# elif number == 3:
# 	print('Number 3')
# else:
# 	print('We didn\'t expect', number)

# x = 2
# print(5 > x and 1 < x) # True
# print(x == 4 or x == 2) # True
# print(x == 2 and not x == 4) # True

# someList = [] # False
# if someList:
# 	print('smth is here')
# else: 
# 	print('i\'m empty')

# vowels = 'aeiou'
# letter = 'o'
# if letter in vowels:
# 	print(letter, 'is a vowel')

# secret = 6
# guess = 6
# if secret > guess:
# 	print('too low')
# elif secret < guess:
# 	print('too high')
# else:
# 	print('just right')

# small = True
# green = False
# if small and green:
# 	print('goroh')
# elif small and not green:
# 	print('viwn9')
# elif green and not small:
# 	print('arbuz')
# else:
# 	print('tykva')

# print('my\nnew \thouse')

# a = 'goose.'
# b = 'mouse.'
# c = 'rat.'

# print(a, b, c)

# start = 'Na ' * 4 + '\n'
# print('Kostya ' * 5)

# word = 'qwertyuiikjhgfdsasdfg'
# print(word[0:]) # qwertyuiikjhgfdsasdfg
# print(word[10:]) # jhgfdsasdfg
# print(word[10:20]) # jhgfdsasdf c 10 do 20
# print(word[15:-3]) # sas
# print(word[-10:-5]) # hgfds
# print(word[::5]) # qyjsg \ ???????????? 5?? ????????????
# print(word[-35:-35]) # '' \ ?? ???????????? ?????????? 0, ?? ?????????? ?????????? -1. ???????? - ??????????????

# word = 'qwertyuiikjhgfdsasdfg'
# print(len(word))

# tasks = 'get gloves,get mask,give cat vitamins,call ambulance'
# list1 = tasks.split(',')

# print(list1)

# some_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
# some_string = ', '.join(some_list)
# print(some_string)

# setup = "a duck goes into a bar..."
# newSetup = setup.replace('duck', 'somers')
# print(setup)
# print(newSetup)

# world = '    saswe   '
# print(world.strip()) # saswe|
# print(world.lstrip()) #saswe   |

# poem = '''All that doth flow we cannot liquid name
# Or else would fire and water be the same;
# But that is liquid which is moist and wet
# Fire that property can never get.
# Then 'tis not cold that doth the fire put out
# But 'tis the wet that makes it die, no doubt.'''

# word = 'the'
# poem.find(word)
# poem.index(word)

# setu = 'a duck goes into a bar...'
# setup = setu.strip('.')
# print(setup.capitalize())
# print(setup.title())
# print(setup.upper())
# print(setup.lower())
# print(setup.swapcase())

# print(setup.center(40))
# print(setup.ljust(40))
# print(setup.rjust(40))

# a = 'string'
# b = 344
# c = 'omg what a bull'
# print(f'{a =} is about {b =} and it\'s {c =}')
# print('{a} is about {b} and it\'s {c}')

# count = 1
# while count < 5:
# 	print(count)
# 	count += 1

# while True:
# 	datas = input('Integer, please [q to quit]: ')
# 	if datas == 'q':
# 		break
# 	print(datas.capitalize())

# while True:
# 	datas = input('Integer, please [q to quit]: ')
# 	if datas == 'q':
# 		break
# 	number = int(datas)
# 	if number % 2 == 0:
# 		continue
# 	print(number, 'squared is', number*number)4

# numbers = [1, 3, 5]
# position = 0
# while position < len(numbers):
# 	number = numbers[position]
# 	if number % 2 == 0:
# 		print('found even number', number)
# 		break
# 	position += 1
# else:
# 	print('no found even number')


# offset = 0
# while offset < len(word):
# 	print(word[offset])
# 	offset += 1

# word = 'aaaaaat'
# for letter in word:
# 	if letter == 'a':
# 		print('found illegal letter')
# 		break
# 	print(letter)

# word = 'aaaaaat'
# for letter in word:
# 	if letter == 'a':
# 		continue
# 	print(letter)

# word = 'qwerty'
# for letter in word:
# 	if letter == 'x':
# 		print("we found 'x'")
# else:
# 	print("no 'x' in there")

# for num in range(0, 5):
# 	print(num)

# for num1 in range(-5, 0):
# 	print(num1)

# newList = list(range(0, 10))
# for index in newList:
# 	print(index)

# tupleTest = ('Word')
# tupleTest1 = ('Word', 'Word2', 'Word3')
# print(tupleTest1)
# print(type(tupleTest), type(tupleTest1))

# a1, a2, a3 = tupleTest1
# print(a1, a2, a3)

# max_list = ['Frank', 'Chao']
# print(tuple(max_list))

# max_list = ('Frank', 'Chao')
# max_list2 = ('Frank', 'Chao')
# sumOf = max_list + max_list2

# print(sumOf)

# print(max_list * 3)

# tupleTest1 = ('Word', 'Word2', 'Word3')
# for word in tupleTest1:
# 	print(word)

# weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# line = 'cats'
# print(list(line))

# cal = '9/19/2020'
# print(cal.split('/'))

# numbers = ['9', '19', '2020']
# print(numbers[2])
# numbers.reverse()
# print(numbers)

# numbers = ['9', '19', '2020', '7', '29', '2120']
# numbers.append('new')
# numbers.insert(0, 'first')
# print(numbers * 2)

# list1 = ['one', 'two']
# list2 = ['three']

# list1.extend(list2)
# list1 += list2
# list1[0] = 'three'
# list1[0:1] = 'popok'
# del list1[5] #delete 'two'
# list1.remove('o')
# print(list1)

# list1 = ['gro', 'groove', 'gooo']
# go = list1.pop()
# print(list1, ' and ', go)
# print(list1.index('groove'))
# print('groove' in list1)

# words = ['lol', 'bow', 'wow', 'lol', 'bow', 'wow']
# print(words.count('lol'))

# separator = '*'
# joined = separator.join(words)
# splited = joined.split(separator)

# print(joined) # lol*bow*wow*lol*bow*wow
# print(splited) # 'lol', 'bow', 'wow', 'lol', 'bow', 'wow']

# sorteed = sorted(words)
# words.sort()
# words.sort(reverse=True)
# print(words, sorteed)

# print(len(words))

# a = [1, 2, 3]
# b = a.copy()
# c = list(a)
# d = a[:]

# print(a, b, c, d) # [1, 2, 3]

# sortsOf = ['low', 'high', 'dream']

# for cheese in sortsOf:
# 	print(cheese)

# for cheese in sortsOf:
# 	if cheese.startswith('c'):
# 		print('I dont want to eat it')
# 		break
# 	else:
# 		print(cheese)
# else:
# 	print('i dont find anything with c')

# days = ['Monday', 'Tuesday', 'Wednesday']
# fruits = ['banana', 'orange', 'peach']
# drinks = ['coffee', 'tea', 'beer']
# desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

# for day, drink, fruit, dessert in zip(days, fruits, drinks, desserts):
# 	print(day, ": drink -", drink, ", eat -", fruit, ", enjoy -", dessert)

# english = 'Monday', 'Tuesday', 'Wednesday'
# french = 'Lundi', 'Mardi', 'Mercredi'

# print(list(zip(english, french)))
# print(dict(zip(english, french)))

# numbers = [number for number in range(1, 8)]
# print(numbers)

# numbers2 = []
# for number in range(1, 8):
# 	numbers2.append(number)
# print(numbers2)

# new_dict = {
# 	'brand': 'Honda',
# 	'model': 'Civic',
# 	'year': 1995
# 	}

# old_dict = {
# 	'solve': 'new'
# }

# new_dict.update(old_dict)
# print(new_dict)
# print(len(new_dict))

# x = new_dict['brand']
# x2 = new_dict.get('brand')
# print(x, x2)

# keys = dict.keys(new_dict)
# values = dict.values(new_dict)
# items = dict.items(new_dict)

# print(keys, values, items)

# for x in new_dict.keys():
# 	print(x)

# get = new_dict.pop('brand')
# print(new_dict, get)

# newOne = new_dict.copy()
# print(newOne == new_dict)
# newOne['brand'] = 'molly'
# print(newOne, new_dict)

# word = 'letters'

# letters_count = {letter: word.count(letter) for letter in word}
# print(letters_count)


# drinks = {
#  'martini': {'vodka', 'vermouth'},
#  'black russian': {'vodka', 'kahlua'},
#  'white russian': {'cream', 'kahlua', 'vodka'},
#  'manhattan': {'rye', 'vermouth', 'bitters'},
#  'screwdriver': {'orange juice', 'vodka'}
#  }

# for name, contents in drinks.items():
# 	if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
#  		print(name)

# def knights(saying):
# 	def inner(quote):
# 		return print(f'We are the knights who say: {quote}')
# 	return inner(saying)

# knights('Vi!')

# # ??????????????????
# def knights(saying):
# 	def inner():
# 		return print(f'We are the knights who say: {saying}')
# 	return inner

# closed = knights('Vi!')
# closed()

# #??????????
# #1
# def area(a, b):
# 	print(a * b)

# print((lambda a, b: a * b)(14, 10)) # 140
# #2
# def maximum(a, b):
# 	if a > b:
# 		print(a)
# 	else:
# 		print(b)

# print((lambda a, b: a if a > b else b))

# def one():
# 	'''
# 	What a one sous isawo sqew
# 	'''
# 	print('f')

# print(one.__doc__)

# my_dict = {'a':1, 'b':2, 'c':3}

# try:
# 	value = my_dict['a']
# except KeyError:
# 	print('A KeyError occurred!')
# else:
# 	print('my_dict: No error occurred!')

# class Hugo():
# 	def __init__(self, name, age):
# 		self.hidden_name = name
# 		self.age = age

# 	def change_age(self, num):
# 		self.age += num

# 	def showInfo(self):
# 		print(f'Hi. I\'m {self.name} and I\'m {self.age} years old')

# 	@property
# 	def name(self):
# 		return self.hidden_name

# 	@name.setter
# 	def name(self, newName):
# 		self.hidden_name = newName

# class LowHugo(Hugo):
# 	def __init__(self, name, age, status):
# 		super().__init__(name, age)
# 		self.status = status

# 	def lower(self):
# 		print('Im lower')



# frank = Hugo('Frank', 31)
# john = LowHugo('John', 24, 'lower')

# john.lower()
# john.showInfo()
# # john.set_name('BigJohn')
# # print(john.get_name())
# frank.name = 'Olof'
# print(frank.name)

# class Circle():
# 	def __init__(self, radius):
# 		self.__radius = radius

# 	@classmethod
# 	def printino(cls):
# 		print('classmethod')

# 	@property
# 	def diameter(self):
# 		return 2 * self.__radius

# c = Circle(5)
# c.printino()

class Saying():
	@staticmethod
	def say():
		print('this class is just saying this')

Saying.say()