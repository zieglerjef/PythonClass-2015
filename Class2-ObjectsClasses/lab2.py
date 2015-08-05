class Clock(object):
	def __init__(self, hour, minutes): #create initial clock with hour and minutes
		self.minutes = minutes
		self.hour = hour
	
	@classmethod
	def at(cls, hour, minutes=0): #generate class attribute of hours and minutes
		return cls(hour, minutes)
	
	def __str__(self): #add zero in front of single digit hour/minutes
		return '0'*(2-len(str(self.hour)))+str(self.hour)+":"+'0'*(2-len(str(self.minutes)))+str(self.minutes)
		
	def __add__(self, added_minutes): #add minutes to myclock
		sum_minutes=self.minutes+added_minutes #sum minutes from myclock and added minutes
		updated_minute=sum_minutes%60 #remainder of sum minutes/60
		updated_hour=(self.hour+sum_minutes/60)%24 #add remainder of hours once clock goes past 24
		return Clock(updated_hour,updated_minute) #return updated clock
		
	def __sub__(self, added_minutes): #minus minutes from myclock
		return self + (-1)*added_minutes #add "subtracted" minutes
		
	def __eq__(self, other): #check whether two clocks are equal or not
		return self.hour == other.hour and other.minutes == self.minutes
		
	def __ne__(self, other):
		return not self==other