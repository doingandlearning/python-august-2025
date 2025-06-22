import matplotlib.pyplot as plt

labels = ("Python", "Scala", "TypeScript", "C#", "Java")
index = (1,2,3,4,5)
sizes = [45, 10, 50, 15, 30]


plt.bar(index, sizes,
        tick_label=labels,
        color=("red", "green", "blue", "yellow", "orange"))


plt.grid()
plt.show()