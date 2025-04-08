import random
from player import Personaje

def main():
    print("escribe tu nombre")
    nombre = input("> ")
    player = Personaje(nombre)
    while player.alive:
        print(player)
       
        enemigo = Personaje("enemigo")
        enemigo.hp = random.randint(3,7)
        enemigo.str = random.randint(1,5)
        enemigo.defense = random.randint(0,2)

        counter = 0
       
        print(enemigo)
        while(enemigo.hp > 0 and player.hp > 0):
            print("1. atacar")
            print("2. escapar")
            n = input("> ")
            if n == "1":
                player.attack(enemigo)
                if enemigo.hp > 0:
                    enemigo.attack(player)
            elif n == "2":
                if random.randint(1,5) == 5:
                    print(f"{player.name} escapó")
                else:
                    print(f"{player.name} no logra escapar!")
                    enemigo.attack(player)
            else:
                enemigo.attack(player)
            if player.hp <= 0:
                print(f"{player.name} ha muerto")
                print(f"{player.name} logró vencer a {counter} enemigos")
                player.alive = False
                exit
            if enemigo.hp <= 0:
                print(f"{enemigo.name} ha muerto")
                counter += 1
                break
       
   

main()
