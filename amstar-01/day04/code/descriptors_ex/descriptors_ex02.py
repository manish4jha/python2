class Alphabet: 
	def __init__(self, value): 
		self._value = value 
			
	# getting the values	 
	@property
	def xyz(self): 
		print('Getting value') 
		return self._value 
			
	# setting the values	 
	@xyz.setter 
	def xyz(self, value): 
		print('Setting value to ' + value) 
		self._value = value 
			
	# deleting the values 
	@xyz.deleter 
	def xyz(self): 
		print('Deleting value') 
		del self._value 
	
	
# passing the value 
x = Alphabet('Peter') 
print(x.xyz) 
	
x.xyz = 'Diesel'
	
del x.xyz 
