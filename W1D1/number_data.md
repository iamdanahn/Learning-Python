# Number data types

### General stuff 
* 'print' command writes messages to the console
* '#' are for single line comments
* """ triple " are for multiline comments 

* +, -, *, /, % - exists
* `**` = exponent
* `//` = integer division
 
### Number data types
1. Integers
  - Whole +/- numbers. No decimals
  - Can be made with `int()`
  - defaults to 0

2. Floating point 
  - +/- Decimal numbers.
  - Can be made with `float()`
  - defaults to 0.0

3. Complex numbers
  - Mix of real part and imaginary parts
  - Ex: 5 + 7j ==> 5 is real, 7 is imaginary
  - Can be made with `complex()`
  - defaults to 0j

`Type-casting` - Converting number types to another 
Needed when converting #s to string format
ex: `print(str(17.0) + ' and ' + str(17))`

### Exponents
print(2**3)        # => 8
print(5.5**15)     # => 127479497357.65536
print(10**30)      # => 1000000000000000000000000000000
print(10.0**30)    # => 1e+30

* Integers stay as integers no matter how large.
* Floating points convert to scientific notation when too large.
    - If too large, will throw error

### Integer Division `//`
// gives other part of %
Essentially, the "floor"

print(47 // 8)         # => 5
print(47 % 8)          # => 7
print(47.0 // 8.0)     # => 5.0
print(47.0 % 8.0)      # => 7.0


### Comparison Ops
Equality operators `< > >= <= == !=` 
Logical operators `and`, `or`, `not` 
Both are combined with comparisons for useful logic.

* Equality operators process left to right BEFORE logical ops
* Logical ops process 
  1. not
  2. and
  3. or

eg: 
a = 4, b = 5
print(not a == b)     # => True
1. a == b     # False
2. not False  # True
VS
print(a == not b)    # => SyntaxError
== ops expects strings, numbers, Booleans or objects
However, Logical ops causes error

print (a == (not b))    # => False
1. `not b` ==> `not True`           # False
2. `a == False` ==> `True == False` # False

# Short circuit
When conditional expressions have definitive answer, it stops processing
eg: 
Expression	  Right side evaluated?
True and  ...	Yes
False and ...	No
True or   ...	No
False or  ...	Yes

With this in mind, place fast functions to the left


# Identity Ops
`is` and `is not` are STRICT comparators
Similar to === in JS
eg: 
  print (2 == '2')    # => False
  print (2 is '2')    # => False
  print ("2" == '2')    # => True
  print ("2" is '2')    # => True
  print (2 == 2.0)    # => True
  print (2 is 2.0)    # => False
  