import unittest
import lab3

class ordinalTest(unittest.TestCase):
	
	def test_one(self): #run test to distinguish between 1st and 11th
		self.assertEqual('11th',lab3.ordinal(11))
		self.assertNotEqual('1st',lab3.ordinal(1))
		
	def test_teens(self): #run test to check ordinals of teens
		self.assertEqual('13th',lab3.ordinal(13))
		self.assertEqual('18th',lab3.ordinal(18))
		
	def test_largeNumber(self): #run test to check large numbers with multiple digits
		self.assertEqual('2013th',lab3.ordinal(2013))
		self.assertEqual('2001st',lab3.ordinal(2001))
		
	def test_typeError(self): #check type errors
		self.assertEqual("Enter an integer.",lab3.ordinal('b'))
		self.assertEqual("Enter an integer.",lab3.ordinal('12.7'))
		
if __name__ == '__main__': #Add this if you want to run the test with this script.
  unittest.main()