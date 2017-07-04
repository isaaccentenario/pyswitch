# Simple switch statement

class switch:
	item = ''
	def __init__(self,val): 
		self.item = val

	def case(self, i, callback):
		if self.item == i or str(self.item) == str(i):
			return callback()
		return False


# to use
foo = 'foo'

def casefoo():
	print "it's foo"
	return foo

def casebar():
	print "it's bar"

switch = switch( foo )

switch.case('foo', casefoo)
switch.case('bar', casebar)

# you can use lambda functions to return values
bar = switch.case('foo', lambda: 'its lambda foo' )

if bar != False:
	print bar
