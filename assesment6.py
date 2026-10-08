# #1 function to check if number is a prime 
# def check_prime(num):
#     if num > 1 and num % 2 != 0:
#         print("number is a prime")
#     else:
#         print("number is not prime")


# num = int(input("Enter your number: "))
# check_prime(num)

# #2 function to reverse a string 
# def reverse_str(text):
#     reverse = text[::-1]
#     print(reverse)


# text = input("Enter text: ")
# reverse_str(text)

# #3 function to find factorial
# def factorial(num):
#      fact=1
#      for i in range(1,num+1):
#           fact = fact *i
#           print("factorial:",fact)
# num=int(input("enter your number:"))
# factorial(num)

# #4 function to calculate simple intrest
# def simple_interest(p, r, t):
#     si = (p * r * t) / 100
#     print("Simple Interest:", si)


# p = float(input("Enter Principal: "))
# r = float(input("Enter Rate: "))
# t = float(input("Enter Time: "))

# simple_interest(p, r, t)


# #5 fuction to check if a word is palindrome
# def palindrome(text):
#     if text == text[::-1]:
#         print("text is palindrome")
#     else:
#         print("text is not palindrome")

# text=input("enter your text:")
# palindrome(text)

# #6 function to count vowels in a string
# def count_vowels(text):
#     count = 0

#     for char in text:
#         if char in "aeiou":
#             count = count + 1

#     print("Number of vowels:", count)


# text = input("Enter a string: ")
# count_vowels(text)

# #7 function to merge two list 
# def merge(list1,list2):
#     sum=list1+list2
#     print(sum)
#     return sum 
# merge([1,3,4,6],[12,13,23,34])

# #8 Function to find gcd of two numbers 

# def gcd_num(num1,num2):
#     a= num1
#     b= num2
#     while b != 0:
#        a,b=b,a%b 
#        return a
   
# print(gcd_num(60,48))

# #9 function to find area of ractangle 
# def rec_num(x,y):
#    z = x*y
#    print ("area of ractangle is :",z)

# x=int(input("enter lenght:"))
# y=int(input("enter a width:"))

# rec_num(x,y)
    
# #10 fuction to check armstrong number 

# def arm_num(n):
#     t=n 
#     p=len(str(n))
#     s=0

#     while t > 0:
#         d= t % 10 
#         s += d ** p
#         t //=10

#     if s==n :
#             print("armsrong number ")
#     else:
#             print("not an armstrong number ")

# arm_num(153)


   
