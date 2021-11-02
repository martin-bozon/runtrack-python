i = 1

while i < 101:
    modulo3 = i % 3
    modulo5 = i % 5
    if (modulo3 == 0) and (modulo5 == 0):
        print("FizzBuzz")
    elif modulo5 == 0:
        print("Buzz")
    elif modulo3 == 0:
        print("Fizz")
    else:
        print(i)

    i += 1
