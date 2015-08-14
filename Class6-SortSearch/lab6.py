#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers

cds=[]
def gcd(n1, n2):
	begin=min(n1,n2)
	if n1%begin==0 and n2%begin==0:
		print begin
	else:
		for i in range (1, begin):
			if n1%i==0 and n2%i==0:
				cds.append(i)
		print max(cds)

#Exercise 2
#Write a function that returns prime numbers less than 121
import math
def prime(n):
	for i in range(2, n):
		if n%i==0:
			return None
	return n
	
primes=[]
for i in range(122):
	if prime(i): primes.append(prime(i))
print primes
  
#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html

def hanoi(disks, startPeg=1, endPeg=3):
    if disks:
        hanoi(disks-1, startPeg, 6-startPeg-endPeg)
        print "Move disk %d from peg %d to peg %d" % (disks, startPeg, endPeg)
        hanoi(disks-1, 6-startPeg-endPeg, endPeg)