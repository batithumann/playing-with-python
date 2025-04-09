import random
from player import Personaje


def main():
    counter = 0

    print("escribe tu nombre")
    nombre = input("> ")
    player = Personaje(nombre)
    while player.alive:
        print(player)

        enemigo = Personaje(
            "enemigo", random.randint(3, 7), random.randint(1, 5), random.randint(0, 2)
        )
        enemigo.exp = enemigo.hp + enemigo.str + enemigo.defense

        print(enemigo)
        while enemigo.hp > 0 and player.hp > 0:
            while True:
                print("1. atacar")
                print("2. escapar")
                n = input("> ")
                if n in ["1", "2"]:
                    break
            if n == "1":
                player.attack(enemigo)
                if enemigo.hp > 0:
                    enemigo.attack(player)
                else:
                    print(f"{enemigo.name} ha muerto")
                    counter += 1
                    player.exp += enemigo.exp
                    if player.exp >= player.next_level:
                        print(f"{player.name} ha subido de nivel!")
                        player.level_up()
                    break
            elif n == "2":
                if random.randint(1, 5) == 5:
                    print(f"{player.name} escapó")
                    break
                else:
                    print(f"{player.name} no logra escapar!")
                    enemigo.attack(player)

            if player.hp <= 0:
                print(f"{player.name} ha muerto")
                print(f"{player.name} logró vencer a {counter} enemigos")
                player.alive = False
                exit


main()
