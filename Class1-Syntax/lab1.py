def binarify(num): 
 """convert positive integer to base 2"""
  if num<=0: return '0'
  elif num>0: return format(num, 'b')

def int_to_base(num, base):
"""convert positive integer to a string in any base"""
	if num<=0:  return '0' 
	digits = []
	while num!=0:
		digits.append(str(num%base))
		num = num/base
	digits.reverse()
	return ''.join(digits)

def base_to_int(string, base):
  """take a string-formatted number and its base and return the base-10 integer"""
  if string=="0" or base <= 0 : return 0 
  string = string[::-1]
  x = [digit for digit in string]
  integ = []
  for i in range (0,len(string)):
  	integ.append(int(x[i])*base**i)
  return sum(integ) 

def flexibase_add(str1, str2, base1, base2):
  """add two numbers of different bases and return the sum"""
  return base_to_int(str1, base1) + base_to_int(str2, base2)

def flexibase_multiply(str1, str2, base1, base2):
  """multiply two numbers of different bases and return the product"""
  return base_to_int(str1, base1) * base_to_int(str2, base2)

def romanify(num):
  """given an integer, return the Roman numeral version"""
  
  
# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.