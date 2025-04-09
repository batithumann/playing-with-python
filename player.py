class Personaje:

    def __init__(self, name, hp=10, str=3, defense=1, exp=0):
        self.name = name
        self.alive = True
        self.hp = hp
        self.max_hp = hp
        self.str = str
        self.defense = defense
        self.exp = exp
        self.next_level = 30

    def __str__(self):
        return f"{self.name}: salud={self.hp}, ataque={self.str}, defensa={self.defense}"

    def attack(self, objetivo):
        dmg = self.str - objetivo.defense
        print(f"{self.name} ataca a {objetivo.name} y le hace {dmg} puntos de daño")
        objetivo.hp -= dmg

    def level_up(self):
        self.max_hp = int(self.max_hp * 1.15)
        self.hp = self.max_hp
        self.str += max(int(self.str * 1.25), 1)
        self.defense += max(int(self.defense * 1.2), 1)
        self.next_level = int(self.next_level * 2.2)