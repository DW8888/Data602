### Darwhin Gomez Assignment 1
# #Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

high_score = 95
 
# Get the test scores.
test1 = int(input('Enter the score for test 1: '))
test2 = int(input('Enter the score for test 2: '))
test3 = int(input('Enter the score for test 3: '))
# Calculate the average test score.
average = (test1 + test2 + test3) / 3
# Print the average.
print('The average score is', average)
# If the average is a high score,
# congratulate the user.
if average >= high_score:
    print('Congratulations!')
    print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 
length = int(input('Enter the length of the rectangle: '))
width = int(input('Enter the width of the rectangle: '))
length2 = int(input('Enter the length of the rectangle 2: '))
width2 = int(input('Enter the width of the rectangle 2: '))
area_rect1= length * width
area_rect2= length2 * width2
print('The area of the first rectangle is: ', area_rect1)
print('The area of the second rectangle is: ', area_rect2)


#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.
name=input('What is your name? ')
age= int(input('What is your age? '))
msg=f"Happy birthday, {name}!  You are {age} years old today!"
print(msg)

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"


