#1: Simple Function
#Define a function that takes a single integer as input and returns its square. Test the function with different inputs.
'''def square(x):
    return x**2
print(square(4))
print(square(6))

#2: Multiple Arguments
#Define a function that takes two integers as input and returns their sum. Test the function with different inputs.
def sum(x,y):
    return x+y
print(sum(4,6))
print(sum(8,4))
    
#3: Default Arguments
#Define a function that takes two integers as input and returns their sum. The second integer should have a default value of 5.
#Test the function with different inputs.
def sum(x,y=5):
    return x+y
print(sum(4))
print(sum(8))

#4: Keyword Arguments
#Define a function that takes three named arguments: first_name, last_name, and age, and returns a formatted string.
#Test the function with different inputs.
def formatted_string(first_name,last_name,age):
    return f"{first_name} {last_name} is {age} years old."
print(formatted_string('kurakula','rupesh',21))
print(formatted_string('kurakula','umesh',19))

#5: Variable-length Arguments
#Define a function that takes a variable number of integer arguments and returns their product. Test the function with different inputs.
def product(*args): # array arguments
    mul=1
    for num in args:
        mul=mul*num
    return mul
print(product(1,2,3))
print(product(5,4,5))

#6: Nested Functions
#Define a function that contains another function inside it. The outer function should take two integers as input and 
#return the result of the inner function, which multiplies the two integers. Test the function with different inputs.
def outer_function(x, y):
    def inner_function(a, b):
        return a * b
    return inner_function(x, y)
print(outer_function(2, 3))
print(outer_function(4, 5))

#7: Returning Multiple Values
#Define a function that takes a single integer as input and returns the integer squared, cubed, and raised to the power of four.
#Test the function with different inputs.
def square(x):
    return x**2,x**3,x**4
x=square(2)
print(x)

#8: Recursive Function
#Define a recursive function that calculates the factorial of a given number. Test the function with different inputs.
def factorial(num):
    fact=1
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
num=factorial(5)
num1=factorial(6)
print(num)
print(num1)

#9: Lambda Function
#Define a lambda function that takes two integers as input and returns their sum. Test the lambda function with different inputs.
add=lambda a,b:a+b
print(add(2,3))
print(add(6,5))

#10: Map Function
#Use the map function to apply a lambda function that squares each number in a list of integers. Test with different lists.
x=[1,2,3,4,5,6] 
y=[4,5,6,7,8]
square=list(map(lambda x:x**2,x))
square1=list(map(lambda y:y**2,y))
print(square)
print(square1)

#11: Filter Function
#Use the filter function to filter out all odd numbers from a list of integers. Test with different lists.
x=[1,2,3,4,5,6] 
y=[7,8,9,10,11,12]
odd=list(filter(lambda x:x%2!=0,x))
odd1=list(filter(lambda y:y%2!=0,y))
print(odd)
print(odd1)'''
#12: Function Decorator
#Define a decorator function that prints 'Executing function...' before executing a function and 'Function executed.' after executing it. 
#Apply this decorator to a function that takes a list of integers and returns their sum. Test the decorated function with different lists.
def my_decorator(fun):
    def wrapper(*args,**kwargs):
        print(f"executing function ...")
        result=fun(*args,**kwargs)
        print("function executied.")
        return result   
    return wrapper

@my_decorator
def sum_list(lst):
    return sum(lst)
print(sum_list([1, 2, 3, 4, 5]))

#13: Function with *args and **kwargs
#Define a function that takes variable-length arguments and keyword arguments and prints them. Test the function with different inputs.
def print_args_kwargs(*args,**kwargs):
    print('args:', args)
    print('kwargs:', kwargs)
print_args_kwargs(1,2,3,a='hi',b='hello')
print_args_kwargs(1,2,3,4,a='hi',b='hello')

#14: Higher-Order Function
#Define a higher-order function that takes a function and a list of integers as arguments, and applies the function to each integer in the list.
#Test with different functions and lists.
def apply_function(func, lst):
    return [func(x) for x in lst]
print(apply_function(lambda x: x ** 2, [1, 2, 3, 4, 5])) 
print(apply_function(lambda x: x + 1, [1, 2, 3, 4, 5]))