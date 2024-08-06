

from typing import List


def get_fuck():
    print("fuck")

get_fuck()

def get_luck(username : str):
    print(f"hello my dude from {username}")

def describe_me(you : str, person_type = 'introver'):
    print(f"me and you : {you} is {person_type}")

describe_me('danawan')

def kembalikan_angka_ini(angka : int) -> str:
    return "kembalikan_angka_ini + {angka}"+" "+str(angka).title()

get_luck('danawan')

print(kembalikan_angka_ini(69))

def get_full_name(firstname : str, lastname : str, middlename= '') -> str:
    if middlename:
        name = firstname+" "+middlename+" "+lastname
        return name.title()
    else:
        name = firstname+" "+lastname
        return name.title()


meine_name = get_full_name("danawan", "bimantoro")

def print_listed_anime(anime : List):
    for ani in anime:
        print(ani)

anime = ['naruto', 'one piece', 'hunterxhunter', 'jjk', 'demon slayer']

print_listed_anime(anime)


unprinted_design = ['meem', 'fck', 'yu']

printed_designs = []

def print_shirt(design: List):
    while design:
        printed_design = design.pop()
        print(f"print this way {printed_design}")
        printed_designs.append(printed_design)


print_shirt(unprinted_design[:])

print(unprinted_design)

print(f"mein name ist {meine_name}")
