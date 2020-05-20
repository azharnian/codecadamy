'''
Write a Function
We have seen the value of simple functions for modularizing code. Now we need to understand how to write a function. To write a function, you must have a heading and an indented block of code. The heading starts with the keyword def and the name of the function, followed by parentheses, and a colon. The indented block of code performs some sort of operation. This syntax looks like:

def function_name():
  some code

For our greet_customer() example, the function definition looks like:

def greet_customer():
  print("Welcome to Engrossing Grocers.")
  print("Our special is mandarin oranges.")
  print("Have fun shopping!")

greet_customer()
# prints greeting lines

The keyword def tells Python that we are defining a function. This function is called greet_customer. Everything that is indented after the : is what is run when greet_customer() is called. So every time we call greet_customer(), the three print statements run.

Instructions
1.
Write a function called loading_screen that prints "This page is loading..." to the console.

2.
Outside of the function body (unindented), call loading_screen().

'''

def loading_screen():
  print('This page is loading...')

loading_screen()