#1 write a program to handle divison by zero error 

a=int(input("enter a first number:"))
b=int(input("enter a second number:"))

if b ==0 :
    print("Error: can not dicide by zero")
else:
    result=a/b
    print("Result:",result)

#2 write a program to handle invalid integer input

try:
    num = int(input("Enter an integer: "))

    if num == int(num):
        print("Valid integer")
    else:
        print("Invalid integer")

except ValueError:
    print("Invalid integer")
 
#3 write a program to open a file amd handle the "file not found error "

try:
    file=open("python.txt","r")
    print(file.read())
    file.close()

except  FileNotFoundError:
    print("error : File not found!")

#4 write a program to demonstrate multiple exception blocks 
try:
    num1=int(input("enter number:"))
    num2=int(input("enter a number:"))

    result=num1/num2 
    print("result:",result)

except  ValueError:
    print("error:please enter integer only")
except ZeroDivisionError:
    print("Error:can not Divide by zero")

#5 write a program to use finally for resource cleanup.
try:
    file=open("python.txt","r")
    print(file.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("resource cleanup completed")

#6 write a program to create a custom exception for invalid age (<18)
try:
    age=int(input("Enter your age:"))

    if age <18:
     print("invalid age")
    else:
       print("valid age")
except ValueError:
   print("enter the int value ")

#7 write a program to handle indexerror when acessing a list 

my_list=[10,20,30]
try:
    
    index=int(input("Enter index:"))
    print(my_list[index])
except IndexError:
    print("Error:list index out of range")

#8 write a program that takes two numbers and handle all possible errors 
try:
    num1=int(input("Enter number:"))
    num2=int(input("Enter number:"))

    result=num1/num2
    print("result:",result)

except ValueError:
    print("Error:enter valid number")
except ZeroDivisionError:
    print("Error:number is not Divide by zero")
except Exception:
    print("something went wrong!")

#9 write a program to log errors to a file inestead of printing them
try:
    num=int(input("Enter a number:"))
    result=10/num
    print("Result",result)

except Exception as e:
    file=open("error.txt","w")
    file.write(str(e)+"\n")
    file.close()

#10 write a program that validates an email format and raises an exception for invalid once.

try:
    email = input("Enter your email: ")

    if "@" not in email or "." not in email:
        print("Email is invalid")
    else:
        print("Email is valid")

except ValueError:
    print("Invalid input!") 