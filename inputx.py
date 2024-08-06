animals = ['cat', 'elephant', 'doplhin', 'cow', 'cat', 'tiger']
print(animals)

while 'cat' in animals:
    animals.remove('cat')


print(animals)

def make_indomie(size : int, *toppings : str):
    print(f"\n Making indomie with a {size}")
    for topping in toppings:
        print(f"using - {topping}")


make_indomie(2, 'lettuce', 'chile', 'sausage', 'cheese')
