class Human():
    def __init__(self, name : str, age : int) -> None:
        self.name = name
        self.age = age

class Skill():
    def __init__(self, rarity  = 'common') -> None:
        self.rarity = rarity

    def get_skill_num(self) -> int:
        if self.rarity == 'common':
            return 0
        elif self.rarity == 'rare':
            return 1
        elif self.rarity == 'ultra rate':
            return 2
        else:
            return 0

class Hero(Human):
    def __init__(self, name: str, age: int, skill : str) -> None:
        super().__init__(name, age)
        if skill:
            self.skill = Skill(skill)
        else:
            self.skill = Skill()
    
    def get_hero_skill(self) -> Skill:
        return self.skill

    def is_old(self) -> bool:
        if self.age > 58:
            return True
        else:
            return False
