'''
Parameters
Let’s return to Engrossing Grocers. The special of the day will not always be mandarin oranges, it will change every day. What if we wanted to call these three print statements again, except with a variable special? We can use parameters, which are variables that you can pass into the function when you call it.

def greet_customer(special_item):
    print("Welcome to Engrossing Grocers.")
    print("Our special is " + special_item + ".")
    print("Have fun shopping!")
In the definition heading for greet_customer(), the special_item is referred to as a formal parameter. This variable name is a placeholder for the name of the item that is the grocery’s special today. Now, when we call greet_customer, we have to provide a special_item:

greet_customer("peanut butter")
That item will get printed out in the second print statement:

Welcome to Engrossing Grocers.
Our special is peanut butter.
Have fun shopping!
The value between the parentheses when we call the function (in this case, "peanut butter") is referred to as an argument of the function call. The argument is the information that is to be used in the execution of the function. When we then call the function, Python assigns the formal parameter name special_item with the actual parameter data, "peanut_butter". In other words, it is as if this line was included at the top of the function:

special_item = "peanut butter"
Every time we call greet_customer() with a different value between the parentheses, special_item is assigned to hold that value.
Instructions
1.
The function mult_two_add_three() prints a number multiplied by 2 and added to 3. As it is written right now, the number that it operates on is always 5.

Call the function and see what it prints to the console.


Stuck? Get a hint
2.
Now, modify the function definition so that it has a parameter called number. Then delete the number = 5 assignment on the first line of the function.

Pass the number 1 into your function call.

3.
Call the function with the value 5 as the argument.

4.
Call the function with the value -1 as the argument.

5.
Call the function with the value 0 as the argument.
'''
def mult_two_add_three(number):
  print(number*2 + 3)
  
# Call mult_two_add_three() here:
#mult_two_add_three(1)
#mult_two_add_three(5)
#mult_two_add_three(-1)
mult_two_add_three(0)