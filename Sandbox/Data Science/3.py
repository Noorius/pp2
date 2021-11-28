from matplotlib import pyplot as plt

movies = ["Ann Hall", 'Ben-Gur', "Kasablanka", "Gandhi", "West History"]
num_oscar = [5,11,3,8,10]

plt.bar(range(len(movies)),num_oscar)

plt.title("Movies")
plt.ylabel("Amount of awards")

plt.xticks(range(len(movies)),movies)
plt.show()