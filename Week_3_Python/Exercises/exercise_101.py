# Define
# the
# following
# variables
# name, last_name, age, eye_color, hair_color
# name = ''
# last_name = ''
# eye_color = ''
# hair_color = ''
# age = ''
# Prompt user for input and Re-assign these

# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.

# Extra:
# Section 2 - Calculate in what year was the person born? and responde back.
# print something like: 'You said you we're 28 hence you were born in 1991!'

# Extra - Cast your input
#
# name = input("What is your full name?  ")
# age = input("How old are you?   ")
# #  = input("What's your date of birth? ")

print("What is your full name?")
my_name = input()
print("Nice to meet you " + my_name)
print("What is your eye colour?")
eye_colour = input()
print("Wow! I'm jealous, I wish I had eyes.")
print("What about your hair colour " + my_name + "?")
hair_colour = input()
print("That's Awesome! I have green hair...I think.")
print("So, " + my_name + " what is your favourite food?")
favourite_food = input()
print("Ah, your favourite food is " + favourite_food + " - mine too!")
print("mmm... " + my_name + ", Which year were you born (yyyy)? ")
age = int(input())
DOB = int(2020)
age_now = str(DOB - age)
print("Wow... that means your either are or going to be " + age_now + " this year, right?")
yes_no = input()
print("Well " + my_name + ", you don't look a day over 20!")
