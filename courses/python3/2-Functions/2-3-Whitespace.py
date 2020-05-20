'''
Whitespace
Consider this function:

def greet_customer():
    print("Welcome to Engrossing Grocers.")
    print("Our special is mandarin oranges.")
    print("Have fun shopping!")
The three print statements are all executed together when greet_customer() is called. This is because they have the same level of indentation. In Python, the amount of whitespace tells the computer what is part of a function and what is not part of that function. If we wanted to write another line outside of greet_customer(), we would have to unindent the new line:

def greet_customer():
    print("Welcome to Engrossing Grocers.")
    print("Our special is mandarin oranges.")
    print("Have fun shopping!")
print("Cleanup on Aisle 6")
When we call greet_customer, the message"Cleanup on Aisle 6" is not printed, as it is not part of the function.

Here at Codecademy, we use 2 spaces for our default indentation. Anything other than that will throw an error when you try to run the program. Many other platforms use 4 spaces. Some people even use tabs! These are all fine. What is important is being consistent throughout the project.
Instructions
1.
Run script.py. Look at what is printed out!

2.
Remove the indent on the second print statement. Run the file. Now what’s printed?

'''

def about_this_computer():
  print("This computer is running on version Everest Puma")
print("This is your desktop")

about_this_computer()
