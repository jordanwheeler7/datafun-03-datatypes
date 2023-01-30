"""
Optional bonus. See course site for details.

>>> len(longwordset1)
415

>>> len(longwordset2)
197

>>> len(longwords)
13
"""

import doctest

# read from second file and get a list of words

with open("text_hamlet.txt", "r") as f1:
    text = f1.read()
    wordlist1 = text.split()  # split on whitespace

# read from second file and get a list of words

with open("text_juliuscaesar.txt", "r") as f2:
    text = f2.read()
    wordlist2 = text.split()  # split on whitespace

# Done with files - let the files close and the work begin

# Remove duplicates by creating two sorted sets
# hint: use sorted() to sort the list
# hint: use set() to remove duplicates
# name them wordset1 and wordset2

sorted_list = sorted(wordlist1)
sorted_list2 = sorted(wordlist2)
wordset1 = set(wordlist1) 
wordset2 = set(wordlist2) 


# initialize a variable maxlen = 10
maxlen = 10 

# use a list comprension to get a list of words longer than 10


longwordset1 = set([word for word in wordset1 if len(word) > 10])
longwordset2 = set([word for word in wordset2 if len(word) > 10])  

# find the intersection of the two sets

longwords = longwordset1 & longwordset2

# print the length of the sets and the list
print(f"Number of words with over 10 letters in Hamlet", len((longwordset1)))
print("Number of words with over 10 letters in Julius Caesar", (len(longwordset2)))
print("Long words in both", len(longwords))
print()
print(f"Similar long words in both {sorted(longwords) = }")
print()

# check your work
print("TESTING...if nothing prints before the testing is done, you passed!")
doctest.testmod()
print("TESTING DONE")
