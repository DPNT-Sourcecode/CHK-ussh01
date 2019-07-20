

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	# CHECK FOR VALID INPUT

	# Alphabets = SKUs
	items = skus.split(' ')

	# Keep track of the total cost of the cart
	cartTotal = 0
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
