# Q1. Last Digit
# Given an integer, find its last digit without converting it to string.

# Example:
# Input: 4786
# Output: 6

# num = "5168416841"

# for i in num:
#     pass
# print(i)

# num = 5168
# last = num % 10
# print(last)

# Q2. Swap Without Third Variable
# Given two numbers, swap them without using a third variable.

# Example:
# a = 10, b = 20
# Output: a = 20, b = 10

# a = 10 
# b = 20

# a ,b = b , a
# print( "a", a)
# print("b" ,b)

# Q3. Three-Digit Number Check
# Check whether a given number contains exactly 3 digits.
# Handle positive and negative numbers too.

# num = int(input("Enter a number : "))
# # abs ka usse isliye  kiya kiuki abs (-) ko hata deta he 
# if 100 <= abs(num) <= 999:
#     print("three digit number")
# else :
#     print("Not a three digit number")    

#Q4. Sum of Even and Odd Digits
# Given:
# Input: 583214

# Find separately:
# Sum of even digits = ?
# Sum of odd digits = ?

# # num = "22"
# # count = 0
# # for i in num:
# #     if num == num % 10:
# #         count += 1
# #         print("sum of even digit : ", count)
# #     elif num == num // 10:
# #         count += 1
        
# #         print("sum of odd digit : ", count)

# num = 231
# even_sum = 0
# odd_sum = 0

# while num > 0:
#     digit = num % 10
    
#     if num % 2 == 0:
#         even_sum += digit
        
#     else :
#         odd_sum += digit
        
#     num = num // 10
    
# print(even_sum)    
# print(odd_sum)    

# Q5. Largest Digit in a Number 🔥
# Input: 583921
# Output: 9

# Don't convert the number into a string.
# n = 1223456789
# large = 0

# while n > 0:
#     digit = n % 10 
#     if digit > large:
#         large = digit
#     n = n // 10 
# print(large)    

# n = 562145
# small = 9
# while n > 0:
#     digit = n % 10
#     if digit < small:
#         small = digit
        
#     n = n // 10
# print(small)        

# Q7. Count Even and Odd Digits
# Input: 583921

# Output should tell:
# Even digits = ?
# Odd digits = ?

# n = 583921

# even = 0
# odd = 0

# while n > 0:
#     digit = n % 10

#     if digit % 2 == 0:
#         even += 1

#     else:
#         odd += 1
#         # yahan kya karna hai?

#     n = n // 10

# print("Even digits =", even)
# print("Odd digits =", odd)

# def perfect(n):
#     total = 0
#     for i in range(1 , n):
#         if n%i == 0 :
#             total += i
#     if total == n:
#         print("Perfect Number")         
#     else:
#         print("Not Perfect Number")
# perfect(2)

