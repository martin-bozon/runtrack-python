def test(note):
    if note > 40:
        x = 0
        while x < 4:
            if (note + x) % 5 == 0:
                print('done', note + x)
        x += 1

    else:
        print('fail:', note)


test(83)
