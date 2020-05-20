'''
Multiple Return Values
Sometimes we may want to return more than one value from a function. We can return several values by separating them with a comma:

def square_point(x_value, y_value):
  x_2 = x_value * x_value
  y_2 = y_value * y_value
  return x_2, y_2
This function takes in an x value and a y value, and returns them both, squared. We can get those values by assigning them both to variables when we call the function:

x_squared, y_squared = square_point(1, 3)
print(x_squared)
print(y_squared)
This will print:

1
9
Instructions
1.
Write a function called get_boundaries() that takes in two parameters, a number called target and a number called margin.

It should create two variables:

low_limit: target minus the margin
high_limit: margin added to target
2.
Return both low_limit and high_limit from the function, in that order.

3.
Call the function on the target 100 with a margin of 20. Save the returned values to variables called low and high.

'''
def get_boundaries(target, margin):
  low_limit = target-margin
  high_limit = margin+target

  return low_limit,high_limit

low, high = get_boundaries(100, 20)