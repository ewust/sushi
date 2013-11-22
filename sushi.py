#!/usr/bin/python

import itertools
import json
import random
import urllib2
import sys

class Item(object):
	def __init__(self, name, price, desc, required=False):
		self.name = name
		self.price = price
		self.desc = desc
		self.required = required

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name

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

	def _pick_random_item(self, item_class=RegularRoll):
		for x in self.menu:
			if isinstance(x, item_class) and x.required:
				yield x
		while True:
			yield random.choice([x for x in self.menu if isinstance(x, item_class)])

	def pick_random_item(self, n=1, item_class=RegularRoll):
 		for i,x in itertools.izip(range(n), self._pick_random_item(item_class)):
			yield x


def get_btc_value_usd():
	try:
		f = urllib2.urlopen('https://mtgox.com/api/1/BTCUSD/ticker')
		json_output = f.read()
		f.close()
		return float(json.loads(json_output)['return']['last']['value'])
	except:
		return None


nagomi = Restaurant("Nagomi", "(734) 761-5800", [
	RegularRoll("Cucumber", 2.50, None),
	RegularRoll("Avocado", 2.50, None),
	RegularRoll("Black Mushroom", 2.50, None),
	RegularRoll("Asparagus", 2.75, None),
	RegularRoll("Asparagus, Avocado, Cucumber", 2.75, None),
	RegularRoll("Tuna", 3.50, None),
	RegularRoll("Nagomi Spicy Tuna", 4.50, None, required=True),
	RegularRoll("Crunch Salmon?", 0.00, None),
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
	SpecialRoll("Prince", 9.50, None),
	SpecialRoll("Princess", 9.50, None),
	SpecialRoll("Rainbow", 11.00, None),
	SpecialRoll("Salmon on the Beach", 8.50, None),
	SpecialRoll("Godzilla", 8.50, None),
	SpecialRoll("Zen", 10.00, None),
	SpecialRoll("Red Dragon", 9.00, None),
	SpecialRoll("Special Eel", 14.00, None),
	SpecialRoll("Dragon Roll", 10.00, None),
	SpecialRoll("Sunday Morning", 0.00, None),
	SpecialRoll("Las Vegas", 8.50, None),
	SpecialRoll("Yum Yum", 11.00, None),
	SpecialRoll("King Kong", 9.50, None),
	SpecialRoll("Spider Roll", 8.00, None)

	])


if __name__=="__main__":
	if len(sys.argv) != 2:
		print "Usage: %s NUM_PEOPLE" % sys.argv[0]
		sys.exit(1)
	num_people = float(sys.argv[1])

	special_rolls = list(nagomi.pick_random_item(int(num_people), SpecialRoll))
	regular_rolls = list(nagomi.pick_random_item(int(num_people * 1.5), RegularRoll))
	total_price = sum([x.price for x in special_rolls + regular_rolls])
	per_person_price = total_price / int(num_people)
	
	print "Special rolls:", special_rolls
	print "Regular rolls:", regular_rolls
	print "   Total=$%.02f" % total_price
	print "   per person: $%.02f" % per_person_price
	
	# Get price in bitcoins
	btc_value = get_btc_value_usd()
	if btc_value == None:
		print "<error connecting to mtgox>"
	else:
		print "   Total=%.05f BTC" % (total_price / btc_value)
		print "   per person=%.05f BTC" % (per_person_price / btc_value)
 
