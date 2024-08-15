from test_first import get_formatted_name


print("Enter 'q' at any time to quit ")

while True:
    first = input ("\n Please gibe me first name : ")
    if first == 'q':
        break
    last = input ("Pleas gibe me last name : ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\t Neatly formatted_name : {formatted_name}")

