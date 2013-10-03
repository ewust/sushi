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
	RegularRoll("Roll", 5.34, "Tasty fish"),

	])



if __name__=="__main__":
	pass
