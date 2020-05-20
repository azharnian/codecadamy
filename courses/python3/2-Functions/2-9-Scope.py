'''
Scope
Let’s say we have our function from the last exercise that creates a string about a special item:

def create_special_string(special_item):
    return "Our special is " + special_item + "."
What if we wanted to access the variable special_item outside of the function? Could we use it?

def create_special_string(special_item):
    return "Our special is " + special_item + "."

print("I don't like " + special_item)
If we try to run this code, we will get a NameError, telling us that 'special_item' is not defined. The variable special_item has only been defined inside the space of a function, so it does not exist outside the function. We call the part of a program where special_item can be accessed its scope. The scope of special_item is only the create_special_string function.

Variables defined outside the scope of a function may be accessible inside the body of the function:

header_string = "Our special is " 

def create_special_string(special_item):
    return header_string + special_item + "."
print(create_special_string("grapes"))
There is no error here. header_string can be used inside the create_special_string function because the scope of header_string is the whole file. This file would produce:

Our special is grapes.
Instructions
1.
Outside of the function calculate_age(), try to print current_year. Does it work?

2.
What about age? Outside of calculate_age(), try to print age. Does it work?

3.
No! Even though we return age at the end of the function, the variable age still only exists within the context of the function.

Remove both print statements.

4.
Let’s try something different. Remove the parameter current_year so that it is no longer a parameter of calculate_age().

5.
It’s the year 2048.

Define current_year as a variable BEFORE defining the function and give it the value 2048. Now, every time calculate_age() is called, it should only take birth_year.

6.
Try to print current_year one last time. Does it work finally?

7.
Hooray! Now we have current_year globally defined. Great work!

Let’s make sure our function still works: print the value of calculate_age() with 1970 as the argument.

'''
current_year = 2048

def calculate_age(birth_year):
  age = current_year - birth_year
  return age

print(current_year)
#print(age)
print(calculate_age(1970))