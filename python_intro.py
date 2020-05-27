# Basic data types
print(23 + 45 - 5)
print(4 * 5)
print(2 ** 3) # Exponential
print(1 // 2)

string_one = "mimi ni mkenya"
string_two = 'na mimi ni mwafrika'
print(string_one)
print(string_one.upper())
print(string_one.lower())
print(string_one.capitalize())
print(string_one + string_two)
print(string_one + " " + string_two)

print (type(string_one))

# Boolean data type
print(23 > 4)
print(1 == 1)
print(2 != 2.0)
print(3 == 5 and 4 < 1)
print(not True)
import numpy as np

bool_array = np.array([True, False])
bool_array.astype(int)