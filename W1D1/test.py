# x = 25
# y = 17.6

# print(x)
# print(x+y)
# print(x * y)
# print(x ** y)
# print(x / y)
# print(x // y)
# print(x % y)

# print(f'The result is {int(x // y)} remainder {x % y}')

## INPUT
# name = input("what is your name? ")
# print(f"hello {name}")
# print("Hello, %s" % name)

# print(len('box'))

# a = ['a', 'b']
# print(len(a))

## DUCKTYPING 
# a = None
# try:
#   print(len(a))
# except:
#   print(f'{a} has no length')


## ARITHMETIC WITH STRINGS
# Numbers can be combined with strings
# a = "a"
# b = "b"
# an = "an"

# print(b + an)
# print(b + a * 7)
# print(b + an * 2 + a)

# print("$1" + ",000"*3)


## ASSIGNMENT OPERATORS
# i = 1
# i += 5
# print(i)

# i **= 2
# print(i)

# i //= 10
# print(i)

# i *= 10**200
# print(i)
# print(float(i))

# i = 3
# i **= 10**100
# print(i)

## MEANING OF TRUTH IN PYTHON
# a = 1
# b = 1.0
# c = "1"

# print(a == b) # True
# print(a == c) # False
# print(b == c) # False

# if (a == c):
#   print("match")
# elif (a == b):
#   print("a matches b")
# else:
#   print("does not match")

# a = {}
# if (a):
#   print(f"{a} is true")
# else:
#   print(f"{a} is false")


## IDENTITY VS EQUALITY

a = 1
b = 1.0
c = "1"

# print(a == b)   # True
# print(a is b)   # False. kinda acts like === triple equal
# print(c == "1") # True
# print(c is "1") # True. But SyntaxWarning: "is" with a literal. Did you mean "=="?

# print(b == 1 and isinstance(b, int)) # False
# # Checks, if b is an instance of an integer

# print(a == 1 and isinstance(a, int)) # True

print(a)
print(float(a))
print(str(a))