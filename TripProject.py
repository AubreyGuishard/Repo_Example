# (5 points): As a developer, I want to make at least three commits with descriptive messages 
# (5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation,
#  and entertainment in their own separate Lists. 
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


import random
my_destinations = ["Hawaii", "Greece", "Jamaica", "Thailand", "Uganda"]

user_response = " "

while user_response != "y" and user_response != "Y" and user_response != "yes" and user_response != "Yes" and user_response != "YES":
    random_destination = random.choice(my_destinations)
    user_response = input(f"Is {random_destination} your place of choice? Y/N ")

# print(f"Okay, {random_destination} is your place of choice! :)")    


# import random
my_restuarants = ["Senia", "Kuzina", "Miss T's Kitchen", "Le Du", "Bistro"]

user_response = " " 

while user_response != "y" and user_response != "Y" and user_response != "yes" and user_response != "Yes" and user_response != "YES":
    random_restuarant = random.choice(my_restuarants)
    user_response = input(f"Is {random_restuarant} your restuarant choice? Y/N ")

mode_of_transportation = ["Plane", "Ship", "Train"]

user_response = " "

while user_response != "y" and user_response != "Y" and user_response != "yes" and user_response != "Yes" and user_response != "YES":
    random_transportation = random.choice(mode_of_transportation)
    user_response = input(f"Is {random_transportation} your choice of transportation? Y/N ")


my_entertainment = ["Site seeing", "Swimming with dolphins", "Get a Massage", "Riding four wheelers", "Ziplining"]

user_response = " "

while user_response != "y" and user_response != "Y" and user_response != "yes" and user_response != "Yes" and user_response != "YES":
    random_entertainment = random.choice(my_entertainment)
    user_response = input(f"Is {random_entertainment} your choice of entertainment? Y/N ")

print(f"Okay, {random_destination} is your place of choice. {random_restuarant} is your resturant of choice. You want to get there by {random_transportation} and you want to {random_entertainment}! :)")


# import random
# mode_of_transportation = ["Plane", "Ship", "Train"]


# import random
# my_entertainment = ["Site seeing", "Swimming with dolphins", "Massage", "Riding four wheelers", "Ziplining"]