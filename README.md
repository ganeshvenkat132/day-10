
Academic Data Drift & Copy Behavior Analyzer

Overview:
This program generates random student academic data and analyzes how different copying methods affect data consistency.

Data Structure:
The data is stored as a list of dictionaries. Each record contains id, marks, attendance, and a scores list.

Copy Methods:
Two copies are created. A shallow copy shares inner references, while a deep copy creates a fully independent dataset.

Mutation Process:
Changes are applied only to copied data. Marks are increased using the square root formula, attendance is reduced, and elements in the scores list are modified. Only indexes divisible by (roll number % 3) are affected.

Analysis:
The program uses NumPy to calculate mean and standard deviation. One mean is also computed manually. Data drift is calculated as the absolute difference between original and modified mean. Marks are normalized using min-max normalization.

Classification:
Based on drift and data behavior, the result is categorized as Stable Data, Minor Drift, Critical Drift, or Copy Failure Detected.

Shallow Copy Issue:
Shallow copy shares references of nested objects like lists. When the copied data is modified, the original data also changes unintentionally, leading to copy failure. Deep copy prevents this by creating a completely separate copy.

Output:
The program displays original data, shallow copy result, deep copy result, drift value, the tuple (mean, drift, standard deviation), and the final classification.
