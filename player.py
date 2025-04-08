class Personaje:

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.hp = 10
        self.str = 3
        self.defense = 1

    def __str__(self):
        return f"{self.name}: salud={self.hp}, ataque={self.str}, defensa={self.defense}"

    def attack(self, objetivo):
        dmg = self.str - objetivo.defense
        print(f"{self.name} ataca a {objetivo.name} y le hace {dmg} puntos de daño")
        objetivo.hp -= dmg
