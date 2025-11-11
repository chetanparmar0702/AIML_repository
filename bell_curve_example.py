import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

population = np.random.randint(8000, 15000, size=100000)

sample_means = []
for i in range(1000):  # take 1000 samples
    sample = np.random.choice(population, 1000)
    sample_means.append(np.mean(sample))

sns.histplot(sample_means, bins=30, kde=True)
plt.title("Sample Averages Forming Bell Shape (CLT)")
plt.xlabel("Average Spending")
plt.ylabel("Frequency")
plt.show()