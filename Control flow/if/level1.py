'''
IF-ELIF-ELSE PRACTICE QUESTIONS
------------------------------
'''

#Eg.1
a = 10
b = 20
if b > a:
    print("b is greater than a")
elif b == a:
    print("b is equal to a")
else:
    print("b is less than a")

# #Eg.2
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if b > a:
    print("b is greater than a")
elif b > 150:
    print("b is also greater than 150") 
else:
    print("a is greater than 20")


# #Eg.3
x = int(input("Enter a number: "))
if x < 10:
    print("x is less than 10")
elif x == 10:
    print("x is equal to 10")
else:
    print("x is greater than 10")
