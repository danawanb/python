
car = ['volvo', 'wuling', 'toyota']
print(car)
print(car[0])
car.append("byd")
car.append("jjj")
del car[4]


poped_car = car.pop()
print(poped_car)

first_owned = car.pop(0)
print(f"the first car i was owned was a {first_owned.title()}.")

print(car)
car.remove('toyota')

car.append("bmw")
car.append("mercedes")
car.append("lexus")
print(car)

car.sort(reverse=False)
print(f"meine orginal cars are -> {car}")

carx = car[:3]
carx.append("neta")

print(f"my friends cars are -> {carx}")

hero = ("homelander", "starlight")
print(hero[0])

