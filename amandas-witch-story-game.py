health = 100
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("You've been drafted to join the Legion of Witches")
choice = input("What is your chosen power? (Lightning or Fire?)")


if choice == "Lightning" or choice == "lightning":
    print("------------------------------------")
    print("You've chosen to be a Lightning Mage.")
    print("Great energy is on your side and you gain +10 health.")
    health = health + 10
    print(f"• Your total health is now {health}")
    print("------------------------------------")
    choice = input("An enemy approaches and taunts you. Would you like to use your special ability? (Y/N)")
    print("------------------------------------")
    if choice == "Y" or choice == "y" or choice == "Yes" or choice == "yes":
        print("You have gained a special ability called Jupiter's Wrath.")
        print("Attacking your opponents at lightning speed, you are cunning yet somewhat clumsy and ")
        print("hurt yourself during your special attack.")
        print("His health has dropped significantly, but his Water Spear attack grazes your leg and you lose 55 health total.")
        health = health - 55
        print(f"• Your health is now at {health}")
        print("------------------------------------")
        print("Realizing the dilemma of using your special attack, you realize you must either")
        choice = input("unleash another attack to finish him off or run away. What will you do? (Run/Fight)")
        print("------------------------------------")
        if choice == "Run" or choice == "run":
            print("You narrowly escape another spell attack as you run away. You've gotten away unscathed,") 
            print("but your actions have consequences and have ranked you in the lower quartile in the Legion.")
            print("You must now return to your faction's headquarters and discuss your actions with your Captain.")
        elif choice == "Fight" or choice == "fight":
            print("Another one of your attacks provides a killing blow to your opponent.")
            print("You are rewarded with loot from his person.")
            choice = int(input("Choose a number between 1 and 10 to decide your prize."))
            print("------------------------------------")
            if choice <= 3:
                print("You are rewarded with the health of your enemy. Gain +200 health.")
                health = health + 200
                print(f"• Your health is now {health}")
                print("Return to base and let your commrades bask in all your glory.")
                print("------------------------------------")
            elif choice >= 4 and choice <= 6:
                print("You gain the strength of your enemy. Return to base and let your commrades bask in all your glory.")
                print("------------------------------------")
            elif choice >=7 and choice <= 9:
                print("You are rewarded with bragging rights. Return to base and let your commrades bask in all your glory.")
                print("------------------------------------")
            # THIS CODE WORKS TOO BUT IS CONFUSING TO READ
            # elif choice <= 6 >4:
            #     print("You gain the strength of your enemy. Return to base and let your commrades bask in all your glory.")
            # elif choice <= 9 >7:
            #     print("You are rewarded with bragging rights.")
            elif choice == 10:
                print("You have gained a new attack called the Tesla Dragon. Return to base and let your commrades bask in all your glory.")
                print("------------------------------------")
    elif choice == "N" or choice == "n" or choice == "No" or choice == "no":
        print("U ded. Game over.")
        print("------------------------------------")
    else:
        print("U dummy. Game over.")
        print("------------------------------------")

elif choice == "Fire" or choice == "fire":
    print("------------------------------------")
    print("You've chosen the path of a Fire Mage.")
    print("Immense passion and wrath burn within you, but provides a")
    print("nice balance in combat. You gain +20 health for inner harmony.")
    health = health + 20
    print(f"Your total health is now {health}")
    print("------------------------------------")
    choice = input("An enemy approaches you in combat. Would you like to use your special ability? (Y/N)")
    print("------------------------------------")
    if choice == "Y" or choice == "y" or choice == "Yes" or choice == "yes":
        print("You have gained a special ability called Pluto's Revenge.")
        print("Attacking your opponents with dark magic, you are so lethal that you sometimes drain yourself of health.")
        print("His health has dropped significantly, but his Light Spear attack grazes your leg and you lose 75 health total.")
        health = health - 75
        print(f"• Your health is now at {health}")
        print("------------------------------------")
        print("Realizing the dilemma of using your special attack, you realize you must either")
        choice = input("unleash another attack to finish him off or run away. What will you do? (Run/Fight)")
        print("------------------------------------")
        if choice == "Run" or choice == "run":
            print("You narrowly escape another spell attack as you run away. You've gotten away unscathed,") 
            print("but your actions have consequences and have ranked you in the lower quartile in the Legion.")
            print("You must now return to your faction's headquarters and discuss your actions with your Captain.")
            print("------------------------------------")
        elif choice == "Fight" or choice == "fight":
            print("Another one of your attacks provides a killing blow to your opponent.")
            print("You are rewarded with loot from his person.")
            choice = int(input("Choose a number between 1 and 10 to decide your prize."))
            print("------------------------------------")
            if choice <= 3:
                print("You are rewarded with the health of your enemy. Gain +200 health.")
                health = health + 200
                print(f"• Your health is now {health}")
                print("Return to base and let your commrades bask in all your glory.")
                print("------------------------------------")
            elif choice >= 4 and choice <= 6:
                print("You gain the strength of your enemy. Return to base and let your commrades bask in all your glory.")
                print("------------------------------------")
            elif choice >=7 and choice <= 9:
                print("You are rewarded with bragging rights. Return to base and let your commrades bask in all your glory.")
                print("------------------------------------")
            elif choice == 10:
                print("You have gained a new attack called Persephone's Song. Return to base and let your commrades bask in all your glory.")
                print("------------------------------------")
    elif choice == "N" or choice == "n" or choice == "No" or choice == "no":
            print("U ded. Game over.")
            print("------------------------------------")
    else:
        print("U dummy. Game over.")
        print("------------------------------------")
else:
    print("U dummy. Game over.")
    print("------------------------------------")