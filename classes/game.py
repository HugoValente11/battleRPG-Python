# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 17:28:25 2020

@author: Hugo
"""

import random

class bcolors:
    HEADER = '\033[35m'
    OKBLUE = '\033[34m'
    OKGREEN = '\033[32m'
    WARNING = '\033[33m'
    FAIL = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
    
class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.high_attack = atk + 10
        self.low_attack = atk - 10
        self.defense = df
        self.magic = magic
        self.items = items
        self.actions = ["ATTACK","MAGIC", "ITEMS"]
        
        
    def generate_damage(self):
        return random.randrange(self.low_attack,self.high_attack)
        
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp
    
    def get_max_hp(self):
        return self.max_hp
    
    def get_hp(self):
        return self.hp
    
    def heal(self,heal):
        self.hp += heal
        if self.hp > self.max_hp:
            self.hp = self.max_hp
    
    def get_max_mp(self):
        return self.max_mp
    
    def get_mp(self):
        return self.mp
    
    def reduce_mp(self, cost):
        self.mp -= cost
   
    def choose_action(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "    Actions available:" + bcolors.ENDC)
        for action in self.actions:
            print("    " + str(i), action)
            i += 1
    
    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "\n    Magic spells available:" + bcolors.ENDC)
        for spell in self.magic:
            print("    ", str(i), spell.name, "(cost:", spell.cost,")")
            i += 1

    def choose_item(self):
        i = 1
        print(bcolors.OKGREEN + bcolors.BOLD + "\n    Items available:" + bcolors.ENDC)
        for item in self.items:
            print(f"    {i}. {item['item'].name}: {item['item'].description} (x{item['quantity']}).")
            i += 1
            
    def cleanse(self):
        self.hp = self.max_hp
        self.mp = self.max_mp
        
    def get_stats(self):
        hp_bar = ""
        hp_ticks = (self.hp / self.max_hp) * 25
        
        while len(hp_bar) < 25:
            if hp_ticks > 0:
                hp_bar += "█"
                hp_ticks -= 1
            else:
                hp_bar += " "

        mp_bar = ""
        mp_ticks = (self.mp / self.max_mp) * 10                
        while len(mp_bar) < 10:
            if mp_ticks > 0:
                mp_bar += "█"
                mp_ticks -= 1
            else:
                mp_bar += " "
        print(f"{bcolors.BOLD}{self.name}          {self.hp:{len(str(self.max_hp))}}/{self.max_hp}  |{bcolors.OKGREEN}{hp_bar}{bcolors.ENDC}|    {bcolors.BOLD}{self.mp:{len(str(self.max_mp))}}/{self.max_mp}  |{bcolors.OKBLUE}{mp_bar}{bcolors.ENDC}|")

       
    def get_enemy_stats(self):
        hp_bar = ""
        hp_ticks = (self.hp / self.max_hp) * 50
        
        while len(hp_bar) < 50:
            if hp_ticks > 0:
                hp_bar += "█"
                hp_ticks -= 1
            else:
                hp_bar += " "
                
        print(f"{bcolors.BOLD}{self.name}          {self.hp:{len(str(self.max_hp))}}/{self.max_hp}  |{bcolors.FAIL}{hp_bar}{bcolors.ENDC}|")

    def choose_target(self, enemies):
        print("Enemies:")
        i = 1
        for enemy in enemies:
            print(f"    {i}. {enemy.name}")
            i += 1
        choice = int(input("Choose enemy to attack: ")) - 1
        return choice
            