import re

f = open("data.txt", "r")
lines = f.readlines()
f.close()
count = 0


for line in lines:
    for mot in line.split(" "):
        wordwhitoutpunctuation = re.sub(r'[^\w\s]', '', mot)
        m = re.findall(r'(\S[a-zA-Z]*\S)', wordwhitoutpunctuation)
        if m != None:
            count += 1

print(count)
