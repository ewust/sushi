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
	pass
