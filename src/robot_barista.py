# ------------------------------------------------------------------------------
# EXCERCISES FROM https://www.youtube.com/watch?v=IXr0-J5XXMA&ab_channel=NetworkChuck
# ------------------------------------------------------------------------------

# Welcome to the coffee shop
print("Hello, welcome to NetworkChuckCoffe!")

# Get name and greet
name = input("What is your name? \n")

# Lock out Ben or Patricia
if name == "Ben" or name == "Patricia" or name == "Loki":
    answer = input("Are you evil?")
    if answer == "yes":
        deeds = input("How many good deeds have you done today?")
        if int(deeds) <= 4:
            print("Get out evil " + name + "! ")
            exit()
    if answer == "no":
        print("You are special!")
        print("")


print("Hello " + name + " , thank you so much for coming in today!")

# Price
price_food = 11

# Order Food
print("""Food:
Pizza 
Salad
Burger""")

food = input("What do you want to eat? \n")

# Order beverage
print("""beverages: 
Coffee
Cola
Sirup
Bilz""")

drink = input("What do you want to drink? \n")

price_beverages = 4


if drink == "Coffee":
    price_beverages = 3

elif drink == "Cola":
    coke_style = input("Zero or good coke?")
    if coke_style == "Zero":
        price_beverages += 2

elif drink == "Sirup":
    price_beverages = 2

elif drink == "Bilz":
    price_beverages = 9
else:
    print("Sorry, we don't have that here. Please leave now evil Ben!")
    exit()


count_beverage = int(input("How many " + drink + "s would you like to order?"))

# Summarize order
print("Ok " + name + " your " + food + " and your " +
      str(count_beverage) + " " + drink + "s will be ready in a few minutes")

price = count_beverage * price_beverages + price_food

print("That would be $" + str(price) + " please")
