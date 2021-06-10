''' 
Decorators are also a powerful tool in Python which are implemented using closures and 
allow the programmers to modify the behavior of a function without permanently modifying it.
'''

          # 1.) Nested functions in python 
  
def outerFunction(text):
	text = text

	def innerFunction():
		print(text)

	innerFunction()

if __name__ == '__main__':
	outerFunction('Hey!')

           # 2.) Python Closures
    
# Python program to illustrate
# closures
def outerFunction(text):
	text = text

	def innerFunction():
		print(text)

	# Note: we are returning function
	# WITHOUT parenthesis
	return innerFunction

if __name__ == '__main__':
	myFunction = outerFunction('Hey!')
	myFunction()
  
# Output :
Hey!


          # 3.)  Python program to illustrate closures
  
import logging
logging.basicConfig(filename='example.log',
					level=logging.INFO)


def logger(func):
	def log_func(*args):
		logging.info(
			'Running "{}" with arguments {}'.format(func.__name__,
													args))
		print(func(*args))
		
	# Necessary for closure to
	# work (returning WITHOUT parenthesis)
	return log_func			

def add(x, y):
	return x+y

def sub(x, y):
	return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3, 3)
add_logger(4, 5)

sub_logger(10, 5)
sub_logger(20, 10)

# Output :
6
9
5
10

            # 4.) defining a decorator
  
def hello_decorator(func):

	# inner1 is a Wrapper function in
	# which the argument is called
	
	# inner function can access the outer local
	# functions like in this case "func"
	def inner1():
		print("Hello, this is before function execution")

		# calling the actual function now
		# inside the wrapper function.
		func()

		print("This is after function execution")
		
	return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
	print("This is inside the function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behavior
function_to_be_used = hello_decorator(function_to_be_used)


# calling the function
function_to_be_used() 

         #  Output:

Hello, this is before function execution
This is inside the function !!
This is after function execution


             # 5.)  Code for testing decorator chaining
def decor1(func):
	def inner():
		x = func()
		return x * x
	return inner

def decor(func):
	def inner():
		x = func()
		return 2 * x
	return inner

@decor1
@decor
def num():
	return 10

print(num())

      # Output :
400
