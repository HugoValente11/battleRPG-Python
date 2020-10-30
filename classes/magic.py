# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 20:13:10 2020

@author: Hugo
"""

import random

class Spells:
    def __init__(self, name, damage, cost, type):
        self.name = name
        self.damage = damage
        self.cost = cost
        self.type = type
        
    def generate_spell_damage(self):
        return random.randrange(self.damage - 5, self.damage + 5)
