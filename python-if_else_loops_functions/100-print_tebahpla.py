#!/usr/bin/python3
result_str = ""
s = True
for c in range(ord('a'), ord('b')):
    result_str += i.upper() if s else i.lower()
    if i.isalpha():
       s = not s
return result_str
print("{:c}".format(c), end="")
