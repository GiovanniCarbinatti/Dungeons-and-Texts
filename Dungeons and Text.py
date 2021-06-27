import random


items_list = ['cancel', 'potion', 'potion', 'holy water']


'''Hello, everyone! Welcome to this simple project. Enemies aren't balanced enough and the history and mechanics
are in development. It'll be amazing if you could contribute to this game. Let's make together a fun game using
only vanilla python without any GUI. Bugs are expected, please report if you find one.'''


'''Hero classes - Start!'''


class Warrior:
    def __init__(self, attack, defense, life):
        self.attack = attack
        self.defense = defense
        self.life = life
        self.vida_var = life


class Mage:  # In development
    def __init__(self, attack, magicatk, defense, life, mana):
        self.attack = attack
        self.magicatk = magicatk
        self.defense = defense
        self.life = life
        self.mana = mana


class Rogue:  # In development.
    pass


'''enemy classes - Start!'''


class Goblin:
    def __init__(self, enemy_class, attack, defense, life):
        self.enemy_class = enemy_class
        self.attack = attack
        self.defense = defense
        self.life = life


class Orc:
    def __init__(self, enemy_class, attack, defense, life):
        self.enemy_class = enemy_class
        self.attack = attack
        self.defense = defense
        self.life = life


class ElderDragon:
    def __init__(self, enemy_class, attack, defense, life):
        self.enemy_class = enemy_class
        self.attack = attack
        self.defense = defense
        self.life = life


class Zombie:
    def __init__(self, enemy_class, attack, defense, life):
        self.enemy_class = enemy_class
        self.attack = attack
        self.defense = defense
        self.life = life


'''By now, here are the base enemy attributes. Later on, it can be semi-randomized.'''


goblin = Goblin("goblin", 4, 2, 20)

orc = Orc("orc", 8, 0, 45)

elder_dragon = ElderDragon("Elder Dragon", 25, 5, 80)

zombie = Zombie("zombie", 14, 0, 35)

'''Game Start!'''


def main():
    print("Welcome to \033[1;30;47mDungeons And Texts!\033[0;0m")
    menu()


def menu():
    print("Choose the option:\n\n1- Play\n2- How to Play\n3- Exit Game\n")
    choice = int(input(""))
    if choice == 3:
        print("\nI hope to see you again!")
        exit()
    elif choice == 2:
        how_to_play()
    elif choice == 1:
        game_start()
    else:
        print("\nInvalid command!\n")
        menu()


def how_to_play():  # Should be improved, as you can see.
    print("\nWelcome to this ultra-generic text-only RPG!\nthere are some things you should know:"
          "\n\nDungeons and Text is text-only. Please, digit only numbers since the game waits for a number input.\n")
    menu()


def game_start():  # The script of the game goes here. There's only battle now, but exploration and NPC is in the plans.
    hero = create_hero()
    print("\nYou're a brave hero! But there's a monster in your way!\n")
    combat_start(hero, goblin)  # Randomized in the future!
    combat_start(hero, orc)
    combat_start(hero, zombie)
    combat_start(hero, elder_dragon)
    print("The End!")


'''hero creation - Start!'''


def create_hero():
    chosen = False
    print("\nAre you ready to start your epic journey? Let's create your hero!\n")
    while not chosen:
        char = int(input("You can be a:\n1- Warrior\n2- Mage\n3- Rogue\n\n"))
        if char == 1:
            chosen = True
            hero = create_warrior()
        elif char == 2:
            chosen = True
            hero = create_mage()
        elif char == 3:
            chosen = True
            hero = create_rogue()
        else:
            print("This doesn't seem to be a valid option!")
    return hero


def create_warrior():
    print("\nWarrior is a nice choice!\n"
          "You must distribute 50 points between attack, defense and life. Choose wisely!\n")
    attack = int(input("what's your warrior's attack? (Remember: war tanks must shoot!)\n\n"))
    defense = int(input("\nwhat's your warrior's defense? (Remember: a glass cannon breaks on the first attack!)\n\n"))
    life = int(input("\nfinally, what's your max life?\n\n"))
    attributes = attack + defense + life
    if attributes == 50 and life >= 1 and attack >= 0 and defense >= 0:
        print(f"\nExcellent! Now you have a warrior with {attack} attack, {defense} defense and "
              f"{life} max life!")
        hero = Warrior(attack, defense, life)
        return hero
    elif life <= 1:
        print("\nYou can't live without life! Try again!")
        return create_warrior()
    elif attack < 0 or defense < 0:
        print("\nNegative attributes don't make sense to me! Am I wrong? Try again!")
        return create_warrior()
    elif attributes > 50:
        print(f"\nHaha, nice try! But you only have 50 points to distribute, you tried to use "
              f"{attributes} points! Try again!")
        return create_warrior()
    else:
        print(f"\nDo you wanna play the game in the hard mode? You are only using {attributes} points. "
              f"You can use 50!")
        return create_warrior()


