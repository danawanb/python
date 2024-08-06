from typing import List


halo = "kakakak"

print(halo)


lista = ["danawan", "bimantoro", "putri", "tamara"]

lista.append("haaha")
lista.append("lmao")

for li in lista:
    print(li)


bansos = "jokowi"

if bansos == "jokowi":
    print("blhohooh")
elif bansos == "proro":
    print("janggar")
else:
    print("hauuaua")


def rax(n :int):
    print("rax {}".format(n))


rax(69)

org = {
        "name" : "danawan",
        "age" : 27,
        }

print(org)


anime = []
for i in range (10) :
    anime.append("naruto")

print(anime)

age = input("Berapa umurmu ? ")
age = int(age)
print("umurmu adalah "+ str(age))

def describe_pet(animal_type : str, pet_name : str):
    print(f"i have a {animal_type}.")
    print(f"my {animal_type} 's name is {pet_name}")

describe_pet('anjing', 'blackie')

def hello(anime : str, age = 75):
    print(f"hello {anime} is {age}")

hello("one piece")

def greet_users(users : List[str]):
    for user in users:
        print(user)

users_list = ["putri", "tamara"]
greet_users(users_list)


