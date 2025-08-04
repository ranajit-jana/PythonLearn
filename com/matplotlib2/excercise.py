import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator



studentnumber=np.arange(0,40, 1 )

englishMarks= np.random.rand(1, 40)*100
mathMarks= np.random.rand(1, 40)*100
print(englishMarks)


subjects= ['Math','Science','English','History']
marks=[82,76,88,70]


plt.bar(subjects, marks)
plt.xlabel("subjects")
plt.ylabel("average Marks")
plt.show()

"""
Visualize and compare the scores of students in different subjects to identify 
strengths and weaknesses.


 Scenario:
You're a data analyst at a school. The principal asks for a quick visual report comparing 
average scores in four subjects for a class of students.


What We'll Do:

Use a bar chart to compare average scores
Add clear labels, title, and color for clarity


Subject	Average Score

Math	82

Science	76

English	88

History	70
"""