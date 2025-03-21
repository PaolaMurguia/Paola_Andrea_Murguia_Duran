# Definition of the method add number, in which the use of
# PEP8 is shown. It shows how to document a method and how 
# to name as well. Using a call to test that the code is 
# working

def is_even(number):
    """Check if a number is even or odd
        returns True if the number is even, False otherwise.
        Parameters:
        number (int)
    """
   
    return number % 2 == 0
if __name__=="__main__": 
    #Calling the is_even() function
    number = 8
    if is_even(number):
        print("Is even.")
    else:
        print("Is odd.")
    
# Docstrings are strings that appear at the beginning of 
# a module, class, or function definition. They provide 
# documentation for the code that follows. Here's an example 
# of a docstring for the multiply_numbers() function:

def multiply_numbers(c, d):
    """
    Multiply two numbers together.
    
    Parameters:
        c (int or float): The first number to be added.
        d (int or float): The second number to be added.
        
    Returns:
        int or float: The product of the two input values. 
    """
    result = c * d
    return result

# Context Manager Context managers are objects that define the 
# enter() and exit() methods. These methods allow you to use the 
# object as a context manager using the with statement. Here's 
# an example of a custom context manager that times how long it 
# takes to execute a block of code:

import time

class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.time()
        print(f"Time taken: {end_time - self.start_time:.6f} seconds")

with Timer():
    total = sum(range(1_000_001))  # add 1 to 1,000,000 --> 1+2+3+...+1,000,000
    print("Sum completed.")

# Show message by applying pep8 style code in python using greet method.

from datetime import datetime

def greet(name):
    """Greets the user with a personalized message based on the time of day.

    Args:
        name (str): The name of the user to greet.

    Returns:
        str: A string containing the greeting message.
    """
    current_hour = datetime.now().hour
    print(current_hour)
    if current_hour < 12 and current_hour > 1:
        time_of_day = "Good morning"
    elif current_hour < 18:
        time_of_day = "Good afternoon"
    else:
        time_of_day = "Good evening"

    if name:
        return f"{time_of_day}, {name}!"
    return f"{time_of_day}, world!"


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greeting = greet(user_name)
    print(greeting)

