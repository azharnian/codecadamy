'''
Returns
So far, we have only seen functions that print out some result to the console. Functions can also return a value to the user so that this value can be modified or used later. When there is a result from a function that can be stored in a variable, it is called a returned function value. We use the keyword return to do this.

Here’s an example of a function divide_by_four that takes an integer argument, divides it by four, and returns the result:

def divide_by_four(input_number):
    return input_number/4
The program that calls divide_by_four can then use the result later:

result = divide_by_four(16)
# result now holds 4
print("16 divided by 4 is " + str(result) + "!")
result2 = divide_by_four(result)
print(str(result) + " divided by 4 is " + str(result2) + "!")
This would print out:

16 divided by 4 is 4!
4 divided by 4 is 1!
In this example, we returned a number, but we could also return a String:

def create_special_string(special_item):
    return "Our special is " + special_item + "."

special_string = create_special_string("banana yogurt")

print(special_string)
Our special is banana yogurt.
Instructions
1.
The function calculate_age in script.py creates a variable called age that is the difference between the current year, and a birth year, both of which are inputs of the function. Add a line to return age.


  
2.
Outside of the function, call calculate_age with values 2049 (current_year) and 1993 (birth_year) and save the value to a variable called my_age.

3.
Call calculate_age with values 2049 (current_year) and 1953 (birth_year) and save the value to a variable called dads_age.

Print the string "I am X years old and my dad is Y years old" to the console, with my_age where the X is and dads_age where the Y is.
'''

def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age

my_age = calculate_age(2049,1993)
dads_age = calculate_age(2049,1953)

print(f"I am {my_age} years old and my dad is {dads_age} years old")