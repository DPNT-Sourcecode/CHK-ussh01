import string

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	# CHECK FOR VALID INPUT
	if type(skus) != str:
		return -1

	if len(skus) == 0:
		return 0

	# Keep track of the quantity of each item in the cart
	itemQtys = {}
	for letter in string.ascii_uppercase:
		itemQtys[letter] = 0
		
	qtyA = 0
	qtyB = 0
	qtyC = 0
	qtyD = 0
	qtyE = 0
	qtyF = 0
	for item in skus:
		if item == 'A':
			qtyA += 1
		elif item == 'B':
			qtyB += 1
		elif item == 'C':
			qtyC += 1
		elif item == 'D':
			qtyD += 1
		elif item == 'E':
			qtyE += 1
		elif item == 'F':
			qtyF += 1
		else:
			return -1

	# Compute each individual SKUs totals

	totalA = int((qtyA / 5)) * 200 # Favour Pack of 5
	qtyA -= 5 * int(qtyA / 5)
	totalA += ((qtyA % 3) * 50 + int((qtyA / 3)) * 130) # Computer for pack of 3 & remainder

	totalC = qtyC * 20
	totalD = qtyD * 15
	totalE = qtyE * 40

	# If E offer applies, update B quantity accordingly
	totalB = 0
	if qtyB != 0:
		qtyB = qtyB - int(qtyE / 2)
		totalB = ((qtyB % 2) * 30 + int((qtyB / 2)) * 45)


	totalF = ((qtyF % 3) * 10 + int((qtyF / 3)) * 20)

	# Computer overall cart total
	cartTotal = totalA + totalB + totalC + totalD + totalE + totalF

	return cartTotal

