import matplotlib.pyplot as plt
import numpy as np

subjects = ['Math', 'Science', 'English', 'History', 'Computer'] 
marks = [85, 90, 75, 70, 95]
plt.title("Subjects marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid()
plt.ylim(0, 100)
plt.plot(subjects, marks)
plt.show()
