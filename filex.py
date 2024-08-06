from pathlib import Path

path = Path('digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)

