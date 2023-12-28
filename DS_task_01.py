#  q.1 "Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable, such as the distribution of ages or genders in a population."
import matplotlib.pyplot as plt
import numpy as np

# Sample data: ages of a population
ages = [22, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

# Create a histogram
plt.hist(ages, bins=10, color='skyblue', edgecolor='black')

# Add title and labels
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Show the plot
plt.show()
