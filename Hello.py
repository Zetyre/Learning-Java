# This is a program that says hello, asks for my name, age, and says how old will I be in a year

print ("Hello world!")
print ("What is your name?")
myName = input()
print("Nice to meet you, " + myName)
print("Your name has a lenght of:")
print (len(myName))

print ("What is your age?")
myAge = input()

print ("You will be " + str(int(myAge) + 1) + " in a year.")
