#QUESTION
#. Explain using small program how to accept numbers in an list from user?

#SOLUTIONS

#I have considered this 2 lists as an example to show various methods of accepting numbers in list.
my_friends = ["anand", "shubham", "pranit", "amit", "swapnil"]
cool_numbers = [1 , 22, 54, 75, 120, 94, 33, 64]

#We can print the list by using simple print command.
#For Example:
print(my_friends)
print(cool_numbers)

#We can merge 2 lists using an append function.
#For Example:
my_friends.extend(cool_numbers)
print(my_friends)

#We can add any other element to a list using an append function.
#For Example:
my_friends.append("jeet")
cool_numbers.append(1230)
print(my_friends)
print(cool_numbers)

#We can insert a number at particular index position using a index function.
#For Example:
my_friends.insert(1, "pankaj")
print(my_friends)

#We can remove any element of a list using the remove function.
#For Example:
my_friends.remove("pranit")
print(my_friends)

#We can find out the index position of any element using .index function:
#For Example:
print(my_friends.index("amit"))
#if the element is not in the list then it is going to give an error.

#We can count the number of times a element id repeated using a count function.
#For Example:
print(my_friends.count("amit"))

#We can sort a list in desending order usinf reverse function
#For example:
my_friends.reverse()
print(my_friends)
cool_numbers.reverse()
print(cool_numbers)

#We can copy the whole elements of a list into another list using copy function.
#For Example:
another_friends = my_friends.copy()
print(another_friends)

#We can sort a list in asending order using sort function.
#For Example.
cool_numbers.sort()
print(cool_numbers)

#If we want to remove every element of a list then we use a clear function.
#For Example:
my_friends.clear()
print(my_friends)

#This is the required solution