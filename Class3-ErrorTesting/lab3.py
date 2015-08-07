def ordinal(integer):
	try:
		if integer%1!=0: #raise type error if remainder is not zero (for float values)
			raise TypeError
		elif str(integer)[-2]=='1': #apply exception to ordinals with values that have 10s digit==1
			raise Exception
		elif (integer - 1)%10==0: #ordinal for values with 1 in ones digit
			return "%dst" %integer
		elif (integer - 2)%10==0: #ordinal for values with 2 in ones digit
			return "%dnd" %integer
		elif (integer - 3)%10==0: #ordinal for values with 3 in ones digit
			return "%drd" %integer
		elif integer%10 in range(4,10): #ordinal for values ranging 4-9 in ones digit
			return "%dth" %integer
	except TypeError: #Error message for float and string values
		return "Enter an integer."
	except: #Define exception for 11-13
		return "%dth" %integer