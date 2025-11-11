# Independent Two-Sample T-Test


import numpy as np
import scipy.stats as stats

teamA = [72, 74, 76, 70, 75]
teamB = [78, 79, 81, 77, 80]

target_value = 75


t_statistic, p_value = stats.ttest_ind(teamA, teamB)

print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")
if p_value < 0.05:
    print(" Reject the null hypothesis. ")
else:
    print(" Accept the null hypothesis.")