b = [23, 'hello', True, 'world!']

# idx = 0
# while idx < len(b):
#     print(b[idx])
#     idx += 1
#
# while True:
#     print(b[idx])
#     idx += 1
#     if idx == len(b):
#         break

password = ''
while True:
    password = input('input password')
    if len(password) < 5:
        continue
    else:
        print('ok')
        break
