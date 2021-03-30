import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

import math 



# Functions enable you to reuse logic an infinite number of times without repeating yourself

# To define a function you write "def" followed by "the name of the function". Next you write parentheses "()"
# Inside the parentheses you list "inputs or arguments" to the function. Next type a colon ":" and  return.press
# The colon is how you start a new code block in Pyhtnon
def f():
    pass #this tells python to skip this line and do nothing. In Python you group code by indentation.

# To call the function, type the name and parentheses.. The function f will do nothing just like we told it to
f()
print("f()")
print(Fore.WHITE + Back.RED + Style.BRIGHT + str(f()))
print(Fore.RED + Style.BRIGHT + 45 * "-")
# if you forget to type parentheses, Python displays that f is a function and gives the memory address
f
print("f")
print(Fore.WHITE + Back.RED + str(f))
print(Fore.RED + Style.BRIGHT + 45 * "-")

# Write a function that returns a value:
def text():
    return "This is a quick Intro to Functions in Python!"
    text()
print("text()") 
print(Fore.WHITE + Back.RED + Style.BRIGHT + str(text())) #str is used to concatenate the function text() to a string
print(Fore.RED + Style.BRIGHT + 45 * "-")

# We can also store the return value to a variable 
x = text()
print("x = text()")
print("print(x)")
print(Fore.WHITE + Back.RED + Style.BRIGHT + str(x))
print(Fore.RED + Style.BRIGHT + 45 * "-")

# Function with 1 argument:
#---------------------------
# Write a function that will return the volume of a sphere given the radius.
# note: V = 4/3 pi r**3
def volume(r):   # This function has a single argument, the radius r
    """returns the volume of a sphere with radius r."""  # This is a docstring; it provides documentation on what the function does and how to use it.
    v = (4.0/3.0) * math.pi * r**3  # We compute the volume
    return v
# Because we used an argument when defining the function, you must provide an input when calling it- R is a required argument
volume(2)
print("volume(2)")
print(Fore.WHITE + Back.RED + Style.BRIGHT + str(volume(2)))
