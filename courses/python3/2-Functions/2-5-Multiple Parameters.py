'''
Multiple Parameters
Our grocery greeting system has gotten popular, and now other supermarkets want to use it. As such, we want to be able to modify both the special item and the name of the grocery store in a greeting like this:

Welcome to [grocery store].
Our special is [special item].
Have fun shopping!
We can make a function take more than one parameter by using commas:

def greet_customer(grocery_store, special_item):
    print("Welcome to "+ grocery_store + ".")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")
The variables grocery_store and special_item must now both be provided to the function upon calling it:

greet_customer("Stu's Staples", "papayas")
which will print:

Welcome to Stu's Staples.
Our special is papayas.
Have fun shopping!
Instructions
1.
The function mult_two_add_three takes a number, multiplies it by two and adds three. We want to make this more flexible. First, change the name of the function to mult_x_add_y.

2.
Now, add x and y as parameters of the function, after number.

3.
Inside the function, replace 2 in the print statement with x, and replace 3 in the print statement with y.

4.
Call the function with these values:

number: 5

x: 2

y: 3

5.
Call the function with these values:

number: 1

x: 3

y: 1
'''
def mult_x_add_y(number,x,y):
  print(number*x + y)
  
#mult_x_add_y(5,2,3)
mult_x_add_y(1,3,1)