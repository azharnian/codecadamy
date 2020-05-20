'''
What is a Function?
Let’s imagine that we are creating a program that greets customers as they enter a grocery store. We want a big screen at the entrance of the store to say:

Welcome to Engrossing Grocers.
Our special is mandarin oranges.
Have fun shopping!

We have learned to use print statements for this purpose:

print("Welcome to Engrossing Grocers.")
print("Our special is mandarin oranges.")
print("Have fun shopping!")

Every time a customer enters, we call these three lines of code. Even if only 3 or 4 customers come in, that’s a lot of lines of code required.

In Python, we can make this process easier by assigning these lines of code to a function. We’ll name this function greet_customer. In order to call a function, we use the syntax function_name(). The parentheses are important! They make the code inside the function run. In this example, the function call looks like:

greet_customer()

Every time we call greet_customer(), we would see:
Welcome to Engrossing Grocer's.
Our special is mandarin oranges.
Have fun shopping!

Having this functionality inside greet_customer() is better form, because we have isolated this behavior from the rest of our code. Once we determine that greet_customer() works the way we want, we can reuse it anywhere and be confident that it greets, without having to look at the implementation. We can get the same output, with less repeated code. Repeated code is generally more error prone and harder to understand, so it’s a good goal to reduce the amount of it.

Instructions
1.
In script.py, we have made a function for you called sing_song. Call this function once to see what it prints out.
2.
Now call sing_song a second time.
'''

def sing_song():
  print("You may say I'm a dreamer")
  print("But I'm not the only one")
  print("I hope some day you'll join us")
  print("And the world will be as one")
  
# call sing_song() below:
sing_song()
sing_song()