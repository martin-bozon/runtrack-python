import re


count = 0

f = open("data.txt", "r")
lines = f.readlines()
f.close()
numbers = {2: 0,3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 0, 18: 0, 19: 0, 20: 0}


for line in lines:
    for mot in line.split(" "):
        wordwhitoutpunctuation = re.sub(r'[^\w\s]', '', mot)
        wordlower = wordwhitoutpunctuation.lower()

        for key in numbers:
            for letter in wordlower:
                if len(wordlower) == key:
                    numbers[key] += 1


print(numbers)
