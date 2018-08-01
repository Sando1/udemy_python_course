from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


#Create Black Magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")


#Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "black")


#create items
potion = Item('Potion', 'potion', 'heals 50 hp', 50)
hipotion = Item('Hi-Potion', 'potion', 'heals 100 hp', 100)
superpotion = Item('Super-Potion', 'potion', 'heals 500 hp', 500)
elixer = Item('Elixer', 'elixer', 'Fully restores hp/mp of one party member', 9999)
megaelixer = Item('Mega-Elixer', 'elixer', 'Fully restores hp/mp of party', 9999)

grenade = Item('Grenade', 'attack', 'Deals 500 damage', 500)

player_magic = [fire, thunder,blizzard,meteor, cura, cure]
player_items = [{'item': potion, 'qty':15},
                {'item': hipotion, 'qty':15},
                {'item': superpotion, 'qty':15},
                {'item': elixer, 'qty':15},
                {'item': megaelixer, 'qty':15},
                {'item': grenade,'qty':15}]

#create people
valos = Person('Valos', 460, 65, 60, 34, player_magic, player_items)
nick  = Person('Nick', 460, 65, 60, 34, player_magic, player_items)
robot = Person('Robot', 460, 65, 60, 34, player_magic, player_items)

players = [valos, nick, robot]

enemy_magic = [fire, thunder,blizzard,meteor, cura, quake]
enemy_items = [{'item': potion, 'qty':5},
                {'item': hipotion, 'qty':5},
                {'item': superpotion, 'qty':5},
                {'item': elixer, 'qty':15},
                {'item': megaelixer, 'qty':5},
                {'item': grenade,'qty':5}]

enemy_1_b = Person('Magnus', 5000, 65, 45, 25, enemy_magic, enemy_items)
enemy_2_s = Person('Imp', 500, 40, 20, 10, enemy_magic, enemy_items)
enemy_3_s = Person('Imp', 500, 40, 20, 10, enemy_magic, enemy_items)

