import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Define the function
def f(x):
  return 4*x**2 - 2*x + 6

# Create x values
x = np.linspace(-5, 5.5, 1000)  # Adjust the range as needed

# Calculate y values
y = f(x)

# Plot the function
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("$y = 4x^2 - 2x + 6$")
plt.grid(True)
plt.show()
