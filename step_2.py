import sys

b = (23, 'hello', True, 'world!')
print(sys.getsizeof(b))
# print(type(b))
# tuple -> immutable
# b[0] = False
# print(b)
print(dir(b))
