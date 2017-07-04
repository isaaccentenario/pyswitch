# pyswitch

## Simple switch statement

````
# to use 
variable = 'foo'
switch = Switch( variable )

def foo_opt():
	print "it's foo"

def bar_opt():
	print "it's bar"

switch.case('foo', foo_opt)
switch.case('bar', bar_opt)


# you can use lambda functions to return values
switch_no_false_return = Switch(foo,False) # the false parameter prevents False return value

bar = switch.case('foo', lambda: 'its lambda foo' )
print bar # result "its lambda foo"

bar = switch.case('notfoo', lambda: 'its lambda foo' )
print bar # result empty value

````