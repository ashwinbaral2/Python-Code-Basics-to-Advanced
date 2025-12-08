'''6.Swap the values of two variables without using a third variable.'''

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
print(f"Before Swapping: a = {a}, b = {b}")
total = a + b
b = total - b
a = total - a
print(f"After Swapping: a = {a}, b = {b}")
#need to rewrite this code again

'''7.Check if a given number is even or odd.'''

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

'''8.Determine if a year is a leap year or not.'''

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

'''9.Convert a given number of days into months and days.'''

days = float(input("Enter number of days: "))
months = days // 30
remaining_days = days % 30
print(f"{days} days is approximately {months} months and {remaining_days} days.")

'''10.Calculate the area of a rectangle.'''

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"Area of the rectangle: {area}")
