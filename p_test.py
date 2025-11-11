import scipy.stats as stats

teamA = [70, 75, 80]
teamB = [78, 80, 79]
teamC = [84, 83, 82]


f_stat, p_val = stats.f_oneway(teamA, teamB, teamC)
print("F-Statistic:", f_stat)
print("P-Value:", p_val)
if p_val <0.05:
    print("Reject the null hypothesis")
else:
    print("Accept the null hypothesis")