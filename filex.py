from pathlib import Path

#path = Path('digits.txt')
#contents = path.read_text()
#contents = contents.rstrip()
#print(contents)


conts_plus = ''

try:

    paath = Path('test.txt')

    conts = paath.read_text()
    conts = conts.splitlines()

    for cont in conts:
        conts_plus += cont

except Exception as err:
    print(err)


print(conts_plus+"\n")

cats = "Hello cats"
cats.replace('cat', 'dogs')

print(cats)

