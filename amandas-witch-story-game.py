from time import sleep
import sys
import random

def typewriter(str):
    for x in str:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.04)
    print('')


health = 100
damage = [5, 10, 20, 25, 40, 50, 60, 75, 80, 100]
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
typewriter("You've been drafted to join the Legion of Witches")
choice = input("What is your chosen power? (Lightning or Fire?)")


if choice == "Lightning" or choice == "lightning":
    print("------------------------------------")
    typewriter("You've chosen to be a Lightning Mage.")
    typewriter("Great energy is on your side and you gain +10 health.")
    health = health + 10
    typewriter(f"• Your total health is now {health}")
    print("------------------------------------")
    choice = input("An enemy approaches and taunts you. Would you like to use your special ability? (Y/N)")
    print("------------------------------------")
    if choice == "Y" or choice == "y" or choice == "Yes" or choice == "yes":
        enemy_health = 70
        typewriter("You have gained a special ability called Jupiter's Wrath.")
        typewriter("Attacking your opponents at lightning speed, you are cunning yet somewhat clumsy and ")
        typewriter("hurt yourself during your special attack.")
        typewriter("His health has dropped significantly, but his Water Spear attack grazes your leg and you lose 5 health total.")
        health = health - 5
        typewriter(f"• Your health is now at {health}")
        print("------------------------------------")
        while health > 0 and enemy_health > 0:
            choice = input("What would you like to do next? Unleash another attack or run away? (Run/Fight)")
            print("------------------------------------")
            if choice == "Run" or choice == "run":
                    typewriter("You narrowly escape another spell attack as you run away. You've gotten away unscathed,") 
                    typewriter("but your actions have consequences and have ranked you in the lower quartile in the Legion.")
                    typewriter("You must now return to your faction's headquarters and discuss your actions with your Captain.")
            elif choice == "Fight" or choice == "fight":
        # Provide additional scenarios here to keep the loop going
                attack = random.choice(damage)
                typewriter(f"Another one of your attacks hurts your enemy for {attack} damage.")
                enemy_health = enemy_health - attack
                if enemy_health >0:
                    typewriter(f"His health is now at {enemy_health}")
                    print("------------------------------------")
                    #write code here to simulate taking damage from the enemy
                    hurt = random.choice(damage)
                    health = health - hurt
                    typewriter(f"Your enemy strikes you for {hurt} damage.")
                    typewriter(f"• Your health is now {health}")
                if enemy_health <= 0:
                    typewriter("You've successfully defeated your opponent.")
                    typewriter("You are rewarded with loot from his person.")
                    choice = int(input("Choose a number between 1 and 10 to decide your prize."))
                    print("------------------------------------")
                    if choice <= 3:
                        typewriter("You are rewarded with the health of your enemy. Gain +200 health.")
                        health = health + 200
                        typewriter(f"• Your health is now {health}")
                        typewriter("Return to base and let your commrades bask in all your glory.")
                        print("------------------------------------")
                    elif choice >= 4 and choice <= 6:
                        typewriter("You gain the strength of your enemy. Return to base and let your commrades bask in all your glory.")
                        print("------------------------------------")
                    elif choice >=7 and choice <= 9:
                        typewriter("You are rewarded with bragging rights. Return to base and let your commrades bask in all your glory.")
                        print("------------------------------------")
                # THIS CODE WORKS TOO BUT IS CONFUSING TO READ
                # elif choice <= 6 >4:
                #     typewriter("You gain the strength of your enemy. Return to base and let your commrades bask in all your glory.")
                # elif choice <= 9 >7:
                #     typewriter("You are rewarded with bragging rights.")
                elif choice == 10:
                    typewriter("You have gained a new attack called the Tesla Dragon. Return to base and let your commrades bask in all your glory.")
                    print("------------------------------------")
    elif choice == "N" or choice == "n" or choice == "No" or choice == "no":
        typewriter("U ded. Game over.")
        print("------------------------------------")
    else:
        typewriter("U dummy. Game over.")
        print("------------------------------------")

elif choice == "Fire" or choice == "fire":
    print("------------------------------------")
    typewriter("You've chosen the path of a Fire Mage.")
    typewriter("Immense passion and wrath burn within you, but provides a")
    typewriter("nice balance in combat. You gain +20 health for inner harmony.")
    health = health + 20
    typewriter(f"Your total health is now {health}")
    print("------------------------------------")
    choice = input("An enemy approaches you in combat. Would you like to use your special ability? (Y/N)")
    print("------------------------------------")
    if choice == "Y" or choice == "y" or choice == "Yes" or choice == "yes":
        typewriter("You have gained a special ability called Pluto's Revenge.")
        typewriter("Attacking your opponents with dark magic, you are so lethal that you sometimes drain yourself of health.")
        typewriter("His health has dropped significantly, but his Light Spear attack grazes your leg and you lose 75 health total.")
        health = health - 75
        typewriter(f"• Your health is now at {health}")
        print("------------------------------------")
        typewriter("Realizing the dilemma of using your special attack, you realize you must either")
        choice = input("unleash another attack to finish him off or run away. What will you do? (Run/Fight)")
        print("------------------------------------")
        if choice == "Run" or choice == "run":
            typewriter("You narrowly escape another spell attack as you run away. You've gotten away unscathed,") 
            typewriter("but your actions have consequences and have ranked you in the lower quartile in the Legion.")
            typewriter("You must now return to your faction's headquarters and discuss your actions with your Captain.")
            print("------------------------------------")
        elif choice == "Fight" or choice == "fight":
            typewriter("Another one of your attacks provides a killing blow to your opponent.")
            typewriter("You are rewarded with loot from his person.")
            choice = int(input("Choose a number between 1 and 10 to decide your prize."))
            print("------------------------------------")
            if choice <= 3:
                typewriter("You are rewarded with the health of your enemy. Gain +200 health.")
                health = health + 200
                typewriter(f"• Your health is now {health}")
                typewriter("Return to base and let your commrades bask in all your glory.")
                print("------------------------------------")
            elif choice >= 4 and choice <= 6:
                typewriter("You gain the strength of your enemy. Return to base and let your commrades bask in all your glory.")
                print("------------------------------------")
            elif choice >=7 and choice <= 9:
                typewriter("You are rewarded with bragging rights. Return to base and let your commrades bask in all your glory.")
                print("------------------------------------")
            elif choice == 10:
                typewriter("You have gained a new attack called Persephone's Song. Return to base and let your commrades bask in all your glory.")
                print("------------------------------------")
    elif choice == "N" or choice == "n" or choice == "No" or choice == "no":
            typewriter("U ded. Game over.")
            print("------------------------------------")
    else:
        typewriter("U dummy. Game over.")
        print("------------------------------------")
else:
    typewriter("U dummy. Game over.")
    print("------------------------------------")