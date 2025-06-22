import matplotlib.pyplot as plt

# continuous - time, length, ...
x = range(1,11)
y = [3,4,9,11,12,10,11,14,16,17]

plt.plot(x, y,
         linewidth=4.0,
         marker="x",
         color="magenta",
         linestyle="-", # --, :, -
         label="Desired"
         )

y1 = y.copy()
y1.reverse()
plt.plot(x, y1, label="Actual")

plt.legend()

plt.ylabel("Income")
plt.xlabel("Day of the month")

plt.title("How salary gets spent")

plt.xlim(2.7,8.3)
plt.ylim(6,15)

plt.savefig("graph.png")
plt.show()
