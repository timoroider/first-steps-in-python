# ------------------------------------------------------------------------------
# HELLO WORLD
# ------------------------------------------------------------------------------

print("Hello World!")

# ------------------------------------------------------------------------------
# PLACEHOLDERS
# ------------------------------------------------------------------------------

name = "Jeff"
print(name + " is 15 years old ")
print("***********************************************")

sentence = "%s is 15 years old"
print(sentence)

print("***********************************************")

print(sentence % name)
print(sentence % ("avin"))

print("***********************************************")

sentence = "%s %s is the president of the us"
print(sentence % ("Barack", "Obama"))

print("***********************************************")

sentence = "%s is %d years old"
print(sentence % ("Obama", 50))

print("***********************************************")


# ------------------------------------------------------------------------------
# LISTS
# ------------------------------------------------------------------------------

shop_list = ["Apples ", "Oranges", "Bananas", "Cheese"]
print(shop_list[0])

shop_list.append("Blueberries")
print(shop_list[0:5])


shop_list.extend(["Cake", "Toast"])

shop_list[0] = "Cherries"
print(shop_list)

shop_list.remove("Cherries")

print(shop_list)

print(len(shop_list))

shop_list.insert(-3, "Bidon")

print(shop_list*2)

# ------------------------------------------------------------------------------
# EXCERCISES FROM https://www.youtube.com/watch?v=mRMmlo_Uqcs&ab_channel=NetworkChuck
# ------------------------------------------------------------------------------

# Multiline string

print("""I am Iron Man.
No, I am Tony Stark""")


# String concatenation

print("I am Iron Man. \n" + "No, I am  Tony Stark")
