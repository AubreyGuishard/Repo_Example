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

while user_response != "y" or "Y" or "yes" or "Yes" or "YES":
    random_destination = random.choice(my_destinations)
    user_response = input(f"Is {random_destination} your place of choice? Y/N ")

print(f"Okay, {random_destination} is your place of choice! :)")    


# import random
# my_restuarants = ["Senia", "Kuzina", "Miss T's Kitchen", "Le Du", "Bistro"]


# import random
# mode_of_transportation = ["Plane", "Ship", "Train"]


# import random
# my_entertainment = ["Site seeing", "Swimming with dolphins", "Massage", "Riding four wheelers", "Ziplining"]