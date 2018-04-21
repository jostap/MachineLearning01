import numpy as np 
import matplotlib.pyplot as plt

greyhunds = 500
labs = 500

grey_height = 28 + 4 * np.random.randn(greyhunds)
lab_height = 24 + 4 * np.random.randn(labs)

plt.hist([grey_height, lab_height], stacked=True, color=['r', 'b'], rwidth=0.8)
plt.show()

