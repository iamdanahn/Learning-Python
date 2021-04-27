# String data types

* Uses ' (single quotes) and " (double quotes) like JS
To use both:
eg: 'Jodi asked, "What\'s up, Sam?"'

* Multi-line strings use (''') triple single quotes

* `len()` calculates string length aka .length for JS
* Can index strings with `[]`
    print("Spaghetti"[0])    # => S
    print("Spaghetti"[4])    # => h

* Last index with `[-1]`, like Ruby!

* Range of letters with `[#:#]` ==> up to, but not including
Eg:
    print("Spaghetti"[1:4])  # => pag
    print("Spaghetti"[4:-1])    # => hett
    print("Spaghetti"[4:4])  # => (empty string)

* Can omit `[:#]` or `[#:]`
Eg:
    print("Spaghetti"[:4])  # => Spag
    print("Spaghetti"[:-1])    # => Spaghett
    print("Spaghetti"[1:])  # => paghetti
    print("Spaghetti"[-4:])    # => etti

* If indexing directly into non-existing place, ERROR OCCURS
    print("Spaghetti"[15])    # => IndexError: string index out of range
    print("Spaghetti"[-15])    # => IndexError: string index out of range
* But its ok if ranged
    print("Spaghetti"[:15])    # => Spaghetti
    print("Spaghetti"[15:])    # => (empty string)
    print("Spaghetti"[-15:])    # => Spaghetti
    print("Spaghetti"[:-15])    # => (empty string)
    print("Spaghetti"[15:20])    # => (empty string)

## String Functions

`.index('a')` 
- calculates first position of the character
  print("Spaghetti".index("h"))    # => 4
  print("Spaghetti".index("t"))    # => 6
- returns ERROR, if char not found
  print("Spaghetti".index("s"))    # => ValueError: substring not found

`.count('a')` - returns count of chars. returns 0 if none.

`+` to string concat
  print("gold" + "fish")    # => goldfish
`*` to multiply string
  print("s"*5)              # => sssss
