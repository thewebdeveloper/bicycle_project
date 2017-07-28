class Bicycle(object):
    ''' Bicycle Class '''
    def __init__(self, model, weight, cost):
        self.model = model
        self.weight = weight
        self.cost = cost
    
    
class Shop(object):
	''' Bike Shops Class '''
	inventory = []
	profit = []
	
	def __init__(self, name, margin):
		self.name = name
		self.margin = margin
    
	def add_bicycle(self, bicycle, quantity):
		bike = {
			'model' : bicycle.model,
			'weight' : bicycle.weight,
			'cost' : bicycle.cost,
			'price': (bicycle.cost + (bicycle.cost*self.margin)),
			'quantity': quantity
		}
		Shop.inventory.append(bike)
		return Shop.inventory
	
	def can_buy(self, customer):
		print("The Customer {} can buy these bikes".format(customer.name))
		for i in Shop.inventory:
			if customer.fund >= i['price']:
				print("Model of " + i['model'] + ", its price $" + str(i['price']) + ", we currently have " + str(i['quantity']))
	
	
class Customer(object):
	''' Customer Class '''
	
	def __init__(self, name, fund):
		self.name = name
		self.fund = fund
	
	def buy_bicycle(self, bicycle):
		for i in Shop.inventory:
			if i['model'] == bicycle:
				balance = self.fund - i['price']
				i['quantity'] -= 1
				Shop.profit.append(i['price'])
				print("Mr. " +self.name+ ", the bike you have chosen is: " + i['model'] + ", with price of $" + str(i['price']))
				print("Your Balance is ${}".format(balance))
				print("The remaining stock for {} is {}".format(i['model'], i['quantity']))
				print("The Shop has made {}".format(sum(Shop.profit)))