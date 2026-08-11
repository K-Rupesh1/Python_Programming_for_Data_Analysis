#1: Creating and Accessing Dictionaries
#Create a dictionary with the first 10 positive integers as keys and their squares as values.
#Print the dictionary.
d={i:i*2 for i in range(1,11)}
print(d)

#2: Accessing Dictionary Elements
#Print the value of the key 5 and the keys of the dictionary created in Assignment 1.
print(f"value of the key 5 {d[5]}")
print(f"keys of te dictionary {d.keys()}")

#3: Dictionary Methods
#Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 
#and then remove the key-value pair with key 1. Print the modified dictionary.
d[11]=121
d.pop(1)
print(f"modified dictionary {d}")

#4: Iterating Over Dictionaries
#Iterate over the dictionary created in Assignment 1 and print each key-value pair.
for key,values in d.items():
    print(key,values)
    

#5: Dictionary Comprehensions
#Create a new dictionary containing the cubes of the first 10 positive integers using 
#a dictionary comprehension. Print the new dictionary.
qubes={i**3 for i in range(1,11)}
print(qubes)

#6: Merging Dictionaries
#Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, 
#and another with keys as the next 5 positive integers and values as their squares.
#Merge these dictionaries into a single dictionary and print it.
d1={i:i*2 for i in range(1,6)}
d2={i:i*2 for i in range(6,11)}
print(d1)
print(d2)
d1.update(d2)
print(f"merged dictionary {d1}")

#7: Nested Dictionaries
#Create a nested dictionary representing a student with keys 'name', 'age', 'grades', where 'grades' is another dictionary 
#with keys 'math', 'science', and 'english'. Print the nested dictionary.

student={'name':'rupesh',
         'age':21,
         'grades':{
             'math':95,
             'science':68,
             'english':85
         }
        }
print(student)

#8: Dictionary of Lists
#Create a dictionary where the keys are the first 5 positive integers and the values are lists containing 
#the first 5 multiples of the key. Print the dictionary.
multiples_dict={i:[i*j for j in range(1,6)] for i in range(1,6)}
print(multiples_dict)

#9: Dictionary of Tuples
#Create a dictionary where the keys are the first 5 positive integers and the values are tuples containing the key and its square. 
#Print the dictionary.
tuple_dict={i:(i**2 )for i in range(1,6)}
print(tuple_dict)

#10: Dictionary and List Conversion
#Create a dictionary with the first 5 positive integers as keys and their squares as values.
#Convert the dictionary to a list of tuples and print it.
d={i:i**2 for i in range(1,6)}
converted_tuples=tuple(d.items())
print(converted_tuples)

#11: Dictionary Filtering
#Create a dictionary with the first 10 positive integers as keys and their squares as values.
#Create a new dictionary containing only the key-value pairs where the key is even. Print the new dictionary.
d={i:i**2 for i in range(1,11)}
new_dictionary={i:i**2 for i in d if i%2==0}
print(new_dictionary)

#12: Dictionary Key and Value Transformation
#Create a dictionary with the first 5 positive integers as keys and their squares as values.
#Create a new dictionary with keys and values swapped. Print the new dictionary.
d={i:i**2 for i in range(1,6)}
swapped_dictionary={v:k for k,v in d.items()}
print(swapped_dictionary)

#13: Default Dictionary
#Create a default dictionary where each key has a default value of an empty list. 
#Add some elements to the lists and print the dictionary.
from collections import defaultdict
default_dict=defaultdict(list)
default_dict['a'].append(1)
default_dict['b'].append(2)
default_dict['c'].append(3)
default_dict['d'].append(4)
print(default_dict)

#14: Counting with Dictionaries
#Write a function that takes a string and returns a dictionary with the count of each character in the string. Print the dictionary.

'''def string_count(string):
    count_dict={}
    for char in string:
        count_dict[char]=count_dict.get(char,0)+1
    return count_dict'''
from collections import Counter
def string_count(string):
    count=Counter(string)
    return count
    
    
string="hi iam rupesh"
print(string_count(string))
    
#15: Dictionary and JSON
#Create a dictionary representing a book with keys 'title', 'author', 'year', and 'genre'.
#Convert the dictionary to a JSON string and print it.
import json

book = {
    'title': 'To Kill a Mockingbird',
    'author': 'Harper Lee',
    'year': 1960,
    'genre': 'Fiction'
}
book_json = json.dumps(book)
print(book_json)