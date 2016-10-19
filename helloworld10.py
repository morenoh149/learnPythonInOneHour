import random
import sys
import os

class Animal:
	__name = ""  # double underscore indicates this is a private variable
	__height = 0
	__weight = 0
	__sound = 0

	def __init__(self, name, height, weight, sound):
		self.__name = name
		self.__height = height
		self.__weight = weight
		self.__sound = sound

	def set_name(self, name): # self works like `this` in other languages (java, javascript)
		self.__name = name

	def get_name(self):
		return self.__name

	def set_height(self, height): # self works like `this` in other languages (java, javascript)
		self.__height = height

	def get_height(self):
		return self.__height

	def set_weight(self, weight): # self works like `this` in other languages (java, javascript)
		self.__weight = weight

	def get_weight(self):
		return self.__weight

	def set_sound(self, sound): # self works like `this` in other languages (java, javascript)
		self.__sound = sound

	def get_sound(self):
		return self.__sound

	def get_type(self):
		print("Animal")

	def toString(self):
		return "{} is {} cm tall and {} kilograms and says \"{}\"".format(self.__name, self.__height, self.__weight, self.__sound)

cat = Animal('Whiskers', 33, 10, 'Meow famz')
print(cat.toString())


### Inheritance
class Dog(Animal):  # extending a class
	__owner = ""

	def __init__(self, name, height, weight, sound, owner):
		self.__owner = owner
		super(Dog, self).__init__(name, height, weight, sound)

	def set_owner(self, owner):
		self.__owner = owner

	def get_owner(self):
		return owner

	def get_type(self):
		print("Dog")

	def toString(self):
		return "{} is {} cm tall and {} kilograms and says \"{}\". His owner is {}".format(
				self.__name, self.__height, self.__weight, self.__sound, self.__owner)

	def multiple_sounds(self, how_many=None):  # default variable values, allow you to omit them when calling the function
		if how_many is None:
			print(self.get_sound())
		else:
			print(self.get_sound() * how_many)

madison = Dog('Maddie', 10, 10, 'wwwoof', 'Harry G Moreno')
print(madison.toString())
print(madison.get_sound())
print(madison.multiple_sounds())
print(madison.multiple_sounds(2))

class AnimalTesting:
	def get_type(self, animal):
		animal.get_type()

test_animals = AnimalTesting()

test_animals.getType(cat)
test_animals.getType(spot)
