import matplotlib.pyplot as plt

students = ['Anil', 'Gary', 'Leo', 'Zach', 'Tom']
averages = [99, 95,76,58,87]

plt.bar(students, averages, width=0.8)
plt.plot(students, averages, color='r')


plt.xlabel('Students')
plt.ylabel('Average')
plt.title('Student Performace Graph')
plt.legend()

plt.show()
 
