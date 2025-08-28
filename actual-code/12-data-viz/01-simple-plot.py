import matplotlib.pyplot as plt

y = [8,3,5,5,4,6,7]
x = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"] 
print(list(x))
plt.plot(x, y, marker="o", linestyle="--", color="blue", label="Emma")
plt.plot(x, [3,7,3,5,6,9,10], color="red", label="Jack")

plt.legend()
plt.xlabel("Day")
plt.ylabel("Number of Articles Read")
plt.grid(True)
plt.show()
# plt.savefig("graph.png")