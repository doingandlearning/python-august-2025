import matplotlib.pyplot as plt

labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
index = (1, 2, 3, 4, 5)
sizes = [45, 10, 15, 30, 22]

plt.bar(index, sizes, tick_label=labels)
plt.plot(index, sizes, color="red", marker="x")

plt.show()