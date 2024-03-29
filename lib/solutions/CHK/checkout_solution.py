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
	totalN = itemQtys['N'] * 40
	totalO = itemQtys['O'] * 10
	totalR = itemQtys['R'] * 50
	# totalS = itemQtys['S'] * 20
	# totalT = itemQtys['T'] * 20
	totalW = itemQtys['W'] * 20
	# totalX = itemQtys['X'] * 17
	# totalY = itemQtys['Y'] * 20
	# totalZ = itemQtys['Z'] * 21

	# A
	# totalA = int((itemQtys['A'] / 5)) * 200 # Favour Pack of 5
	# itemQtys['A'] = itemQtys['A'] % 5
	# totalA += ((itemQtys['A'] % 3) * 50 + int((itemQtys['A'] / 3)) * 130) # Computer for pack of 3 & remainder
	totalA = applyOffer3(itemQtys['A'], 5, 3, 200, 130, 50)

	# B: If E offer applies, update B quantity accordingly
	# totalB = 0
	# if itemQtys['B'] != 0:
	# 	itemQtys['B'] = itemQtys['B'] - int(itemQtys['E'] / 2)
	# 	totalB = ((itemQtys['B'] % 2) * 30 + int((itemQtys['B'] / 2)) * 45)
	totalB = applyOffer1(itemQtys['B'], itemQtys['E'], 2, 30, 45, 2)


	# F
	# totalF = ((itemQtys['F'] % 3) * 10 + int((itemQtys['F'] / 3)) * 20)
	totalF = applyOffer2(itemQtys['F'], 10, 3, 20)

	# H
	# totalH = int((itemQtys['H'] / 10)) * 80
	# itemQtys['H'] = itemQtys['H'] % 10
	# totalH += ((itemQtys['H'] % 5) * 10 + int((itemQtys['H'] / 5)) * 45)
	totalH = applyOffer3(itemQtys['H'], 10, 5, 80, 45, 10)

	# K
	totalK = applyOffer2(itemQtys['K'], 70, 2, 120)

	# M (possibly needs debugging later)
	totalM = applyOffer1(itemQtys['M'], itemQtys['N'], 3, 15, 15, 15)

	# P
	totalP = applyOffer2(itemQtys['P'], 50, 5, 200)

	# Q
	# totalQ = applyOffer2(itemQtys['Q'], 30, 3, 80)
	totalQ = applyOffer1(itemQtys['Q'], itemQtys['R'], 3, 30, 80, 3)

	# U
	totalU = applyOffer2(itemQtys['U'], 40, 4, 120)

	# V
	totalV = applyOffer3(itemQtys['V'], 3, 2, 130, 90, 50)


	# Computer overall cart total
	# cartTotal = totalA + totalB + totalC + totalD + totalE + totalF + totalG + totalH + totalI + totalJ + totalK + totalL + totalM + totalN + totalO + totalP + totalQ + totalR + totalS + totalT + totalU + totalV + totalW + totalX + totalY + totalZ
	cartTotal = totalA + totalB + totalC + totalD + totalE + totalF + totalG + totalH + totalI + totalJ + totalK + totalL + totalM + totalN + totalO + totalP + totalQ + totalR+ totalU + totalV + totalW
	cartTotal += applyGroupOffer(itemQtys)
	
	return cartTotal


# Example offer: 2E get one B free
def applyOffer1(itemQty1, itemQty2, specialOfferQty, normalPrice, normalOfferPrice, normalOfferQty):
	total = 0
	if itemQty1 != 0:
		itemQty1 = itemQty1 - int(itemQty2 / specialOfferQty)
		total = ((itemQty1 % normalOfferQty) * normalPrice + int((itemQty1 / normalOfferQty)) * normalOfferPrice)

	return total

# Example: 2K for 150
def applyOffer2(itemQty, normalPrice, offerQty, offerPrice):
	return ((itemQty % offerQty) * normalPrice + int((itemQty / offerQty)) * offerPrice)

# Example: 3A for 130, 5A for 200
def applyOffer3(itemQty, firstOfferQty, secondOfferQty, firstOfferPrice, secondOfferPrice, normalPrice):
	total = int(itemQty / firstOfferQty) * firstOfferPrice # Favour first offer
	itemQty = itemQty % firstOfferQty
	total += ((itemQty % secondOfferQty) * normalPrice + int(itemQty / secondOfferQty) * secondOfferPrice) # Computer for second offer

	return total

def applyGroupOffer(itemQtys):
	# NOTE: FAVOUR CUSTOMER PRICE POINT
	# Highest to lowest prices: Z > S=T=Y >  X
	groupQtys = {'Z': 0, 'S': 0, 'T': 0, 'Y': 0, 'X': 0}

	groupQtys['S'] = itemQtys['S']
	groupQtys['T'] = itemQtys['T']
	groupQtys['X'] = itemQtys['X']
	groupQtys['Y'] = itemQtys['Y']
	groupQtys['Z'] = itemQtys['Z']

	# Z. not enough for group
	# S. not enough
	# S. enough
	# X. not enough

	# Represent item quantities dictionary as string (arranged from highest to lowest cost SKUs)
	potentialGroupString = ""
	for item in groupQtys:
		potentialGroupString += item * groupQtys[item]

	# If empty string, return zero
	if len(potentialGroupString) == 0:
		return 0

	# Get last index after groups of 3
	lastIndex = len(potentialGroupString) % 3

	# Separate grouped items and items not in the group (to calculate later)
	groupString = ""
	normalItems = ""
	if lastIndex == 0:
		groupString = potentialGroupString
	else: 
		groupString = potentialGroupString[:-lastIndex]
		normalItems = potentialGroupString[-lastIndex:]

	# Calculate group price
	groupTotalPrice = int(len(groupString) / 3) * 45

	# Calculate normal non-offer prices for the remaining items
	normalTotalPrice = 0
	for item in normalItems:
		if item == 'Z':
			normalTotalPrice += 21
		elif item == 'S':
			normalTotalPrice += 20
		elif item == 'T':
			normalTotalPrice += 20
		elif item == 'Y':
			normalTotalPrice += 20
		elif item == 'X':
			normalTotalPrice += 17
		

	return groupTotalPrice + normalTotalPrice









