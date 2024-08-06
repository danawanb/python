
message = input("Who are you dude ? ")
print(f"\n Hello, {message} !")



def goblok(num : int):
    current = 0
    while current <= num:
        print("blok")
        current += 1


goblok(6)
print("end me")

class Car:
    def __init__(self, brand: str, engine : list[str]):
        self.brand = brand
        self.engine = engine

    def get_brand(self)-> str :
        return self.brand


v8 = ["v8", "2jz"]
xx = Car("zenix", v8)

print(xx.get_brand())


print(xx.engine)
