'''
Python descriptors are created to manage the attributes of different classes which use the object as reference. 
A descriptor is a mechanism behind properties, methods, static methods, class methods, and super() .
Python programming provides us with a built-in @property decorator which makes usage of getter and setters much easier in Object-Oriented Programming.
'''

          # 1.)  How to invoke descriptor
  
def __getattribute__(self, key):
    v = object.__getattribute__(self, key)
    if hasattr(v, '__get__'):
        return v.__get__(None, self)
    return v
  
          
              # 2.) Python program to explain property() function
	
# Alphabet class
class Alphabet:
	def __init__(self, value):
		self._value = value
			
	# getting the values
	def getValue(self):
		print('Getting value')
		return self._value
			
	# setting the values
	def setValue(self, value):
		print('Setting value to ' + value)
		self._value = value
			
	# deleting the values
	def delValue(self):
		print('Deleting value')
		del self._value
		
	value = property(getValue, setValue, delValue, )
	
# passing the value
x = Alphabet('GeeksforGeeks')
print(x.value)
	
x.value = 'GfG'
	
del x.value

    # Output :

Getting value
GeeksforGeeks
Setting value to GfG
Deleting value


            # 3.) Creating Descriptor Class
class Descriptor(object):

	def __init__(self, name =''):
		self.name = name

	def __get__(self, obj, objtype):
		return "{}for{}".format(self.name, self.name)

	def __set__(self, obj, name):
		if isinstance(name, str):
			self.name = name
		else:
			raise TypeError("Name should be string")
		
class GFG(object):
	name = Descriptor()
	
g = GFG()
g.name = "Geeks"
print(g.name)

   # Output :
GeeksforGeeks


            # 4.) Class Without Getters and Setters
  
class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
      
      
            # 5.) Using Getters and Setters
# Making Getters and Setter methods
class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        self._temperature = value
      
