"""
Jordan Wheeler
28 January 2023
Project 3

"""

# imports first

import math
import statistics as stats
import decimal as dec


# reusable functions next

"""

listw is a list of weights used during the last training session 

"""
listw = [315,
         310,
         235, 
         225, 
         215, 
         205, 
         195, 
         185, 
         175, 
         155, 
         135, 
         135
         ]

"""
listx formulates our weights into an integer

"""

listx = list(range(11))

"""
listy is the amount of reps preformed during our last session

"""

listy= [3,
        6,
        8,
        8,
        10,
        12,
        12,
        14,
        13,
        10,
        10
]


spacer = "==============================================="




# call functions and execute code

print("List 1: Central Tendencies")


"""
Calculate the Central Tendencies

"""

print()
print()

mean = stats.mean(listw)
median = stats.median(listw)
mode = stats.mode(listw)
variance = stats.pvariance(listw)
std_deviation = stats.stdev(listw)

print(f"List 1: List Statistics")
print()
print(f"Mean of weight lifted:", round(mean, 2))
print(f"Median of weight lifted:", round(median, 2))
print(f"Mode of weight lifted:", round(mode, 2))
print(f"Variance of weight lifted:", round(variance, 3))
print(f"Standard deviation of weight lifted:", round(std_deviation, 3))



print()
print(spacer)
print(f"Sometimes we may want to see if there are any\
        relationships between weight and number of reps.\
        This section will explain those relationships.")

# Calculate different relathionships and 
# predict future weight at 1 rep

slope, intercept = stats.linear_regression(listx, listy)
correlation_reps_weight = stats.correlation(listx, listy)
lbs_future = 15
rep_future =  slope * lbs_future + intercept

# Provide print statements for user review

print("List 2: Lists-Correlation and Prediction")
print()
print(f"The correlation between weight and reps is:", {round(correlation_reps_weight, 2)})
print(f"The slope of the best fit line is:",{round(slope, 2)})
print(f"The intercept of the best fit line is:", {round(intercept, 2)})
print(f"Utilizng this information, our future reps at 155 lbs is:", {round(rep_future)})

print()
print(spacer)
print()

print("List 3: Lists-Using Python Built-in Functions")

"""
Calculate for the min, max, len, sum\
average, set, sorted, sorted () reverse true

"""
minimum = min(listw)
maximum = max(listw)
length = len(listw)
total = sum(listw)
average_1 = total / length
set_info = set(listw)
sorted_list = sorted(listw)
sorted_reverse = sorted(listw, reverse=True)

# Print readable information for users.

print(f"The minimum weight was: {listw}")
print(f"The maximum weight was: {maximum}")
print(f"The number of sets done was: {length}")
print(f"The total weight lifted was: {total}")
print(f"The average weight lifted was: {average_1}")
print(f"The weight set was: {set_info}")
print(f"The sorted list for our weight was:",  sorted_list)
print(f"The descending sorted list for our weight was:", sorted_reverse)


print()
print(spacer)
print()


print("List 4: List methods")

"""
Make a new short list named lst and explore list methods: 
append, extend, insert, remove, count, sort, sort w/ reverse
copy, pop first, pop last
  
"""

print()

# Short List named lst

lst = [7, 13, 21, 23, 56, 63, 99]
print(f"Lst: {lst}")

# Append a valule

lst.append(3)
print(f"List with Appended", lst)

# Extend list with new list

lst.extend([22, 27, 35])
print(f"Extend lst: {lst}")

# Insert a value at index 4
lst.insert(1, 4)
print(f"lst with insert: {lst}")

# Remove value 4 from list
lst.remove(4)
print(f"List minus value 4: {lst}")

# Count how many times 21 shows up in list
print(f"21 appears {lst.count(21)} times in lst.")

# Sort lst
lst.sort()
print(f"lst sorted ascending: {lst}")

# Descending lst
lst.sort(reverse=True)
print(f"lst sorted descending: {lst}")

# Copy of lst

lst_copy = lst.copy()
print(f"Copy of lst: {lst}")

# Pop first list item
first = lst.pop(0)
print(f"The first value in our list is: {first}")

# Pop last item
last = lst.pop(-1)
print(f"The last item on our list is: {last}")

print()
print(spacer)
print()

print("List 5: List Transformations- filter and map")

"""
Using fliter and map on listy

"""

if __name__ ==" __main__ ": 
        
        
        print()

listx_evens = list(filter(lambda x: x % 2 == 0, listw))
listy_cubes = list(map(lambda x: x**3, listw))
listy_vol = list(map(lambda x: x * x * x, listw))

print(f"The even weight ranges completed are: {listx_evens}")
print()
print(f"The cube of each rep in the list are: {listy_cubes}")
print(f"The volume of cubes with equal sides in listy are: {listy_vol}")

print()
print(spacer)
print()

print("Lists 6: List Transformations Using List Comprehension")

print()

# Get odd values from listw

getx = [x for x in listw if x > 165]
print(f"The weights utilized over 165 lbs was: {getx}")

# Triple each value

getx3 = [x * 3 for x in listw]
print(f"If we tripled each weight utilized, we would have: {getx3}")

# Convert each weight to kilograms

get_kg = [round(x * .45359237, 2) for x in listw]
print(f"If you need weights in kg for listw they are as follows: {get_kg}")

print()
print(spacer)
print()