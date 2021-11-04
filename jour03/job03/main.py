import re

choice = input("Choisis un entier:")
count = 0

f = open("data.txt", "r")
lines = f.readlines()
f.close()


for line in lines:
    for mot in line.split(" "):
        wordwhitoutpunctuation = re.sub(r'[^\w\s]', '', mot)
        m = re.search(r'(\S[a-zA-Z]*\S)', wordwhitoutpunctuation)
        if m != None and m=longueurchoix:
            print(m)
            count += 1

# r'(\S[a-zA-Z]*\S{'+choice+'})'
print(count)
