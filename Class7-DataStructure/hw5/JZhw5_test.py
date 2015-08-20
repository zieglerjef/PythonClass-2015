import unittest
from JZhw5 import *
 
class JZhw5Test(unittest.TestCase):
 
	def initial(self):
		self.mylist = LinkedList()
	
	def testAddNode(self):
		self.mylist.addNode(3)
		self.mylist.addNode(8)
		self.mylist.addNode(7)
		self.mylist.addNode(15)
		self.assertEqual('3, 8, 7, 15', self.mylist.__str__())  
            
	def testAddNodeAfter(self):
		self.mylist.addNodeAfter(9, 2)
		self.mylist.addNode(2, 4)
		self.assertEqual('3, 8, 9, 7, 2, 15', self.mylist.__str__())
	
	def testAddNodeBefore(self):
		self.mylist.addNodeBefore(6, 3)
		self.mylist.addNodeBefore(10, 4)
		self.assertEqual('3, 8, 6, 10, 9, 7, 2, 15', self.mylist.__str__())
		
	def testRemoveNode(self):
		self.mylist.removeNode(3)
		self.mylist.removeNode(6)
		self.assertEqual('3, 8, 10, 9, 7, 15', self.mylist.__str__())
		
	def testRemoveNodeByValue(self):
		self.mylist.removeNodesByValue(7)
		self.mylist.removeNodesByValue(9)
		self.assertEqual('3, 8, 10, 15', self.mylist.__str__())
		
	def testReverse(self):
		self.mylist.reverse()
		self.assertEqual('15, 10, 8, 3', self.mylist.__str__())
		
	def testLength(self):
		self.assertEqual(self.mylist.length, 4)

if __name__ == '__main__':
	unittest.main()