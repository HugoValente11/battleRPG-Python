# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 17:29:04 2020

@author: Hugo
"""

from classes.game import Person, bcolors
from classes.magic import Spells
from classes.inventory import Items
import random

# Instantiate Spells

# Create black spells
fire = Spells("fire", 500, 10, "black")
thunder = Spells("thunder", 100, 10, "black")
blizzard = Spells("blizzard", 100, 10, "black")
quake = Spells("quake", 500, 10, "black")
meteor = Spells("meteor", 100, 10, "black")

# Create white spells
cure = Spells("cure", 100, 10, "white")
cura = Spells("cura", 100, 10, "white")
curaga = Spells("curaga", 1000, 20, "white")


# Instantiate items
potion = Items("Potion", "potion", "Heals for 50 HP", 50)
high_potion = Items("Hi-Potion", "potion", "Heals for 100 HP", 100)
super_potion = Items("Super Potion", "potion", "Heals for 500 HP", 500)
elixir = Items("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
high_elixir = Items("MegaElixir", "elixir", "Fully restores HP/MP of all party member", 9999)

grenade = Items("Grenade", "attack", "Deals 500 damage", 500)


player_spells = [fire, thunder, blizzard, quake, meteor, cure, cura]
enemy_spells = [fire, thunder, blizzard, quake, meteor, curaga]
player_items = [{"item": potion, "quantity": 15}, 
                 {"item": super_potion, "quantity": 5},
                 {"item": elixir, "quantity": 5},
                 {"item": high_elixir, "quantity": 2},
                 {"item": grenade, "quantity": 5 }]
# Instantiate players
player1 = Person("Valos", 2400, 20, 40, 45, player_spells, player_items)
player2 = Person("Nick ", 4100, 30, 45, 60, player_spells, player_items)
player3 = Person("Robot", 3300, 40, 45, 30, player_spells, player_items)

enemy1 = Person("Imp  ", 1000, 30, 1200, 10, enemy_spells, [])
enemy2 = Person("Eren ", 1000, 30, 800, 10, enemy_spells, [])
enemy3 = Person("Imp  ", 1000, 30, 1200, 10, enemy_spells, [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True

while running:
    # Show stats of active players
    print("=============================")
    print("\n\n")
    print("NAME                       HP                                    MP")

    for player in players:
        print("                           _________________________             __________")
        player.get_stats()
    print("\n")
    for enemy in enemies:
        enemy.get_enemy_stats()
        
    # Player turn to attack
    for player in players:
        print("\n")        
        print(bcolors.BOLD + "    " + player.name + bcolors.ENDC)
        player.choose_action()
        choice = int(input("Choose your action: "))
        index = choice - 1
    
        #Choose combat actions
        if index not in range(0,3):
            continue
        
        if index == 0:
            enemy_choice = player.choose_target(enemies)
            damage = player.generate_damage()
            enemies[enemy_choice].take_damage(damage)
            print(f"{player.name.strip()} attacked {enemies[enemy_choice].name.strip()} enemy for:", damage)
            if enemies[enemy_choice].hp == 0:
                print(f"{enemies[enemy_choice].name.strip()} has died.")
                enemies.pop(enemy_choice)
                if len(enemies) == 0:
                    running = False
                    print(bcolors.OKGREEN + bcolors.BOLD + "You have won!" + bcolors.ENDC)
                    break

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose your spell: ")) - 1
            
            if magic_choice == -1:
                continue
            
            spell = player.magic[magic_choice]        
            if spell.cost > player.get_mp():
                print(f"{player.name.strip()} does not have enough MP")
                continue
            
            magic_damage = spell.generate_spell_damage()
            player.reduce_mp(spell.cost)
            print("You have chosen: ", spell.name)
            
            if spell.type == "white":
                player.heal(magic_damage)
                print(bcolors.OKGREEN + f"\n{player.name.strip()} has healed for ", magic_damage, "HP." + bcolors.ENDC)
            elif spell.type == "black":   
                enemy_choice = player.choose_target(enemies)
                enemies[enemy_choice].take_damage(spell.damage)
                print(f"{player.name.strip()} attacked {enemies[enemy_choice].name.strip()} enemy for:", damage)
                if enemies[enemy_choice].hp == 0:
                    print(f"{enemies[enemy_choice].name.strip()} has died.")
                    enemies.pop(enemy_choice)
                    if len(enemies) == 0:
                        running = False
                        print(bcolors.OKGREEN + bcolors.BOLD + "You have won!" + bcolors.ENDC)
                        break
                
        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose your item: ")) - 1
            if item_choice == -1:
                continue
            
            item = player.items[item_choice]['item']
            
            if player.items[item_choice]['quantity'] == 0:
                print(bcolors.FAIL + bcolors.BOLD + "\nNone left..." + bcolors.ENDC)
                continue
            
            player.items[item_choice]['quantity'] -= 1
            
            if item.type == "potion":
                print(bcolors.OKGREEN + bcolors.BOLD + f"\n{item.name} heals for {item.prop} HP." + bcolors.ENDC)
                player.heal(item.prop)
                
            elif item.type == "elixir":
                if item.name == "elixir":
                    print(bcolors.OKGREEN + bcolors.BOLD + f"\n{item.name} restores to maximum HP and MP." + bcolors.ENDC)
                    player.cleanse()
                else:
                    for i in players:
                        i.cleanse()
    
            elif item.type == "attack":
                enemy_choice = player.choose_target(enemies)
                enemies[enemy_choice].take_damage(item.prop)
                print(f"{player.name.strip()} attacked {enemies[enemy_choice].name.strip()} enemy for {damage}")
                if enemies[enemy_choice].hp == 0:
                    print(f"{enemies[enemy_choice].name.strip()} has died.")
                    enemies.pop(enemy_choice)
                    if len(enemies) == 0:
                        running = False
                        print(bcolors.OKGREEN + bcolors.BOLD + "You have won!" + bcolors.ENDC)
                        break
    if not running:
        break
    # Enemies attack
    print(bcolors.BOLD + bcolors.FAIL + "\nEnemies turn to attack...")
    for enemy in enemies: 
        enemy_action = random.randint(0,1)
        
        if enemy_action == 0:
            enemy_damage = enemy.generate_damage()
            player_attacked = random.randint(0, len(players)-1)
            players[player_attacked].take_damage(enemy_damage)
            print(f"{enemy.name.strip()} attacked {players[player_attacked].name.strip()} for {enemy_damage}.")    
            if players[player_attacked].hp == 0:
                print(f"{players[player_attacked].name.strip()} has died.")
                players.pop(player_attacked)
                if len(players) == 0:
                    running = False
                    print(bcolors.FAIL + bcolors.BOLD + "You have lost!" + bcolors.ENDC)
                    break
                
        if enemy_action == 1:
            spell = enemy.choose_enemy_spell()       
            if spell.cost > enemy.get_mp():
                print(f"{enemy.name.strip()} does not have enough MP")
                continue
            
            magic_damage = spell.generate_spell_damage()
            print(f"{enemy.name.strip()} has chosen {spell.name}.")
            
            if spell.type == "white":
                enemy.heal(magic_damage)
                print(bcolors.FAIL + f"{enemy.name.strip()} has healed for ", magic_damage, "HP.")
            elif spell.type == "black":   
                player_attacked = random.randint(0, len(players)-1)
                players[player_attacked].take_damage(spell.damage)
                print(f"{enemy.name.strip()} attacked {players[player_attacked].name.strip()} for {spell.damage} HP.")
                if players[player_attacked].hp == 0:
                    print(f"{players[player_attacked].name.strip()} has died.")
                    players.pop(player_attacked)
                    if len(players) == 0:
                        running = False
                        print(bcolors.FAIL + bcolors.BOLD + "You have lost!" + bcolors.ENDC)
                        break                
    
    print(bcolors.ENDC)




