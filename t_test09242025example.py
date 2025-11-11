# Average sales per employee should be at least 75 units( one sample T-test)

import numpy as np
import scipy.stats as stats


# sample = [72, 74, 76, 70, 75]
sample = [65, 68, 70, 62, 67]

target_value = 75


t_statistic, p_value = stats.ttest_1samp(sample, target_value)

print(f"Sample Mean: {np.mean(sample)}")
print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")
if p_value < 0.05:
    print(" Reject the null hypothesis. ")
else:
    print(" Accept the null hypothesis.")
    