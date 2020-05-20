'''
Keyword Arguments
In our greet_customer() function from the last exercise, we had two arguments:

def greet_customer(grocery_store, special_item):
    print("Welcome to "+ grocery_store + ".")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")
Whichever value is put into greet_customer() first is assigned to grocery_store, and whichever value is put in second is assigned to special_item. These are called positional arguments because their assignments depend on their positions in the function call.

We can also pass these arguments as keyword arguments, where we explicitly refer to what each argument is assigned to in the function call.

greet_customer(special_item="chips and salsa", grocery_store="Stu's Staples")
Welcome to Stu's Staples.
Our special is chips and salsa.
Have fun shopping!
We can use keyword arguments to make it explicit what each of our arguments to a function should refer to in the body of the function itself.

We can also define default arguments for a function using syntax very similar to our keyword-argument syntax, but used during the function definition. If the function is called without an argument for that parameter, it relies on the default.

def greet_customer(special_item, grocery_store="Engrossing Grocers"):
    print("Welcome to "+ grocery_store + ".")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")
In this case, grocery_store has a default value of "Engrossing Grocers". If we call the function with only one argument, the value of "Engrossing Grocers" is used for grocery_store:

greet_customer("bananas")
Welcome to Engrossing Grocers.
Our special is bananas.
Have fun shopping!
Once you give an argument a default value (making it a keyword argument), no arguments that follow can be used positionally. For example:

def greet_customer(special_item="bananas", grocery_store): # this is not valid
    ...

def greet_customer(special_item, grocery_store="Engrossing Grocers"): # this is valid
    ...
Instructions
1.
We have defined a function create_spreadsheet, which just takes in a title, and prints that it is creating a spreadsheet.

Run the code to see the function work on an input of "Downloads".


 
2.
Add the parameter row_count to the function definition. Set the default value to be 1000.

3.
Change the print statement in the function to print “Creating a spreadsheet called title with row_count rows”, where title and row_count are replaced with their respective values.

Remember, to concatenate a number to a string object, you’ll first have to cast row_count to a string using str(). Otherwise, you’ll get a TypeError.


 
4.
Call create_spreadsheet() with title set to "Applications" and row_count set to 10.
'''
# Define create_spreadsheet():
def create_spreadsheet(title, row_count=1000):
  print("Creating a spreadsheet called "+title+" with "+str(row_count)+" rows")

# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Applications", 10)