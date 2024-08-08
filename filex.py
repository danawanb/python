from pathlib import Path

path = Path('digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)


try:

    paath = Path('test.txt')

    conts = path.read_text()
    conts = conts.split()

    for cont in conts:
        print(cont)

except Exception as err:
    print(err)
