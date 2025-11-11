import numpy as np
from scipy.stats import chi2_contingency

observed = np.array([
    [20, 30],
    [10, 40]
])

chi2, p_value, dof, expected = chi2_contingency(observed)

print(f"Chi-Square: {chi2:.3f}, DOF: {dof}, P-value: {p_value:.4f}")
print("Expected Frequencies:\n", expected)

alpha = 0.05
print("Result:", "Dependent" if p_value < alpha else "Independent")