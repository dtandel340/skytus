# #1 Take a string input and print the length of the string
# name = input("Enter your string: ")
# lenght=len(name)
# print("Length of the string is:",lenght)

# #2 Take a string input and convert it to lowercase
# sentence=input("Enter a sentence: ")

# print(sentence.lower())

# #3 replace spaces with underscores in a string
# text = input("Enter a string:")
# print(text.replace(" ", "_"))

# #4 extract the first and last character of a string
# sentence = input("Enter a sentence: ")
# print("First character:", sentence[0])
# print("Last character:", sentence[-1])

# #5 reverse a string 
# string = input("Enter a string: ")
# reverse_string = string[::-1]

# print("Reversed string:", reverse_string)

# sentense = input("Enter a sentence: ")

# #6 check if word is presen t in sentence
# sentence = input("Enter a sentence: ")
# word= input("Enter a word to search in the sentence: ")

# if word in sentence:
#     print("word is present")
# else:
#     print("word is not present")

# #7 take name and age and print using f-string formating
# name="Deep"
# age =25 
# print(f"My name is {name} and i am {age} year old")

# #8 remove extra spaces form the start and end of the string

# string ="  i am a beginner of a python "

# print(string.strip())

# #9 join a list of two  words in to a single string with-Between them 
# string ="python is a very useful programming language  "
# add=["beginners", " ","for"]

# x="".join([string]+add)
# print(x)

# #10 create a list of your favorite movies and add a new movie to the list
# movies =["avengers","wolverine","Thor","Reacher","stranger things"]
# movies.append("spiderman")
# print(movies)

# #11 remove a movie from the list of favorite movies
# movies = ["avengers", "wolverine", "Thor", "Reacher", "stranger things"]
# movies.remove("Thor")
# print(movies)

# #12 remove a first movie from the list of favorite movies
# movies = ["avengers", "wolverine", "Thor", "Reacher", "stranger things","spiderman"]
# movies.remove(movies[0])
# print(movies)

# #13 sort a list of numbers in ascending order 
# numbers=[32,34,23,45,67,12,28,49,65]
# numbers.sort()
# print(numbers)

#14 reverse a list of numbers
# numbers=[32,34,23,45,67,12,28,49,65]
# numbers.reverse()
# print(numbers)

# #15 find the largest number in a list of numbers
# numbers=[32,34,23,45,67,12,28,49,65]
# large_number=max(numbers)
# print("The large number in the list is:", large_number)

# #16 merge two lists of numbers and print the merged list 
# numbers1=[32,34,23,45,67,12,28,49,65]
# numbers2=[12,34,56,78,90,23,45,67]
# merged_list = numbers1 + numbers2
# print("Merged list:", merged_list)

# #17 find the last number in a list of numbers without using index
# numbers=[32,34,23,45,67,12,28,49,65]
# last_number=next(reversed(numbers))
# print("The last number in the list is:", last_number)

# #18 create a nested list and acess a specific inner element
# my_list=[["name","Deep","maths",56,"science",60,"english",70],
#          ["name","Rahul","maths",60,"science",55,"english",65],
#          ["name","Rohit","maths",70,"science",75,"english",80]]

# print(my_list[2][1],"has scored",my_list[0][3],"in maths,",
#       my_list[0][5],"in the science")


# #19  count how many time an elements appear in alist 
# my_list1=["maths","science","english"]
# my_list2=["maths","science""english","hindi","sanskrit"]
# result =my_list2+my_list2
# print(result.count("maths"))
