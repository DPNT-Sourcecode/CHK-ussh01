

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	# CHECK FOR VALID INPUT
	if type(skus) != str:
		return -1

	# Alphabets = SKUs
	items = skus.split(' ')

	# Keep track of the quantity of each item in the cart
	qtyA = 0
	qtyB = 0
	qtyC = 0
	qtyD = 0
	for item in items:
		if item == 'A':
			qtyA += 1
		elif item == 'B':
			qtyB += 1
		elif item == 'C':
			qtyC += 1
		elif item == 'D':
			qtyD += 1
		else:
			return -1

	# Compute each individual SKUs totals
	totalA = ((qtyA % 3) * 50 + int((qtyA / 3)) * 130)
	totalB = ((qtyB % 3) * 30 + int((qtyB / 3)) * 45)
	totalC = qtyC * 20
	totalD = qtyD * 15

	# Computer overall cart total
	cartTotal = totalA + totalB + totalC + totalD

	return cartTotal
