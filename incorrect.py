import os
import random

def greet(name)
    print("Hello, " + name)  # Syntax Error: Missing colon in function definition

def calculate_sum(a, b)
    return a + b  # Syntax Error: Missing colon in function definition

def get_random_number()
    return random.randint(1, 10)  # Syntax Error: Missing colon

def faulty_logic():
    if False  # Syntax Error: Missing colon
        print("This will never print")

def division(a, b):
    return a / b  # Runtime Error: Division by zero if b is 0

def print_list_elements(lst):
    for i in range(len(lst) + 1):  # Logical Error: Index out of range
        print(lst[i])

def file_operations():
    with open("non_existent_file.txt", "r") as f:  # Runtime Error: FileNotFoundError
        content = f.read()
    print(content)

def recursive_function(n):
    if n == 0:
        return 1
    else:
        return n * recursive_function(n - 1)  # Logical Error: Stack overflow if n is too large

def type_error_example():
    num = "5" + 10  # TypeError: Can't concatenate str and int
    print(num)

class Animal
    def __init__(self, name):  # Syntax Error: Missing colon
        self.name = name

    def speak():
        print("The animal speaks!")  # Logical Error: Missing self parameter

def list_manipulation():
    my_list = [1, 2, 3]
    my_list.remove(4)  # Runtime Error: ValueError if 4 is not in the list

def dictionary_error():
    my_dict = {"name": "Alice", "age": 25}
    print(my_dict["address"])  # Runtime Error: KeyError

def loop_mistake():
    for i in range(5):
        i = 10  # Logical Error: Loop variable assignment doesn't affect the iteration

def infinite_loop():
    while True:
        print("This will run forever")  # Logical Error: Infinite loop

def broken_function():
    return 5
    print("This will never execute")  # Logical Error: Unreachable code

def another_syntax_error(
    print("Oops! Missing closing parenthesis.")  # Syntax Error

def call_undefined_function():
    undefined_function()  # Runtime Error: NameError

def missing_return_value():
    x = 10
    y = x * 2
    # Missing return statement

def incorrect_assertion():
    assert 2 + 2 == 5, "Math is broken!"  # AssertionError

def division_by_zero():
    x = 10 / 0  # ZeroDivisionError

def tuple_error():
    my_tuple = (1, 2, 3)
    my_tuple[0] = 5  # Runtime Error: TypeError (tuples are immutable)

def wrong_import():
    import non_existent_module  # ImportError: Module does not exist

# Calling all functions to trigger errors
greet("Alice")
calculate_sum(5, 10)
get_random_number()
faulty_logic()
print_list_elements([1, 2, 3])
file_operations()
print(division(10, 0))
recursive_function(1000)
type_error_example()
animal = Animal("Dog")
animal.speak()
list_manipulation()
dictionary_error()
loop_mistake()
# infinite_loop()  # Uncommenting this will cause an infinite loop
broken_function()
another_syntax_error()
call_undefined_function()
missing_return_value()
incorrect_assertion()
division_by_zero()
tuple_error()
wrong_import()