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
