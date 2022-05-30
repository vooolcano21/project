# STRING

#1.
# song = """When an eel grabs your arm,
# ... And it causes great harm,
# ... That's - a moray!"""

# print(song.find('moray'))
# newMoray = song.replace(' m', ' M')
# print(newMoray)

#2.
# questions = [
# 	"We don't serve strings around here. Are you a string?",
# 	"What is said on Father's Day in the forest?",
# 	"What makes the sound 'Sis! Boom! Bah!'?"
# 	]

# answers = [
# 	"An exploding sheep.",
# 	"No, I'm a frayed knot.",
# 	"'Pop!' goes the weasel."
# 	]

# questionsNew = str(questions)
# answersNew = str(answers)
# questionsNew = questionsNew.strip('[]')
# answersNew = answersNew.strip('[]')

# print(f'''Q: {questionsNew}
# A: {answersNew}
# ''')

#3.


#4-5.
# salutation = 'Saint'
# name = 'Frank'
# verbed = 'ran'
# room = 72
# animals = 'horses'
# amount = 5
# product = 'seventy'
# percent = 56
# spokesman = 'Richard Geer'
# job_title = 'President'

# letterString = f'''Dear {salutation} {name},
# Thank you for your letter. We are sorry that our {product}
# {verbed} in your {room}. Please note that it should never
# be used in a {room}, especially near any {animals}.
# Send us your receipt and {amount} for shipping and handling.
# We will send you another {product} that, in our tests,
# is {percent}% less likely to have {verbed}.
# Thank you for your support.
# Sincerely,
# {spokesman}
# {job_title}'''

# print(letterString)


#6.


#WHILE / FOR
#1.
# list1 = [3, 2, 1, 0]

# for index in list1:
# 	print(index)

#2.
# guess_me = 7
# number = 3

# while True:
# 	if number < guess_me:
# 		print('too low')
# 		number += 1
# 	elif number == guess_me:
# 		print('found it', number)
# 		break
# 	elif number > guess_me:
# 		print('oops', number)
# 		break
# 	else:
# 		print('smth wrong')

#3.
# guess_me = 5

# for num in range(10):
# 	if num < guess_me:
# 		print('too low')
# 	elif num == guess_me:
# 		print('found it')
# 	elif num > guess_me:
# 		print('too high')
# 		break


#TUPLES and LISTS

# float1 = 4.2

# print(type(float1))

# years_list= [1999, 2000, 2001, 2002, 2003, 2004]
# things = ["mozzarella", "cinderella", "salmonella"]
# newThings = things[1].capitalize()
# print(newThings)
# newMoz = things[0].upper()
# print(newMoz)

# things.remove('salmonella')
# print(things)

# surprise = ["Groucho", "Chico", "Harpo"]
# surprise[2] = 'harpo'
# surprise.reverse()
# surprise[0] = 'Harpo'
# print(surprise)

# even = [number for number in range(1, 10) if number % 2 == 0]
# print(even)

# start1 = ["fee", "fie", "foe"]
# rhymes = [
# 	("flop", "get a mop"),
# 	("fope", "turn the rope"),
# 	("fa", "get your ma"),
# 	("fudge", "call the judge"),
# 	("fat", "pet the cat"),
# 	("fog", "walk the dog"),
# 	("fun", "say we're done"),
# ]
# start2 = "Someone better"


# for (first, second) in rhymes:
# 	print(f'{first.capitalize()} {second}.')


#CLASS & OBJECT#

# class Thing():
# 	pass

# class Thing2():
# 	pass

# letters = 'abc'

# class Thing3():
# 	letters = 'xyz'

# print(Thing3.letters)

# class Element():
# 	def __init__(self, name, symbol, number):
# 		self.__name = name
# 		self.__symbol = symbol
# 		self.__number = number

# 	def dump(self):
# 		return self.__name, self.__symbol, self.__number

# 	def getName(self):
# 		print(self.__name)

# 	def getSymbol(self):
# 		print(self.__symbol)

# 	def getNum(self):
# 		print(self.__number)

# el = Element('Hydrogen', 'H', 1)

# dictionary =  {
# 	'name': 'Hydrogen',
# 	'symbol': 'H',
# 	'number': 1,
# }

# hydrogen = Element(**dictionary)
# print(hydrogen.dump())
# hydrogen.getName()

# # #
# class Laser():
# 	def does(self):
# 		return 'disintegrate'

# class Claw():
# 	def does(self):
# 		return 'crush'

# class SmartPhone():
# 	def does(self):
# 		return 'ring'

# class Robot():
# 	def __init__(self, laser, claw, smartPhone):
# 		self.laser = laser
# 		self.claw = claw
# 		self.smartPhone = smartPhone

# 	def does(self):
# 		print(self.laser.does(), self.claw.does(), self.smartPhone.does())

# laser1 = Laser()
# claw1 = Claw()
# smart = SmartPhone()

# robot = Robot(laser1, claw1, smart)
# robot.does()

