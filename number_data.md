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