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
			return -1

	# Compute each individual SKUs totals

	# No offer items first
	totalC = itemQtys['C'] * 20
	totalD = itemQtys['D'] * 15
	totalE = itemQtys['E'] * 40
	totalG = itemQtys['G'] * 20
	totalI = itemQtys['I'] * 35
	totalJ = itemQtys['J'] * 60
	totalL = itemQtys['L'] * 90
	# totalM = itemQtys['M'] * 15
	totalN = itemQtys['N'] * 40
	totalO = itemQtys['O'] * 10
	totalS = itemQtys['S'] * 30
	totalT = itemQtys['T'] * 20
	totalW = itemQtys['W'] * 20
	totalX = itemQtys['X'] * 90
	totalY = itemQtys['Y'] * 10
	totalZ = itemQtys['Z'] * 50

	# A
	totalA = int((itemQtys['A'] / 5)) * 200 # Favour Pack of 5
	itemQtys['A'] = itemQtys['A'] % 5
	totalA += ((itemQtys['A'] % 3) * 50 + int((itemQtys['A'] / 3)) * 130) # Computer for pack of 3 & remainder

	# B: If E offer applies, update B quantity accordingly
	# totalB = 0
	# if itemQtys['B'] != 0:
	# 	itemQtys['B'] = itemQtys['B'] - int(itemQtys['E'] / 2)
	# 	totalB = ((itemQtys['B'] % 2) * 30 + int((itemQtys['B'] / 2)) * 45)
	totalB = applyOffer1(itemQtys['B'], itemQtys['E'], 2, 30, 45, 2)


	# F
	totalF = ((itemQtys['F'] % 3) * 10 + int((itemQtys['F'] / 3)) * 20)

	# H
	totalH = int((itemQtys['H'] / 10)) * 80
	itemQtys['H'] = itemQtys['H'] % 10
	totalH += ((itemQtys['H'] % 5) * 10 + int((itemQtys['H'] / 5)) * 45)

	# K
	totalK = ((itemQtys['K'] % 2) * 80 + int((itemQtys['K'] / 2)) * 150)

	# M (possibly needs debugging later)
	totalM = applyOffer1(itemQtys['M'], itemQtys['N'], 3, 15, 15, 15)

	totalP = 



	# Computer overall cart total
	cartTotal = totalA + totalB + totalC + totalD + totalE + totalF + totalG + totalI + totalJ + totalK + totalL + totalM + totalN
	# cartTotal = totalA + totalB + totalC + totalD + totalE + totalF + totalG + totalI + totalJ + totalK + totalL + totalM + totalN + totalO + totalP + totalQ + totalR + totalS + totalT + totalU + totalV + totalW + totalX + totalY + totalZ

	return cartTotal


# Example offer: 2E get one B free
def applyOffer1(itemQty1, itemQty2, specialOfferQty, normalPrice, normalOfferPrice, normalOfferQty):
	total = 0
	if itemQty1 != 0:
		itemQty1 = itemQty1 - int(itemQty2 / specialOfferQty)
		total = ((itemQty1 % normalOfferQty) * normalPrice + int((itemQty1 / normalOfferQty)) * normalOfferPrice)

	return total









