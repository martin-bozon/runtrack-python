text = input('Ecris ici mécréant:')

f = open("output.txt", "w")
f.write(text)
f.close()

f = open("output.txt", "r")
print(f.read())
f.close()