enemies = [enemy_1_b, enemy_2_s, enemy_3_s]

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:

    for player in players:

        for player in players:
            if player.get_hp() != 0 or player.get_mp() != 0 :
                player.get_stats()

        for enemy in enemies:
            if enemy.get_hp() != 0:
                enemy.get_enemy_stats()

        print("="*80)

        print(bcolors.BOLD + "\n{}'s turn! ".format(player.name))

        #choose enemy to attack
        player.choose_target(enemies)
        enemy_target = int(input('Choose Enemy to Attack: '))
        enemy = enemies[enemy_target]

        player.choose_action()
        choice = int(input('Choose Action: '))

        #Code : Player Choice

        # player chooses attack
        if choice == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print(bcolors.OKBLUE + '\nAttacked Enemy!' + bcolors.ENDC)

        #Player Chooses Magic
        elif choice == 1:
            player.choose_magic()
            mgc_choice = int(input('Choose Magic : '))

            #check for -1
            if mgc_choice == -1:
                continue

            spell = player.mgc[mgc_choice]
            magic_dmg = spell.generate_damage()

            # only cast spell if player has enough magic points
            if player.get_mp() < spell.cost :
                print(bcolors.FAIL + '\nNot Enough Magic Power \n' + bcolors.ENDC)

            else:
                player.reduce_mp(spell.cost)

                if spell.type == 'white':
                    player.heal(magic_dmg)
                    print(bcolors.OKGREEN + '\nHealing Done!' + bcolors.ENDC)

                elif spell.type == 'black':
                    enemy.take_damage(magic_dmg)
                    print(bcolors.OKBLUE + '\nSpell Cast! ' + bcolors.ENDC)


        #if player chooses items
        if choice == 2:
            player.choose_item()
            item_choice = int(input('Choose Item : '))

            #check for -1
            if item_choice == -1:
                continue

            item = player.items[item_choice]['item']

            if  player.items[item_choice]['qty'] == 0:
                print(bcolors.FAIL + '\nNone Left\n' + bcolors.ENDC)
            else:
                if item.type == 'potion':
                    player.heal(item.prop)
                    print(bcolors.OKGREEN + '\nHealing Done! ' + bcolors.ENDC)
                elif item.type == 'elixir':

                    if item.name == 'Mega-Elixer':
                        for p in players:
                            p.set_mp(p.get_max_mp())
                            p.set_hp(p.get_max_hp())
                            print(bcolors.OKGREEN + '\nFully Restored All Players! ' + bcolors.ENDC)

                    else:
                        player.set_mp(player.get_max_mp())
                        player.set_hp(player.get_max_hp())
                        print(bcolors.OKGREEN + '\nFully Restored {}! '.format(player.name) + bcolors.ENDC)

                elif item.type == 'attack':
                    enemy.take_damage(item.prop)
                    print(bcolors.OKBLUE + '\nEnemy Attacked! ' + bcolors.ENDC)

                player.items[item_choice]['qty']-= 1

        else :
            print(bcolors.OKGREEN + '\nIncorrect Choice. You will lose your turn! ' + bcolors.ENDC)

        #check if player won
        for e in enemies:
            if e.get_hp() == 0 :
                del(enemies[enemy_target])

            if len(enemies)== 1:
                print(bcolors.OKGREEN + "You Win!!! " + bcolors.ENDC)
                running = False
                break

        #code for enemy
        #select any enemy
        enemy = enemies[random.randrange(0,len(enemies))]

        #enemy choice and select target player
        enemy_choice = random.randrange(0,3)
        target = players[random.randrange(0,3)]

        #enemy chooses to attack
        if enemy_choice == 0:
            enemy_dmg = enemy.generate_damage()
            target.take_damage(enemy_dmg)
            print(bcolors.HEADER +  bcolors.BOLD + bcolors.FAIL + '\nEnemy Attacked {}'.format(target.name) + bcolors.ENDC)

        #enemy chooses magic
        elif enemy_choice == 1:
            mgc_choice = random.randrange(0,len(enemy_magic))
            spell = enemy.mgc[mgc_choice]
            magic_dmg = spell.generate_damage()

            # only cast spell if player has enough magic points
            if enemy.get_mp() < spell.cost :
                print(bcolors.OKGREEN + '\nEnemy Cannot Cast Spell\n' + bcolors.ENDC)

            else:
                enemy.reduce_mp(spell.cost)

                if spell.type == 'white':
                    enemy.heal(magic_dmg)
                    print(bcolors.FAIL + '\nEnemy Is Healed!' + bcolors.ENDC)

                elif spell.type == 'black':
                    target.take_damage(magic_dmg)
                    print(bcolors.WARNING + '\nSpell Cast On {}! '.format(target.name) + bcolors.ENDC)

        #enemy chooses item
        elif enemy_choice == 2:
            item_choice = random.randrange(0,len(enemy_items))
            item = enemy.items[item_choice]['item']

            if  enemy.items[item_choice]['qty'] == 0:
                print(bcolors.OKGREEN + '\nNone Left\n' + bcolors.ENDC)
            else:
                if item.type == 'potion':
                    enemy.heal(item.prop)
                    print(bcolors.FAIL + '\nEnemy is Healed!' + bcolors.ENDC)

                elif item.type == 'elixir':

                    if item.name == 'Mega-Elixer':
                        for e in enemies:
                            e.set_mp(e.get_max_mp())
                            e.set_hp(e.get_max_hp())
                            print(bcolors.FAIL + '\nAll Enemies Are Healed! ' + bcolors.ENDC)

                    else:
                        enemy.set_mp(enemy.get_max_mp())
                        enemy.set_hp(enemy.get_max_hp())
                        print(bcolors.FAIL + '\n{} Healed! '.format(enemy.name) + bcolors.ENDC)

                elif item.type == 'attack':
                    target.take_damage(item.prop)
                    print(bcolors.OKBLUE + '\n{} Attacked! '.format(target.name) + bcolors.ENDC)

                enemy.items[item_choice]['qty']-= 1

        #check if enemy won
        defeated = 0
        for p in players:
            if p.get_hp() == 0:
                defeated += 1
                if defeated > len(players)/2:
                    print(bcolors.FAIL + " You Have Been Defeated! " + bcolors.ENDC)
                    running = False
                    break



