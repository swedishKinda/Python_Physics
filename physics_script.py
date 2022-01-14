# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3*10**8

# Write your code below: 

def f_to_c(f_temp):
  return (f_temp - 32) * 5/9
  
f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  return c_temp * 9/5 + 32

c0_in_fahrenheit = c_to_f(0)

def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)

print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass):
  c = 3*10**8
  return mass * c**2

print(get_energy(bomb_mass))