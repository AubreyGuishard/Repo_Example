# print("Hello World")
# (5 points): As a developer, I want to make at least three commits with descriptive messages 
# (5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 
# (5 points): As a user, I want a destination to be randomly selected for my day trip. 
# (5 points): As a user, I want a restaurant to be randomly selected for my day trip
# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.
# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, 
# and/or form of entertainment if I don’t like one or more of those things.


# my_destinations = ["Hawaii", "Greece", "Jamaica", "Thailand", "Uganda"]
# my_restuarants = ["Senia", "Kuzina", "Miss T's Kitchen", "Le Du", "Bistro"]
# mode_of_transportation = ["Plane", "Ship", "Train"]
# my_entertainment = ["Site seeing", "Swimming with dolphins", "Massage", "Riding four wheelers", "Ziplining"]


# Produce True or False (boolean)m from the user's input
#  What do we need for this user input:
# variable to capture user's response to the prompt
# prompt
# input function
# add Y/N in the input string


# response = input("Are you 18 or older? y/n ")
# if response == "y" or response == "Y" or response == "Yes" or response == "yes":
#     print("Here's your booze")
# else:
#      print("Sorry buddy get a ginger ale")

# Now we have to create a response (boolean) for either "y" or "n"
# If "y" print "Here's your booze"
#  If we have an expression (response == "y") then print it it will print a boolean

# print(response == "y" or response == "Y" or response == "Yes" or response == "yes")

# How do you get the for loop to select a random name off of the list you need to import random (Google: python random selection from list)


import random
instructors = ['Neven', 'David', 'JJ', "megan"]
# random_instructor = random.choice(instructors)
print(random_instructor)

user_response = " "

while user_response != 'y':
    random_instructor = random.choice(instructors)
    user_response = input(f"Is {random_suspect} the perptrator")

print(f"{random_suspect} has been detained")    
# for instructor in instructors: