class Clock(object):
	def __init__(self, hour, minutes): #create initial clock with hour and minutes
		self.minutes = minutes
		self.hour = hour
	
	@classmethod
	def at(cls, hour, minutes=0): #generate class attribute of hours and minutes
		return cls(hour, minutes)
	
	def __str__(self): #add zero in front of single digit hour/minutes
		return '0'*(2-len(str(self.hour)))+str(self.hour)+":"+'0'*(2-len(str(self.minutes)))+str(self.minutes)
		
	def __add__(self, added_minutes):
		sum_minutes=self.minutes+added_minutes
		updated_minute=sum_minutes-(60*(sum_minutes/60))
		updated_hour=(self.hour+sum_minutes/60)%24
		return Clock(updated_hour,updated_minute)
		
	def __sub__(self, minus_minutes):
		return self + (-1)*minus_minutes
		
	def __eq__(self, other):
		