def create_mage():
    pass  # should be included in the future


def create_rogue():
    pass  # should be included in the future


'''combat functions - Start!'''


def combat_start(hero, enemy):  # The main function of the combat
    print(f"You found a {enemy.enemy_class}! What will you do?\n")
    while enemy.life > 0 and hero.life > 0:
        print("Your turn!")
        result = combat_choice(hero, enemy)
        if result == "Escape":
            return
        if enemy.life > 0:
            print("The enemy is not dead! Prepare yourself!")
            combat_defense(hero, enemy)
        else:
            print(f"The {enemy.enemy_class} is dead! You are amazing!\n")
        if hero.vida_var < 1:
            print("You are dead! I'm pressing F to pay respect!\n")
            main()


def combat_choice(hero, enemy):  # Player choose if he wants to attack, run away or use items
    choose = int(input("1- Attack\n2- Run away\n3- Items\n\n"))
    if choose == 1:
        critical_hit = critical_check()
        if critical_hit:
            combat_attack(hero, enemy, critical_hit)
        else:
            combat_attack(hero, enemy)
        return hero, enemy
    elif choose == 2:
        flee = combat_run()
        if flee == 1:
            return "Escape"
    elif choose == 3:
        item_menu(hero, enemy)
    else:
        print("\nInvalid option! Try again!\n")


def combat_attack(hero, enemy, critical_hit=False):  # Critical hit is checked and damage is dealt
    damage = hero.attack - enemy.defense
    if damage <= 0:
        damage = 1
    if critical_hit:
        damage *= 2
    enemy.life -= damage
    print(f"\nA sure strike! The {enemy.enemy_class} took {damage} damage!\n")
    return hero, enemy


def combat_run():  # There's a 60% base chance of running away by now. Some battle's can be inescapable in the future.
    print("\nYou're a coward, huh?!")
    flee = random.randint(0, 4)  # Maybe rogues can have a improved chance in the escape calculation in the future...
    if flee <= 2:
        print("Successfully escaped!\n")
        return 1
    else:
        print("Can't escape! Too bad!\n")
        return 0


def combat_defense(hero, enemy):  # Defense is pretty strong now. Balancing will be made in the future.
    damage = enemy.attack - hero.defense
    if damage <= 0:
        damage = 1
    hero.vida_var -= damage
    print(f"Wow, that hurts! You took {damage} damage! Now you have {hero.vida_var}/{hero.life} life!\n")
    return hero, enemy


def critical_check():  # Maybe rogues should have a improved critical ratio...
    criticalcheck = random.randint(0, 7)
    if criticalcheck == 0:
        print("\nCRITICAL HIT!!!")
        return True
    else:
        return False


'''Item use - Start!
Please, note: I tried to code items to be used outside of combat as well as in combat.
Btw they can only be used in combat now and bugs are expected.'''


def item_menu(hero, enemy=None):
    items = item_check()
    print("\nITEMS IN INVENTORY:\n")
    item_count = 0
    for i in items:
        print(item_count, end="- ")
        print(i)
        item_count += 1
    print("\nChoose the item you wanna use or 0 to return to menu:\n")
    item_used = int(input(""))
    if item_used == 0:
        print("")
        combat_choice(hero, enemy)
    elif item_used < 0:
        print("\nInvalid option! Try again!\n")
        item_menu(hero, enemy)
    item_use(hero, items_list[item_used], item_used, enemy)


def item_check():
    return items_list


def item_use(hero, item, item_used, enemy=None):  # More items need to be included.
    if item == "potion":
        heal = int(hero.life * 0.1)
        if hero.vida_var + heal > hero.life:
            heal = int(hero.life - hero.vida_var)
        hero.vida_var += heal
        print(f"\nThat was refreshing! Healed {heal} life points, now you have {hero.vida_var}/{hero.life} life!\n")
    if item == "holy water":
        if enemy.enemy_class == "zombie":
            enemy.life = 0
            print("\nWow, holy water instakilled zombie! That was nice!\n")
        else:
            print(f"\nSeems to have no effect against a {enemy.enemy_class}...\n")
    items_list.pop(item_used)
    return hero, enemy


'''Item use - End!'''


main()
