def test(notes):
    new_notes = []
    for note in notes:
        if note > 40:
            x = 0
            while x < 3:
                if (note + x) % 5 == 0:
                    note = note + x
                x += 1
            new_notes.append(note)
        else:
            new_notes.append(note)
    return new_notes


print(test([83, 82]))
