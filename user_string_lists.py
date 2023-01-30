"""
Jordan Wheeler
28 January 2023
Project 3

"""

# imports first

import random

# Types of Training and characteristics

types_of_training = ["HIIT", "STRENGTH", "CARDIO", "HICT", "YOGA", "POWERLIFTING"]

training_goal = ["FLEXIBILITY", "GET STRONG", "IMPROVE HEALTH", "COMPETE", "RELAX", "MARATHON TRAIN"]

gym_lifts = ["BENCH", "SQUAT", "DEADLIFT", "PULLUPS", "MACHINES"]

running_style = ["SHORT DISTANCE", "MEDIUM DISTANCE", "LONG DISTANCE", "SPRINTS", "INTERVAL"]

length_workout = ["QUICK", "MEDIUM", "LONG", "FAST PACED", "SLOWER PACED"]


spacer = "=========================================================================================="
short_spacer = "============"


print()
print("String Lists 1: Using Python Built-in Functions")

"""
Use built-in functions: len, ,set, and zip

"""

print()

# Utilizing Length

print(f"The length of types of training is {len(types_of_training)}")
print(short_spacer)

# Utilizing Set
print(f"The unique training goals are: {set(training_goal)}")
print(short_spacer)

# Combine Lists Utilizing Zip
running_tuple = zip(running_style, training_goal, length_workout)
print(f"This is a tuple of running styles, training goals, and length of workout: {list(running_tuple)}")

print()
print(spacer)
print()

print("String Lists 2: Random Choice")

"""
Use random choice to pick a random value from one of\
your lists

"""

print()

print(f"Let's utilize random choice to see what we can get!")
print({random.choice(gym_lifts)})

print(short_spacer)

print()

# Define Names
list_names = ["Aaron", "Ashley", "Hank", "Rylynn", "Jeph", "Tina"]

# Define Lifts
list_lifts = ["Bench", "Squat", "Deadlift"]

# Define Calls
list_calls = ["Light", "Moderate", "Heavy"]

# Define Rep Range
list_rep = ["6", "8", "10", "14", "18", "24"]

# Define Adjectives
list_adj = ["Good", "Bad", "Tolerable"]

# Define Encouragement
list_encourage = ["You're doing great!", 
                  "You're gonna love the results!"
                  "We can muscle through this!",
                  "Almost done!"]

# Create A Random Sentence

sentence = (
    f"Hi! My name is {random.choice(list_names)}! We will be doing the {random.choice(list_lifts)}! We will complete this at a {random.choice(list_calls)} weight\
    for a total of {random.choice(list_rep)} reps! This is gonna feel {random.choice(list_adj)}, however, {random.choice(list_encourage)}!")


print()
print()
print(sentence)
print()
print()   

print(spacer)
print()

print("String Lists 3: Get Unique Words")
"""
Use open, read, split, and set to read a text file and get a list of unique words.

"""

print()

with open("text_juliuscaesar.txt", "r") as file:
    text = file.read()
    list_words = text.split()
    unique_words = set(list_words)
    
unique_words_sorted = sorted(unique_words)
unique_words_count = len(unique_words_sorted)
print(f"Julius Caesar has {unique_words_count} unique words!")

print()

