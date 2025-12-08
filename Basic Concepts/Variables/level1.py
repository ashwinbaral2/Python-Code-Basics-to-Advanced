'''1.Write a Python program to print "Hello, World!".'''

print("Hello, World!")

'''2.Calculate the sum of two numbers.'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum = a + b
print("Sum:", sum)

'''3.Find the product of two numbers.'''

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
product = a * b
print("Product:", product)

'''4.Convert temperature from Celsius to Fahrenheit.'''

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

'''5.Compute the area of a circle given its radius.'''

import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(math.pi)#value of pi from math module
print("Area of the circle:", area)
