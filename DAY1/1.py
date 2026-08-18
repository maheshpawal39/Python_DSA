# Number = int(input("Enter your Number : "))
# e = "Even"
# o = "odd"


# if Number % 2 == 0 :
#     print("Input","=",Number)
#     print("output", "=", e)
# else:
#     print("Input","=",Number)
#     print("output", "=", o)

# Q2. Positive, Negative or Zero

# if Number > 0 :
#     print(Number," is Positive ")
# elif Number < 0:
#     print(Number , "is Negative ")
# else :
#     print("ZERO")    

# Q3. Greater of Two Numbers

# a = int(input("Enter Number of a : "))
# b = int(input("Enter Number of b : "))

# if a > b :
#     print("Input :")
#     print("Value of " ,a)
#     print("Value of " ,b)
#     print("output")
#     print(a)
# else :
#     print("Input :")
#     print("Value of " ,a)
#     print("Value of " ,b)
#     print("output")
#     print(b)

# Q4. Greatest of Three Numbers

# a = int(input("Enter Number of a : "))
# b = int(input("Enter Number of b : "))
# c = int(input("Enter Number of c : "))

# if a >= b and a >= c:
#     print("The value of a is greter form all" , a)
# elif b >= a and b >= c:
#     print("The value of b is greter form all" , b)
# else :
#     print("The value of c is greter from all " , c)

# Q5. Divisible by 5

# if Number % 5 == 0:
#     print("YES")
# else:
#     print("NO")    


# Q6. Divisible by both 3 and 5
# if Number % 3 == 0 and Number % 5 == 0 :
#     print("YES")
# else:
#     print("NO")    

# Q7. Leap Year
# year = int(input("Enter a your Year : "))
# y = "Leap Year"
# n = "Not a Leap Year"
# if year % 400 == 0 :
#     print("Input" , year )
#     print("output : " , y)
# elif year % 100 == 0:
#     print("Input" , year )
#     print("output :" , n)   
# elif year % 4 == 0:
#     print("Input" , year )
#     print("output :" , y)
# else:
#     print("output : ", n)       

# Q8. Profit or Loss
# a = int(input("Enter Value of cost price : "))
# b = int(input("Enter Value of selling price  : "))

# if a < b :
#     print("Profit" , b - a)
# elif a > b :
#     print("Lose" , a - b)
# else:
#     print("ZERO")    

# Q9. Electricity Bill

# Given units consumed:

# First 100 units → ₹5/unit
# Next 100 → ₹7/unit
# Above 200 → ₹10/unit

# Calculate total bill.

# unit =  int(input("Enter unit : "))

# if unit < 100 :
#     bill = unit*5
# elif unit < 200 :
#     bill = (100   * 5) + ((unit - 100) * 7)
# else:
#     bill = (100 * 5) + (100 * 7) + ((unit - 200) * 10)

# print("units " , unit)
# print("Total Bill ",  bill ) 

# q10
# a = int(input("Enter side a: "))
# b = int(input("Enter side b: "))
# c = int(input("Enter side c: "))

# if a + b > c and b + c > a and a + c > b:
#     print("Valid Triangle")
# else:
#     print("Invalid Triangle")


# Q11. Find Middle Number

# Given three different numbers:

# 10 50 30

# Output:

# 30

# Without using sort().
# a = int(input("Enter a "))
# b = int(input("Enter b "))
# c = int(input("Enter c "))
# if (a > b and a < c) or (a < b and a > c):
#     print(a)
# elif(b > a and b < c) or (b < a and b > c):
#     print(b)

# else :
#     print(c)        

# num = input("Enter value of : ")
# if num.isupper():
#     print("Uppercase")

# elif num.islower():
#     print("Lowercase")    

# elif num.isdigit():
#     print("Digit") 

# else:
#     print("special charactors")

# student eligibility :

# Maths = int(input("Enter a values of Maths : "))
# English = int(input("Enter a values of English : "))
# Hindi = int(input("Enter a values of Hindi : "))

# total = Hindi+ English+ Maths

# if Maths >= 60 and English >= 50 and Hindi >= 40 and total >= 200:
#     print("Eligible")
# else:
#     print("NotEligible")    

# Q14. Calculator

# Input:

# 10 5 +

# Output:

# 15

# Handle:

# +
# -
# *
# /

# # Yahan if-elif ka proper use hoga.
# a = int(input("Enter a vlaur of a :"))
# b = int(input("Enter a vlaur of b :"))

# op = input("Enter oprator")

# if op == "+":
#     print(a+b)

# elif op == "-":
#     print(a-b)    
# elif op == "*":
#     print(a*b)    
# elif op == "/":
#     print(a/b)    
# else :
#     print("Invalied op ")    


# Q15. Number Classification 🔥

# Given an integer:

# If divisible by both 2 and 3 → "Divisible by both"
# If only 2 → "Divisible by 2"
# If only 3 → "Divisible by 3"
# Otherwise → "Neither"

# Example: 

# num_1 = int(input("Enter a value : "))

# if num_1 % 2 == 0 and num_1 % 3 == 0:
#     print("Divisible by both")
# elif num_1 % 2 == 0:
#     print("Divisible by 2")
# elif num_1 % 3 == 0:
#     print("Divisible by 3")
# else :
#     print("Invalied")        