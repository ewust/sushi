#!/usr/bin/python

class Item(object):
	def __init__(self, name, price, desc):
		self.name = name
		self.price = price
		self.desc = desc

class RegularRoll(Item):
	pass

class SpecialRoll(Item):
	pass



class Restaurant(object):
	def __init__(self, name, phone, menu):
		self.name = name
		self.phone = phone
		self.menu = menu

	def pick_random_item(self, n=1, item_class=RegularRoll):
		for i in range(n):
			yield random.choice([x for x in self.menu if x.class == item_class])


nagomi = Restaurant("Nagomi", "...", [
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
	RegularRoll("Special California", 4.50, None),
	RegularRoll("Eel", 4.00, None),
	RegularRoll("East", 5.00, None),
	RegularRoll("Alaskan", 5.50, None),
	RegularRoll("Boston", 5.00, None),
	RegularRoll("Philly Roll", 5.00, None),
	])



if __name__=="__main__":
	pass
