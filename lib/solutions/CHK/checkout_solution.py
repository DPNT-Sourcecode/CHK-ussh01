import string

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	# Check if input is of type string
	if type(skus) != str:
		return -1

	# Return zero if empty string
	if len(skus) == 0:
		return 0

	# Initialize dictionary with all uppercase alphabet SKUs
	itemQtys = {}
	for letter in string.ascii_uppercase:
		itemQtys[letter] = 0

	# Keep track of the quantity of each item in the cart
	for item in skus:
		if item in itemQtys:
			itemQtys[item] += 1
		else:
			return -1s

	# Compute each individual SKUs totals

	# No offer items first
	totalC = itemQtys['C'] * 20
	totalD = itemQtys['D'] * 15
	totalE = itemQtys['E'] * 40
	totalG = itemQtys['G'] * 20
	totalI = itemQtys['I'] * 35
	totalJ = itemQtys['J'] * 60

	# A
	totalA = int((itemQtys['A'] / 5)) * 200 # Favour Pack of 5
	itemQtys['A'] -= 5 * int(itemQtys['A'] / 5)
	totalA += ((itemQtys['A'] % 3) * 50 + int((itemQtys['A'] / 3)) * 130) # Computer for pack of 3 & remainder

	

	# If E offer applies, update B quantity accordingly
	totalB = 0
	if itemQtys['B'] != 0:
		itemQtys['B'] = itemQtys['B'] - int(itemQtys['E'] / 2)
		totalB = ((itemQtys['B'] % 2) * 30 + int((itemQtys['B'] / 2)) * 45)


	totalF = ((itemQtys['F'] % 3) * 10 + int((itemQtys['F'] / 3)) * 20)

	# Computer overall cart total
	cartTotal = totalA + totalB + totalC + totalD + totalE + totalF

	return cartTotal



