# Importing the classes objects from bicycles
from bicycles import Bicycle, Shop, Customer

# Add Bicycle instances 	
allston = Bicycle('Allson', 10, 100)
fit = Bicycle('FIT', 8, 50)
navigator = Bicycle('Navigator', 7, 200)
urban = Bicycle('Urban', 7, 400)
boston = Bicycle('Boston', 6, 600)
crosstown = Bicycle('Crosstown', 5, 800)

# Add Shop instance
shop1 = Shop('Altamimi Bikes LLC', 0.2)

# Add 6 Bikes to Shop
shop1.add_bicycle(allston, 5)
shop1.add_bicycle(fit, 5)
shop1.add_bicycle(navigator, 4)
shop1.add_bicycle(urban, 4)
shop1.add_bicycle(boston, 3)
shop1.add_bicycle(crosstown, 2)

# Add 3 Customers
abdullah = Customer("Abdullah", 200)
bader = Customer("Bader", 500)
hasan = Customer("Hasan", 1000)

# Show the shop inventory
print("The Shop '{}'".format(shop1.name))
print("="*30)
for i in shop1.inventory:
    print("The Model: " + i['model'] + " - Price: $" + str(i['price']) + " - Quantity: " + str(i['quantity']))


print()
shop1.can_buy(abdullah)
print()
shop1.can_buy(bader)
print()
shop1.can_buy(hasan)
print()
abdullah.buy_bicycle('Allson')
print()
bader.buy_bicycle('Navigator')
print()
hasan.buy_bicycle('Crosstown')
print()
for i in shop1.inventory:
    print("The Model: " + i['model'] + " - Price: $" + str(i['price']) + " - Quantity: " + str(i['quantity']))