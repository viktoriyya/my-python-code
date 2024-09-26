import cmath

# Integer
print(123, "is type of", type(123))

# Float
print(43.23, "is type of", type(43.23))

# Complex
print(4 - 1j, "is type of", type(4 - 1j))

 # String
print("How are you?", "is type of", type("How are you?"))

# Boolean
print(True, "is type of", type(True))


print(f"Is {123} an instance of int: {isinstance(123, int)}")
print(f"Is {43.23} an instance of int: {isinstance(43.23, int)}")
print(f"Is {4 - 1j} an instance of complex: {isinstance(4 - 1j, complex)}")
print(f"Is {'How are you?'} an instance of string: {isinstance('How are you?', str)}")
print(f"Is {True} an instance of string: {isinstance(True, str)}")



