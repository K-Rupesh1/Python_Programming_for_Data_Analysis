#1:Creating and Accessing Sets
#Create a set with the first 10 positive integers. Print the set.
my_set=set(x for x in range(1,11) )
print(my_set)

#2: Adding and Removing Elements
#Add the number 11 to the set created in Assignment 1. 
#Then remove the number 1 from the set. Print the modified set.
my_set.add(11) # append is not used for set.
print(my_set)
my_set.remove(1)
print(my_set)

#3: Set Operations
#Create two sets: one with the first 5 positive integers 
# and another with the first 5 even integers. 
# Perform and print the results of union, intersection, difference, 
# and symmetric difference operations on these sets.

my_set1=set(x for x in range(1,6))
print(my_set1)
my_set2=set(x for x in range(1,11) if x%2==0)
print(my_set2)
result=my_set1.union(my_set2)
print(f"union : {result}")
result=my_set1.intersection(my_set2)
print(f"intersection : {result}")
result=my_set1.difference(my_set2) #Returns elements that are present in the first set but not in the second set.
print(f"difference : {result}")
result=my_set1.symmetric_difference(my_set2) #Returns elements that are present in either set, but not in both.
print(f"symmetric difference : {result}")

#4: Set Comprehensions 
"""note:set comprehension is a short way to create a set using a for loop in a single line."""
#Create a new set containing the squares of the first 10 positive integers using a set comprehension. 
# Print the new set.
myset=set(x**2 for x in range(1,11))
print(myset)
print(sorted(myset))

#5: Filtering Sets
#Create a new set containing only the even numbers from the set created in Assignment 1 using a set comprehension. 
# Print the new set.
new_set={x for x in my_set if x%2==0}
print(new_set)

#6: Set Methods
#Create a set with duplicate elements and 
#remove the duplicates using set methods. Print the modified set.

my_set={1,2,1,3,2,4,3,4}
result=set(my_set)
print(result)

#7: Subsets and Supersets
#Create two sets: one with the first 5 positive integers and 
# another with the first 3 positive integers. 
# Check if the second set is a subset of the first set 
# and if the first set is a superset of the second set. 
# Print the results.
set1={x for x in range(1,6)}
print(set1)
set2={x for x in range(1,4)}
print(set2)
result=set2.issubset(set2)
print(result)
result1=set1.issuperset(set2)
print(result1)

#8: Frozenset
#Create a frozenset with the first 5 positive integers. Print the frozenset.
my_set=frozenset(x for x in range(0,6))
print(my_set)
print(type(my_set))

#9: Set and List Conversion
#Create a set with the first 5 positive integers. 
# Convert it to a list, append the number 6, 
# and convert it back to a set. Print the resulting set.
my_set=set(x for x in range(0,6))
my_list=list(my_set)
my_list.append(6)
my_set=set(my_list)
print(my_set)

#10: Set and Dictionary
#Create a dictionary with set keys and integer values. Print the dictionary.
my_set=set(x for x in range(0,6))
values=[x for x in range(6,11)]
dictionary=dict(zip(my_set,values)) # zip method pairs elements together
print(dictionary)

#11: Iterating Over Sets
#Create a set and iterate over the elements, printing each element.
my_set=set(x for x in range(0,6))
for i in my_set:
    print(i)
    
#12: Removing Elements from Sets
#Create a set and remove elements from it until it is empty. Print the set after each removal.
my_set=set(x for x in range(0,6))
for i in range(0,len(my_set)):
    if i in my_set:
        my_set.remove(i)
        print(my_set)
        
#13: Set Symmetric Difference Update
#Create two sets and update the first set with the symmetric difference of the two sets. 
#Print the modified first set.
set1={x for x in range(1,6)}
set2={x for x in range(1,4)}
set1=set1.symmetric_difference(set2)
print(set1)

#14: Set Membership Testing
#Create a set and test if certain elements are present in the set. Print the results.
set1={x for x in range(1,6)}
'''if 1 in set1:
    print("the element is present")'''
print(1 in set1)
print(6 in set1)

#15: Set of Tuples
#Create a set containing tuples, where each tuple contains two elements. Print the set.
my_set={(0,1),(2,3),(4,5),(6,7)}
print(type(my_set))
print(my_set)
    
