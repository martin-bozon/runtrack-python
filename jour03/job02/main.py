import re

f = open("data.txt", "r")
lines = f.readlines()
print(lines)
f.close()
count = 0


# for line in lines:
#     for mot in line.split(" "):
#         wordwhitoutpunctuation = re.sub(r'[^\w\s]', '', mot)
#         m = re.search(r'(\S[a-zA-Z]*\S)', wordwhitoutpunctuation)
#         print(m)
#         if m != None:
#             count += 1

print(count)
