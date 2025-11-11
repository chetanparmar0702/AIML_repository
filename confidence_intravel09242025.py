import numpy as np
import scipy.stats as stats

sample = [190, 205, 200, 210, 195, 205, 200, 198, 202, 207]


mean = np.mean(sample)
std_err = stats.sem(sample)


confidence = 0.95
h = std_err * stats.t.ppf((1 + confidence) / 2, len(sample) - 1)
ci_lower = mean - h
ci_upper = mean + h

print(f"Sample Mean: {mean}")
print(f"95% Confidence Interval: {ci_lower:.2f} - {ci_upper:.2f}")