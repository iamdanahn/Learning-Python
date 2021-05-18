# Variables

## Ducktyping
Programming style that avoids checking an object's "type" to see what it can do.
How to check types? `type()` or `isinstance()` or `hasattr()`

## Assigning variables
* No "let, var, const"s here. Assignment of values declares variables. like Ruby!
* Variables can be chained to give the same initial value.
* Variables can be reassigned anytime

  a = 7
  print(a)         # => 7

  count = max = min = 0
  print(count)           # => 0
  print(max)             # => 0
  print(min)             # => 0

  a = 17
  print(a)         # => 17
  a = 'seventeen'
  print(a)         # => seventeen


* null === None aka variable that has no value
None is a NoneType in Python.
  my_var = None
  print(my_var is None)     # => True

