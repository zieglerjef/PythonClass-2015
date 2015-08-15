from JZhw4 import *
import random
import timeit
import matplotlib.pyplot as plt

def iterations(sort_type, n):  # This function sorts randomly generated numbers of length n that range from -500 to 500
	if sort_type == "insertion sort":
		insertion_sort([random.randint(-500,500) for number in range(n)])
	elif sort_type == "selection sort":
		selection_sort([random.randint(-500,500) for number in range(n)])

time_selection = []
for n in range(1,1000):
	t = timeit.Timer('iterations("insertion sort", %s)' % (n), 'from __main__ import iterations').timeit(number=1)
	time_selection.append(t)

time_merge = []
for n in range(1,1000):
	t = timeit.Timer('iterations("selection sort", %s)' % (n), 'from __main__ import iterations').timeit(number=1)
	time_merge.append(t)

plt.figure()  # Open a figure to plot

plt.plot(range(1,1000), time_selection, label="Insertion sort")
plt.plot(range(1,1000), time_merge, label="Selection sort")
plt.xlabel("Size")
plt.ylabel("Time")
plt.title("Runtime by Size")
plt.legend(loc="upper left") 

plt.savefig("runtime_by_size.pdf")