#1 write a program to print your name, age and city

Name ="Deep"
age="25"
city="Billimora"

print(
    Name,age,city
)

#2 write a program to calculate sum of two numbers

num1 = float(input("Enter a First Number: "))
num2 = float(input("Enter a Second Number: "))
sum = num1 + num2
print("sum=",sum)

#3 write program to convert celsius to fahrenheit

celsius= float(input("Enter a temperature in Celsius: "))
fahrenheit= (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

#4 store your name in a variable and print it in upper case
name ="Deep"
print(name.upper())

#5 ask the user for their birth year and calculate their age based on the current
from datetime import datetime
birth_year = int(input("Enter your birth year: "))
current_year = datetime.now().year
age = current_year - birth_year
print("Your age is:", age)

#6 write a program to swap two numbers
a=10
b=20

a,b = b,a

print ("a=",a)
print ("b=",b)

#7 write a program to calculate the area of rectangle
lenght =float(input("Enter the length: "))
width =float(input("Enter the width: "))

area = lenght * width
print("Area of rectangle is:", area)

#8 write a program to check if a number is positive, negative or zero
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#9 write a program to calculate the average of two numbers
num1 =float(input("Enter a First Number: "))
num2 =float(input("Enter a Second Number: "))

average = (num1 + num2) / 2
print("Average:", average)