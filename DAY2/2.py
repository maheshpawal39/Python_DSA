# 🟢 Level 1 — Loops
# # Q1. Print numbers
# 1 se 10 tak numbers print karo.

# for i in range(1,11):
#     print(i)

# Q2. Print even numbers

# 1 se 50 ke beech saare even numbers print karo.
# for i in range(1,51):
#     if i % 2 == 0:
#         print( "Even :" ,i)
#     # else:
#     #     print( "odd : " ,i)

# Q3. Sum of numbers

# 1 se n tak numbers ka sum find karo.

# Example:

# n = 5


# 1 + 2 + 3 + 4 + 5 = 15

# n = 5
# sum_1 = 0

# for i in range(1 , n+1):
#         sum_1 = sum_1 + i
# print(sum_1)

# Q4. Multiplication Table

# Given number ka table print karo.

# Example:

# 5 × 1 = 5
# 5 × 2 = 10
# ...
# 5 × 10 = 50

# num = 10

# for i in range(1,11):
#     print(num , "X" , i , "=", num*i)


# Q5. Count digits 🔥

# Given:

# num = 58392

# Output:

# 5

# def count(a):
#     print(len(a))

# # count("654123")    
# m = "mahesh"
# count(m)


# Q6. Sum of digits 🔥
# Input: 583

# Output:

# 16

# Because:

# # 5 + 8 + 3 = 16
# n = "524"
# count = 0

# for i in n:
#     count = count + int(i)
    
# print(count)    


# 🟡 Level 2 — Functions
# Q7. Even/Odd Function

# Ek function banao jo number le aur "Even" ya "Odd" return kare.

# def even(num):
#     if num % 2 == 0:
#         print("even :", num)
#     else:
#         print("odd", num )
# even(2)


# Q8. Maximum of 3

# Function ko 3 numbers do aur greatest number return karo.

# max() use nahi karna

# def graet(a,b,c):
#     if a > b and a>c :
#         return(a)
#     elif  b>a and b> c:
#         return(b)
#     else:
#         return(c)

# print(graet(50,20,30))

# Q9. Factorial

# Function banao:

# 5 → 120

# Because:

# 5 × 4 × 3 × 2 × 1 = 120

# def factorial(n):
#     result = 1
#     for i in range(1 , n + 1):
#          result = result * i
#     print(result)
         
         
# factorial(5)         

# Q10. Prime Number 🔥

# Function banao jo check kare number prime hai ya nahi.

# Example:

# 7 → Prime
# 8 → Not Prime

# Isko deeply solve karna, kyunki DSA mein prime-related logic baar-baar aayega.

# def is_prime(n):
#     count = 0
#     for i in range(1 ,n + 1):
#         if n % i == 0:
#             count += 1
         
#     if count == 2 :
#          return "prime"
     
#     else :
#         return "not prime"
    
# print(is_prime(8))    
# print(is_prime(7))    

# 🟠 Level 3 — Strings
# Q11. Count characters

# Given:

# "python"

# Output:

# 6

# a = "python"
# print(len(a))

# Q12. Count vowels

# Given:

# "education"

# Count vowels:

# 5

# Think about:

# a e i o u

# a  = "Mahesh"
# b = "aeiou"
# count = 0
# for i in a :
#     if i in b:
#         print(i)
#         count += 1
# # print(count)       

   
# Q13. Reverse String
# Input: "python"
# Output: "nohtyp"

# Pehle slicing se try karo, phir loop se bhi try karna.

# inp = "python"
# vapas = ""
# # print(inp[::-1])
# for i in inp:
#     vapas = i + vapas
# print(vapas)    
    
# Word = input("Enter a name ")

# if Word == Word[::-1]:
#     print("It is a palendroom")
# else:
#     print("its not")    
    
    
# Q15. Count a particular character
# Input: "banana"
# Character: "a"

# Output:

# 3

# Pehle .count() se karo.

# Then same problem loop se solve karo.

# word = "banana"
# cha = "a"
# count = 0
# # count = word.count(cha) 
# # print(count)
# for i in word:
#     if i == cha:
#         count += 1
        
# print(count)        

