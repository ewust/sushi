#!/usr/bin/python
import random

class Item(object):
	def __init__(self, name, price, desc, required=False):
		self.name = name
		self.price = price
		self.desc = desc
		self.required = required

class Roll(Item):
	pass

class RegularRoll(Roll):
	pass

class SpecialRoll(Roll):
	pass



class Restaurant(object):
	def __init__(self, name, phone, menu):
		self.name = name
		self.phone = phone
		self.menu = menu

	def _pick_random_item(self, n=1, item_class=RegularRoll):
		returned = 0
		for x in self.menu:
			if isinstance(x, item_class) and x.required:
				returned += 1 
				if returned > n:
					return
				yield x
		while True:
			returned += 1 
			if returned > n:
				return
			yield random.choice([x for x in self.menu if isinstance(x, item_class)])


nagomi = Restaurant("Nagomi", "(734) 761-5800", [
	RegularRoll("Cucumber", 2.50, None),
	RegularRoll("Avocado", 2.50, None),
	RegularRoll("Black Mushroom", 2.50, None),
	RegularRoll("Asparagus", 2.75, None),
	RegularRoll("Asparagus, Avocado, Cucumber", 2.75, None),
	RegularRoll("Tuna", 3.50, None),
	RegularRoll("Spicy Tuna", 4.50, None),
	RegularRoll("Salmon", 3.50, None),
	RegularRoll("Spicy Salmon", 4.50, None),
	RegularRoll("Salmon Skin", 4.00, None),
	RegularRoll("Yellow Tail & Scallion", 4.00, None),
	RegularRoll("Spicy Yellow Tail", 4.50, None),
	RegularRoll("California", 3.75, None),
	RegularRoll("Shrimp California", 4.50, None),
	RegularRoll("Special California", 4.50, "Crab Salad, Tempura, Cucumber, Avocado"),
	RegularRoll("Eel", 4.00, None),
	RegularRoll("East", 5.00, "Shrimp Tempura, Cucumber, Avocado"),
	RegularRoll("Alaskan", 5.50, "Salmon, Avocado, Cucmber"),
	RegularRoll("Boston", 5.00, "Lettuce, Mayo, Cooked Shrimp, Cucumber, Avocado"),
	RegularRoll("Philly Roll", 5.00, "Smoked Salmon, Cream Cheese"),

	SpecialRoll("Nagomi Roll", 9.00, None),
	SpecialRoll("Michigan", 11.00, None),
	SpecialRoll("Mexican", 9.00, None),
	SpecialRoll("Prince", 0.00, None),
	SpecialRoll("Princess", 0.00, None),
	SpecialRoll("Rainbow", 0.00, None),
	SpecialRoll("Salmon on the Beach", 0.00, None),
	SpecialRoll("Godzilla", 0.00, None),
	SpecialRoll("Zen", 0.00, None),
	SpecialRoll("Red Dragon", 0.00, None),
	SpecialRoll("Special Eel", 0.00, None),
	SpecialRoll("Dragon Roll", 0.00, None),
	SpecialRoll("Sunday Morning", 0.00, None),
	SpecialRoll("Las Vegas", 0.00, None),
	SpecialRoll("Yum Yum", 0.00, None),
	SpecialRoll("King Kong", 0.00, None),
	SpecialRoll("Spider Roll", 0.00, None)

	])


if __name__=="__main__":
	import sys
	num_people = sys.stdin[1]

	print nagomi.pick_random_item(num_people, SpecialRoll)
	print nagomi.pick_random_item(int(num_people * 1.5), RegularRoll)
