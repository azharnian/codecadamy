'''
Turn up the Temperature
1.
Write a function called f_to_c that takes an input f_temp, a temperature in Fahrenheit, and converts it to c_temp, that temperature in Celsius.

It should then return c_temp.

The equation you should use is:

Temp (C) = (Temp (F) - 32) * 5/9

Stuck? Get a hint
2.
Let’s test your function with a value of 100 Fahrenheit.

Define a variable f100_in_celsius and set it equal to the value of f_to_c with 100 as an input.


Stuck? Get a hint
3.
Write a function called c_to_f that takes an input c_temp, a temperature in Celsius, and converts it to f_temp, that temperature in Fahrenheit.

It should then return f_temp.

The equation you should use is:

Temp (F) = Temp (C) * (9/5) + 32
4.
Let’s test your function with a value of 0 Celsius.

Define a variable c0_in_fahrenheit and set it equal to the value of c_to_f with 0 as an input.


Stuck? Get a hint
Use the Force
5.
Define a function called get_force that takes in mass and acceleration. It should return mass multiplied by acceleration.

6.
Test get_force by calling it with the variables train_mass and train_acceleration.

Save the result to a variable called train_force and print it out.


Stuck? Get a hint
7.
Print the string “The GE train supplies X Newtons of force.”, with X replaced by train_force.

8.
Define a function called get_energy that takes in mass and c.

c is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set c to have a default value of 3*10**8.

get_energy should return mass multiplied by c squared.

9.
Test get_energy by using it on bomb_mass, with the default value of c. Save the result to a variable called bomb_energy.


Stuck? Get a hint
10.
Print the string “A 1kg bomb supplies X Joules.”, with X replaced by bomb_energy.

Do the Work
11.
Define a final function called get_work that takes in mass, acceleration, and distance.

Work is defined as force multiplied by distance. First, get the force using get_force, then multiply that by distance. Return the result.


Stuck? Get a hint
12.
Test get_work by using it on train_mass, train_acceleration, and train_distance. Save the result to a variable called train_work.

13.
Print the string "The GE train does X Joules of work over Y meters.", with X replaced with train_work and Y replaced with train_distance.
'''
def f_to_c(f_temp):
  c_temp = (f_temp-32)* 5/9
  return c_temp

def c_to_f(c_temp):
  f_temp = c_temp * 9/5 + 32
  return f_temp

def get_force(mass, acceleration):
  return mass*acceleration

def get_energy(mass, c=3*10**8):
  return mass*c**2

def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration)*distance

train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

f100_in_celcius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)

train_force = get_force(train_mass, train_acceleration)

bomb_energy = get_energy(bomb_mass)

train_work = get_work(train_mass, train_acceleration, train_distance)

print(f"The GE train supplies {train_force} Newtons of force.")
print(f"A 1kg bomb supplies {bomb_energy} Joules.")
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")


