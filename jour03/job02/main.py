import re

f = open("data.txt", "r")
lines = f.readlines()
f.close()
count = 0


for line in lines:
    m = re.search(r'(^[a-zA-Z0-9])', line)
    if m != None:
        count += 1


print(count)
