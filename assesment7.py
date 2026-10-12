#1 write a program to read a file and display it contents
file =open("assesment4.py","r")
content=file.read()
print (content)
file.close()

#2 write a program to count the number of lines in a file 
file =open("assesment2.py","r")
content=file.read()
print(len(content))

#3 wite a program to count how many times each words appear in a file 
file =open("python.txt")
content=file.read()

words =content.split()

word_count= {}

for word in words :
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

        for word,count in word_count.items():
            print(word,":",count)

#4 write a program to write 5 user-enterd sentece to a file 
file = open("python.txt","w") 

for i in range(5):
    sentence=input("Enter a sentence :")
    file.write(sentence +"\n" )
  
    print ("sentence saved sucessfully")

#5 wirte a program to read a file and print only lines containing a specific word.
word =input("enter a word to search: ")
file=open("python.txt")
content=file.read()

for line in content.split("\n"):
     if word in line:
      print(line)

#6 write a program to replace a specific word in a file and save cahnges 
old_word=input("enter the old word: ")
new_word=input("enter the new word: ")

file=open("python.txt","r")
content=file.read()
file.close()

content= content.replace(old_word,new_word)
file =open("python.txt","w")
file.write(content)
file.close()
print("word replace sucessfuly.")

#7 write a program to merge the contents of two text file in to third file 

file1=open("first.txt","r")
content1=file1.read()
file1.close()

file2=open("second.txt","r")
content2=file2.read()
file2.close()

file3=open("third.txt","w")
file3.write(content1)
file3.write("\n")
file3.write(content2)
file3.close()

print("file merged sucessfully")

#8 write a program to read a csv file and display it content in a formated way
import csv

file=open("students.csv","r")
reader=csv.reader(file)

for row in reader :
    print("|".join(row))

#9 write a program to backup a file by copying its content into another file 
file1=open("python.txt","r")
content=file1.read()
file1.close()

file2=open("backup.txt","w")
file2.write(content)
file2.close()

print ("backup created sucessfully")