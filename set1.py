'''
IF-ELIF-ELSE PRACTICE QUESTIONS
------------------------------
'''

#Eg.1
# a = 10
# b = 20
# if b > a:
#     print("b is greater than a")
# elif b == a:
#     print("b is equal to a")
# else:
#     print("b is less than a")

# #Eg.2
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# if b > a:
#     print("b is greater than a")
# elif b > 150:
#     print("b is also greater than 150") 
# else:
#     print("a is greater than 20")


# #Eg.3
# x = int(input("Enter a number: "))
# if x < 10:
#     print("x is less than 10")
# elif x == 10:
#     print("x is equal to 10")
# else:
#     print("x is greater than 10")

'''
NESTED IF PRACTICE QUESTIONS
----------------------------

1. Number Classification
Ask the user for a number.
- If the number is positive:
    - Check if it's even or odd and print accordingly.
- Else if the number is negative, print "Negative".
- Else, print "Zero".
'''
# num = int(input("Enter a number: "))
# if num > 0:
#     if num % 2 == 0:
#         print("Positive even number")
#     else:
#         print("Positive odd number")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

'''
2. Student Grades
Ask for marks in a subject.
- If marks >= 50:
    - Check if marks >= 90: print "Grade A"
    - Else if marks >= 75: print "Grade B"
    - Else: print "Grade C"
- Else: print "Fail"
'''

# marks = float(input("Enter your Marks : "))

# if marks>=50:
#     if marks>=90:
#         print("You have obtained Grade-A. Excellent performance!")
#     elif marks>=75:
#         print("You have obtained Grade-B. Very Good performance!")
#     else:
#         print("You have obtained Grade-C. Acceptable performance!")

# else:
#     print ("Sorry! You didn't pass, better luck next time.")

'''
3. Login System
Ask for username and password.
- If username is correct:
    - Check if password is correct:
        - If yes, print "Login successful"
        - Else, print "Incorrect password"
- Else: print "User not found"
'''
# username = input("Your Username : ")


# if username == "b_for_barsha" or "ashwin_baral":
#     password = input("Your Password : ")
#     if password == "ktm@123":
#         print("Login Successful!")
#     else:
#         print("Incorrect Password!")
# else:
#     print("User not found!")


'''
4. Leap Year Detailed
Ask for a year.
- If year divisible by 4:
    - If year divisible by 100:
        - If year divisible by 400: print "Leap year"
        - Else: print "Not a leap year"
    - Else: print "Leap year"
- Else: print "Not a leap year"
'''

# year = int (input("Enter any year in AD : "))
# if year%4 == 0:
#     if year%100 == 0:
#         if year%400 == 0:
#             print(f"{year} is a Leap Year!")
#         else:
#             print(f"{year} is not a Leap Year!")
#     else:
#         print(f"{year} is a Leap Year!")

# else: 
#     print(f"{year} is not a Leap Year!")

'''
5. Temperature Advice
Ask for the temperature.
- If temperature > 30:
    - If humidity > 70: print "Hot and humid"
    - Else: print "Hot"
- Else if temperature between 15 and 30:
    - If wind speed > 20: print "Pleasant but windy"
    - Else: print "Pleasant"
- Else: print "Cold"
'''
# temperature = float(input("Enter the Temperature : "))
# if temperature>30:
#     humidity = float(input("Enter the Humidity : "))
#     if humidity>70:
#         print("It is Hot and humid Weather!")
#     else:
#         print("It is Hot Weather!")
# elif (30>temperature>15):
#     windspeed = float(input("Enter the Windspeed : "))
#     if windspeed>20:
#         print("It is Pleasant but windy Weather!")
#     else:
#         print("It is Pleasant Weather!")
# else:
#     print("The Weather is COLD AF!")
'''
Create a nested-if program for shop discount.
If purchase is above 1000, check if customer has membership and provide 20% discount if not member provide 10%.
Print applicable discount.
'''
purchase_amount = float(input("Enter the purchase amount: "))
if purchase_amount > 1000:
    membership = input("Do you have a membership? (yes/no): ").strip().lower()
    if membership == 'yes':
        discount = 0.20 * purchase_amount
        print(f"Applicable discount: {discount}")
    else:
        discount = 0.10 * purchase_amount
        print(f"Applicable discount: {discount}")
else:
    print("No discount applicable")

# Create a nested-if program for shop discount.
# If purchase is above 1000, check if customer has membership and provide 20% discount if not member provide 10%.
# Print applicable discount.

