import re

choice = int (input("Choisis un entier:"))
count = 0

f = open("data.txt", "r")
lines = f.readlines()
f.close()


for line in lines:
    for mot in line.split(" "):
        wordwhitoutpunctuation = re.sub(r'[^\w\s]', '', mot)
        if len(wordwhitoutpunctuation) == choice:
            m = re.search(r'(\S[a-zA-Z]*\S)', wordwhitoutpunctuation)
            if m != None:
                count += 1


print(count)
