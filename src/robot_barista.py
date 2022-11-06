# ------------------------------------------------------------------------------
# EXCERCISES FROM https://www.youtube.com/watch?v=IXr0-J5XXMA&ab_channel=NetworkChuck
# ------------------------------------------------------------------------------

# Welcome to the coffee shop
print("Hello, welcome to NetworkChuckCoffe!")

# Get name and greet
name = input("What is your name? \n")

print("Hello " + name + " , thank you so much for coming in today!")

# Price
price_food = 50
price_beverages = 4


# Order Food
print("""Food:
Pizza 
Salad
Burger""")

food = input("What do you want to eat? \n")

# Order beverage
print("""beverages:
Coffe
Cola
Sirup""")

drink = input("What do you want to drink? \n")

count_beverage = int(input("How many " + drink + "s would you like to order?"))

# Summarize order
print("Ok " + name + " your " + food + " and your " + str(count_beverage) + " " + drink + "s will be ready in a few minutes")

price = count_beverage * price_beverages + price_food

print("That would be $" + str(price) + " please")
