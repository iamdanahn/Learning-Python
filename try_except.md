Exception - An error that occurs while a program is executing 
Catching exceptions - The process of detecting these execution errors

"try ... except" is similar to "if ... else"
However, Try will attempt its block and if it errors, it will go to the exception and continue on. If no errors, exception is skipped.
In the If block, if it crashes, the app crashes.


### Except
Exceptions can be specified to execute only on certain ones
```py
  a = 100
  b = 0
  try:
      print(a / b)
  except ZeroDivisionError: # this except on ZeroDivisionError
      pass # special keyword and will not output anything
  except (TypeError, NameError): # this except on either TypeError/NameError 
    print("ERROR!")
```

### Else
Else runs when no exceptions are thrown.
Must come after all "Except"s
```py
# tuple of file names
files = ('one.txt', 'two.txt', 'three.txt')

# simple loop
  for filename in files: 
    try:
        # open the file in read mode
        f = open(filename, 'r')
    except OSError:
        # handle the case where file does not exist or permission is denied
        print('cannot open file', filename)
    else:
        # do stuff with the file object (f)
        print(filename, 'opened successfully')
        print('found', len(f.readlines()), 'lines')
        f.close()
```

### Finally
This clause acts as "clean-up" actions and executes in all circumstances.
```py
  def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print("Result is", result)
    finally:
        print("Finally...")
```

### Return statements
If 'try' or 'except' blocks include returns, 'finally' blocks will run BEFORE the return.
If 'finally' has a return, the 'finally' return will execute over the other returns