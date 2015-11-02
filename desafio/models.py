class Merchant:
	name = ""
	adress = ""

	def __init__(self, name, adress):
		self.name = name
		self.adress = adress

class Purchase:
	purchaser_name = ""
	item_description = ""
	item_price = 0.0
	purchase_count = 0
	merchant_name = 0

	def __init__(self, purchaser_name, item_description, item_price, purchase_count, merchant_name):
		self.purchaser_name = purchaser_name
		self.item_description = item_description
		self.item_price = item_price
		self.purchase_count = purchase_count
		self.merchant_name = merchant_name