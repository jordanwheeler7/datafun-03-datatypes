"""
Jordan Wheeler
29 January 2023
Project 3

This is to practice utilizing tuples and more!

"""
import math
import decimal as dec
import statistics as stats
import re


spacer = ("================================================================")


print()
print("Practice Tuples")
print()

# Tuples
workout_1_splits = (9, 10, 11, 8)
workout_2_splits = (8, 9, 10, 13)
workout_3_splits = (6, 9, 11, 7)

print()

# Concatenate Tuples
workout_measure = workout_1_splits + workout_2_splits + workout_3_splits
print("Workout Measurement is: {workout_measure}")

# Slice Tuple
mile_1 = workout_1_splits[0:1]
mile_2 = workout_2_splits[1:2]
mile_3 = workout_3_splits[3:4]

print("Mile 1 time was:", {mile_1})
print("Mile 2 time was:", {mile_2})
print("Mile 3 tiem was:", {mile_3})


# Tuple Reps

two_mile2 = mile_2 * 2
print(f"Double Mile 2:", {two_mile2})


# Tuple Membership Testing
hasNine = 9 in workout_1_splits
hasEleven = 11 in workout_2_splits

print(f"9 is in wourkout_1_splits", {hasNine})
print(f"11 is in workout_2_splits", {hasEleven})

print()

# Indexing

first_workout = workout_1_splits[0]
last_workout = workout_1_splits[-1]

print(f"The first workout split was {first_workout}.")
print(f"The last workout split was {last_workout}.")

print()

# Syntactic Sugar
print(f"{workout_1_splits = }")
print(f"{workout_2_splits = }")
print(f"{workout_3_splits = }")

print()
print(spacer)
print()

print("Practice with Sets")

print()

set1 = ("Dog", "Cat", "Bird", "Snake", "Iguana")
set2 = ("Bear", "Wolf", "Cat", "Dog", "Spider")

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

print()


print()
union_set = {set1}.union(set2)
intersection_set = {set1}.intersection(set2)

print(f"The union of set 1 and 2 is: {union_set}")
print(f"The intersection of set 1 and set 2 is: {intersection_set}")

print()

list_words = union_set
setwords = set(list_words)
ListWithNoDuplicate = list(setwords)
ListWithNoDuplicate1 = [setwords]
print(ListWithNoDuplicate)


print()

print(spacer)

print()

print("Practicing with Dictionaries")

print()

# Dictionary Terms

snakeA_dict = ["name:" "Brett", "age:", 2, "weight:", 1.8, "lbs"]
snakeB_dict = ["name:" "Jessica", "age:", 3, "weight:", 2.2, "lbs"]

assesment_dict = {"low": 0, "moderate": 1, "high": 2}

data_dict = {
    "name":["Bob", "Erin", "Tom", "Paco"],
    "age": [1, 3, 5, 7],
    "weight": [12, 15, 19, 21]
    
}

print(data_dict)

print()

with open("text_zen_of_python.txt") as file_object:
    word_list = file_object.read().split()
    
word_counts_dict = {}
for word in word_list:
    if word in word_counts_dict:
        word_counts_dict[word] += 1
    else:
        word_counts_dict[word] = 1
print(word_counts_dict)

print()
    
