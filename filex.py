from pathlib import Path

#path = Path('digits.txt')
#contents = path.read_text()
#contents = contents.rstrip()
#print(contents)


try:

    paath = Path('test.txt')

    conts = paath.read_text()
    conts = conts.splitlines()

    for cont in conts:
        print(cont)

except Exception as err:
    print(err)
