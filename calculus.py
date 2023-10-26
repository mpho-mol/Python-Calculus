import numpy as np

X = np.array([0.5, 1.5, 3, 4.25, 5, 7, 9.75])
y = np.array([0, 4.5, 7, 6.5, 9, 20.25, 15.75])

def model(x, m):
    return m * x

def error_function(m):
    # Define the numerator of the error function
    numerator = 0
    n = len(X)
    for i in range(n):
        y_true = y[i]
        x_val = X[i]
        numerator += (y_true - model(x_val, m))**2

    return numerator / n


def derivative(m):
    numerator = 0
    n = len(X)
    for i in range(n):
        y_true = y[i]
        x_val = X[i]
        # Calculate inner expression
        bracketed_term = y_true - model(x_val, m)
        numerator += -2 * x_val * bracketed_term
    return numerator / n


def update_step(m, learning_rate=0.01):
    # Get the amount to change m by
    derivative_term = derivative(m)
    update_amount = learning_rate * derivative_term

    # Change m
    return m - update_amount

m = -6
n_epochs = 5 # This is just the number of update steps you take

# Iterate for n epochs
for epoch in range(n_epochs):
    # Update and print m
    m = update_step(m)
    print(f'Epoch {epoch + 1}: m = {round(m,2)} and loss = {round(error_function(m), 2)}')

# Print Final Results
print("-----------------")
print("FINAL RESULTS")
print("-----------------")

print(f'm = {round(m,2)} and loss = {round(error_function(m), 2)}')


print("-----------------")