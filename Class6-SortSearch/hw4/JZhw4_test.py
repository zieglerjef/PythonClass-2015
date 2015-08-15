import unittest
from JZhw4 import *
 
class JZhw4Test(unittest.TestCase):
 
	def testInsertionSort(self):
		x = [10, 5, 100, 3, 1, 19, 78, 0, 5, 34, 29]
		insertion_sort(x)
		for i in range(1, len(x)):
			if x[i - 1] > x[i]:
				print self.fail("Insertion sort failed.")
            
	def testSelectionSort(self):
		x = [10, 5, 100, 3, 1, 19, 78, 0, 5, 34, 29]
		selection_sort(x)
		for i in range(1, len(x)):
			if x[i - 1] > x[i]:
				print self.fail("Selection sort failed.")

if __name__ == '__main__':
	unittest.main()