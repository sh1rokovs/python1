d = [5, 8, 1, 89, 4]
print(d, id(d))

# in place
# d.sort(reverse=False)
# print(d, id(d))

s = d.append('hi')
print(s)
print(d)
# print(d.sort(reverse=False))
# new object returned
# d_sorted = sorted(d)
# print(d_sorted, id(d_sorted))
