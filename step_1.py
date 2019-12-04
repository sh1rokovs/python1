# a = 5
# print(a)
# print(type(a))
#
# a = '5'
# print(a)
# print(type(a))
import sys

b = [23, 'hello', True, 'world!']
c = b
print(sys.getsizeof(b))
# print('id(b)', id(b))
# print('id(c)', id(c))
# print('c == b', c == b)
# print('c is b', c is b)
# # c = b
# #
# # print(b)
# # print(c)
# #
# # # setter -> mutable ...... vs immutable
# # c[0] = False
# # print(b)
# #
# # # getter
# # print(b[0], b[1], b[2],
#
# print(c)
# type(c)
# sys.getsizeof(c)

# print(dir(b))

# b.append(154.9)
# print(b)
# print(b.count(23))

d = [5, 8, 1, 89, 4]
print(d)
d.sort()
print(d)

