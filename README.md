Calculus is the study of the change in mathematical functions and is a fundamental concept in machine learning  where every model has an error function, most of which are differentiable. Finding the instantaneous gradient of the error function the code can move down the error function thus finding optimal parameters.

This assignment was completed in Python using the computational framework NumPy and the calculus.py file which does linear regression. The aim of the task was to code in the functions that were left blank. The slope m and arrays denoted as x and y are defined. The following were the functions to be completed:
- def model(x,m) which returns m*x as the model f(x) = mx receives a data point x 
  and line gradient m and returns a prediction for y.
- def error_function(m) receives the slope m and returns J(m) which is the mean 
  squared error (MSE) between the model and the data.
- def derivative(m) is the derivation of the function J(m) above and receives the 
  slope m and returns dJ/dm.
- def update_step(m, learning_rate=0.01) is meant to update the gradient m using 
  the derivative of J(m) input m and outputs an updated m.
The slope m is set at 6 and the number of update steps which is denoted n_epochs was set at 5. A for loop was made to perform iterations of the number of the update steps. The final results are then printed.
