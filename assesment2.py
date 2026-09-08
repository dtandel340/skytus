#1 calculate the reminder of two numbers

num1 =int(input("Enter a First Number: "))
num2=int(input("Enter a Second Number: "))

reminder = num1 % num2

print("Reminder",reminder)

#2 check if a number is even or odd

num =int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#3 calculate the square and cube of a number

num=int (input("Enter a number: "))
square = num ** 2
cube = num ** 3

print("Square of the number is:", square)
print("Cube of the number is:", cube)

#4 find the largest of two numbers

num1=int(input("Enter a First Number: "))
num2=int(input("Enter a Second Number: "))

if num1 > num2:
    print( "larger number is:", num1)
else:
    print("larger number is:", num2)


#5 check if two numbers are equal or not

num1 = int(input("Enter a First Number: "))
num2 = int(input("Enter a Second Number: "))

if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

num1=int(input("Enter a First Number: "))
num2=int(input("Enter a Second Number: "))

#6 check if both numbers are positive

if num1 > 0 and num2 > 0:
    print("true")
else:
    print("false")

#7 convert a float number to an integer

num=float(input("Enter a number: "))
integer_num=int(num)
print("Integer value:", integer_num)

#8 convvert a num to int and multiply it by 10
num= input("Enter a number: ")

num= int(num)
result= num * 10
print("Result :", result)

#9 check if a number is between 1 and 99 or not

num = int(input("Enter a number: "))

if num > 0 and num< 100:
    print("The number is between 1 and 99.")
elif num == 0 or num == 100:
    print("The number is either 0 or 100.")
else:
    print("The number is outside the range .")

#10 divide two numbers and print the quiontent and remainder sepratly

num1 = int(input("Enter a First Number: "))
num2 = int(input("Enter a Second Number: "))

quotient = num1 // num2
remainder = num1 % num2

print("Quotient:", quotient)
print("Remainder:", remainder)