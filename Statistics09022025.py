import random

import pandas as pd
students_data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [20, 21, 22],
    'Exam_Score': [85, 92, 78]
}
students_df = pd.DataFrame(students_data)


print("Our Student Data Table (DataFrame):")
print(students_df)
print("\nChecking the data types:")
print(students_df.info())

exam_scores = students_df['Exam_Score']


average_score = exam_scores.mean()

print(f"\nDescriptive Statistics: The average exam score is {average_score:.2f}")

import numpy as np
np.random.seed(35)

population_scores = np.random.randint(50, 100, 100)
population_df = pd.DataFrame(population_scores, columns=['Exam_Score'])
print(f"The average score for the whole population is: {population_df['Exam_Score'].mean():.2f}")



sample_df = population_df.sample(n=5, random_state=35)

print("\nOur Random Sample of 5 students:")
print(sample_df)


sample_average_score = sample_df['Exam_Score'].mean()

print(f"\nSample Average Score: {sample_average_score:.2f}")