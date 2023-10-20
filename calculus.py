import numpy as np
x = np.array([0.5, 1.5, 3, 4.25, 5, 7, 9.75])

y = np.array([0, 4.5, 7, 6.5, 9, 20.25, 15.75])
def model(x, m):
   return m * x


def error_function(m):
   return 3 * (m**2)

def derivative(n):
   return 6 * m
   
def update_step(m, learning_rate=0.01):
  return m - (learning_rate * derivative(m))
m=-6
n_epochs=5
   
  
for epoch in range(n_epochs):
  m = update_step(m) 
  print(f'Epoch {epoch + 1}: m = {round (m,2)} and loss = {round (error_function (m), 2)}') 

print("predictions in x value")
print("FINAL RESULTS")
print("predictions in y values")

print (f'm= {round (m, 2)} and loss = {round (error_function (m), 2)}')

print(f"The regression line is: y = {round(m, 2)}x")
