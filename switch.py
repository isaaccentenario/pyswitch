# Simple switch statement

class Switch:
	item = ''
	def __init__(self,val,return_false = True): 
		self.item = val
		self.return_false = return_false

	def case(self, i, callback):
		if self.item == i or str(self.item) == str(i):
			return callback()

		if self.return_false == True:
			return False

		return ""

# to use
variable = 'foo'

def casefoo():
	print "it's foo"

def casebar():
	print "it's bar"

switch = Switch( variable )

switch.case('foo', casefoo)
switch.case('bar', casebar)

# you can use lambda functions to return values
switch_no_false_return = Switch(variable, False) # the False parameter prevents False return value
bar = switch_no_false_return.case('notfoo', lambda: 'its lambda foo')

print bar