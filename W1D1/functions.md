# Functions
A set of procedures that will run when called

Consists of:
  - 'def' keyword
  - name of the function
  - list of parameters to the function in parentheses ()
  - colon, :, at the end of the line
  - One tab indentation fro the block of code to run

ie:
```py
############
def exampleFunc():
  print("I'm an example function")
```

### 'Positional Arguments' 
- relying on the position of the arg to specify which paramenter it is
```py
  def average(num1, num2):
    return (num1/num2)

  print(average(6, 2))        # => 3.0
```

### Default parameters
- Can be passed in like JS. 
Defaults must ALWAYS go after parameters without defaults

```py
def greeting(name, saying="Hello"):
    print(saying, name)

greeting("Monica")
# Hello Monica

greeting("Barry", "Hey")
# Hey Barry

#############
```


### Keyword Args (named paramenters)
Python can specify arguments by name w/o destructuring.
Write the parameter and an equal sign before passing in its value.
Can be placed in any order.

If positional arg has no default, value will be provided w/o specifying its keyword arg

```py
def greeting(name, saying="Hello"):
    print(saying, name)

greeting(name="Monica")
# Hello Monica

greeting(name="Barry", saying="Hey")
# Hey Barry

greeting(saying="Hey", name="Barry")
# Hey Barry

# name has no default value, so just provide the value
# saying has a default value, so use a keyword argument
greeting("Monica", saying="Hi")
```

## Anonymous Functions (lambda)
Python requires the keyword "lambda" to make anonymous functions.
Meant to be one-liners. Multi-liners are HIGHLY discouraged

JS version: `const toUpper = s => s.toUpperCase();`
PY version: `toUpper = lambda s: s.upper()`

const = lambda (arguements): arguments + methods