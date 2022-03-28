#write a function that takes in two arguments
argument_one = "hello world"
argument_two = "hello mine friend"
two_args = argument_one + argument_two
print(two_args)

#write code to generate a tandom number between (0 - 99) and print result on the screen
import random

random_number = random.randint(0, 99)
print(random_number)

#while loop
#1. write a while loop to print ("Today, I am outstanding in every way") 4x
number = 0
while(number < 4):
    print("Today, I am outstanding in every way", number)
    number = number + 1

#1. write a for loop that says "I become what I think about most of the time" 200x
for i in range(200):
    print("I become what I think about most of the time", i)

#write code that asks a user for input and prints the message "You look great today, name"
user_input = int(input("You look great today, name:"))

#string operations
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#write a line of code to find the length of this string
#print the length on the screen 
the_length = len(alphabet)
print(the_length)

#write code to find the idex (position) of the letter 'j'
#print the index on the screen


from array import array
#create a new integet array using built in array method to store the class grades on the findal exam
class_grades = array['i', 90, 80, 70, 68, 99, 100]
#add another test scores to end of our array (append = add)
class_grades.append(100)
print(class_grades)

#print the length of the array on the screen
length = len(class_grades)
print("length of the array(number of scores): ", length)

#create a list of IGCSE computer science student names (list of strings) and include the name "Arsalon"
student_name = ["Mars", "Mike", "Leon", "Henry", "Arsalon"]

#sort the list of names using the built in sort method of Python and print on the screen
student_name.sort()

#create a dictionary (key-value pair)
#key = a string representing the student name
#value = list of integers representing scores on past three exams
#** inculde "Arsalon": [99, 100, 99]
the_student_name = dict(
   Leon=["88,78,99"],
   Mars=['78,88,99'],
   Arason=['99,100,99']
    )

#Using python's built in get method to retrieve "Arsalon"'s list of scores (list of integers) and print them on the screen
the_student_name = the_student_name.get("Adrain")
for score in the_student_name:
    print(score)