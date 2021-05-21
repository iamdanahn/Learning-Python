# Boolean
True or False only.

# Logical operators
Py vs JS
  and === &&
  or === ||
  not === !

# Logical AND
print(True and True)    # => True
print(True and False)   # => False
print(False and False)  # => False

# Logical OR
print(True or True)     # => True
print(True or False)    # => True
print(False or False)   # => False

# Logical NOT
print(not True)             # => False
print(not False and True)   # => True
print(not True or False)    # => False

ANY objects can be tested for truthys in `IF` statements or `WHILE` loops

ALL objects are `true` unless one of the following:
* None or False
* 0 or 0.0 (any zero) 
* empty sequence or collection
  - ''
  - []
  - ()
  - {}
  - set()
  - range(0)


# XOR Functions
True  | True   ==> False
True  | False  ==> True
False | True  ==> True
False | False ==> False
