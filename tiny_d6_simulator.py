#! python3
# tiny_d6_simulator: A program for testing the power of various things using the
# Tiny D6 system.

import random as r
from statistics import mean

def tiny_d6_roll():
    return r.randint(1,6)

def tiny_d6_test(success_threshold, critical_threshold, advantage_state):
    rolls = []
    if advantage_state == 'Advantage':
        for i in range(3):
            rolls.append(tiny_d6_roll())
    if advantage_state == 'Disadvantage':
        rolls.append(tiny_d6_roll())
    else:
        for i in range(2):
            rolls.append(tiny_d6_roll())
    if (advantage_state == 'Advantage' and 
    len(rolls) == len(list(filter(lambda x: x >= critical_threshold, rolls)))):
        return "Critical!"
    elif len(list(filter(lambda x: x >= success_threshold, rolls))) >= 1:
        return "Success!"
    else:
        return 'Failure!'

def antimatter_missiles(success_threshold, critical_threshold, advantage_state):
    attack_roll = tiny_d6_test(success_threshold, critical_threshold, advantage_state)
    damage = tiny_d6_roll()
    if attack_roll == 'Critical!':
        return damage + 1
    elif attack_roll == 'Success!':
        return damage
    else:
        return 0

def armor_piercing_axe(success_threshold, critical_threshold, advantage_state):
    attack_rolls = []
    for i in range(3):
        if tiny_d6_test(success_threshold, critical_threshold, 'Disadvantage') == 'Success!':
            attack_rolls.append(1)
    return sum(attack_rolls)

def plasma_cannons(success_threshold, critical_threshold, advantage_state):
    attack_roll1 = tiny_d6_test(success_threshold, critical_threshold, advantage_state)
    attack_roll2 = tiny_d6_test(success_threshold, critical_threshold, 'Disadvantage')
    if attack_roll1 == 'Critical!':
        attack_damage1 = 2
    elif attack_roll1 == 'Success!':
        attack_damage1 = 1
    else:
        attack_damage1 = 0
    if attack_roll2 == 'Success!':
        attack_damage2 = 1
    else:
        attack_damage2 = 0
    if attack_damage1 > 0 and attack_damage2 > 0:
        return 1 + attack_damage1 + attack_damage2
    else:
        return attack_damage1 + attack_damage2 

def charge_cannon(success_threshold, critical_threshold, advantage_state):
    attack_roll = tiny_d6_test(success_threshold, critical_threshold, 'Disadvantage')
    if attack_roll == 'Success!':
        return 6
    else:
        return 0

def rapid_fire_lasers(success_threshold, critical_threshold, advantage_state):
    num_tests = 3
    damage = 0
    while num_tests > 0:
        attack_roll = tiny_d6_test(success_threshold, critical_threshold, 'Disadvantage')
        if attack_roll == 'Success!':
            damage += 1
        else:
            num_tests -= 1
    return damage

def big_glowy_sword(success_threshold, critical_threshold, advantage_state):
    attack_roll = tiny_d6_test(success_threshold, critical_threshold, advantage_state)
    if attack_roll == 'Critical!':
        return 4
    elif attack_roll == 'Success!':
        return 3
    else:
        return 0
    
def main_cannon(success_threshold, critical_threshold, advantage_state):
    attack_roll = tiny_d6_test(success_threshold, critical_threshold, advantage_state)
    if attack_roll == 'Critical':
        damage = 3
    elif attack_roll == 'Success!':
        damage = 2
    else: 
        damage = 0
    return damage

def automatic_cannon(success_threshold, critical_threshold, advantage_state):
    attack_roll1 = tiny_d6_test(success_threshold, critical_threshold, advantage_state)
    attack_roll2 = tiny_d6_test(success_threshold, critical_threshold, advantage_state)
    if attack_roll1 == 'Critical':
        attack1_damage = 2
    elif attack_roll1 == 'Success!':
        attack1_damage = 1
    else:
        attack1_damage = 0
    if attack_roll2 == 'Critical':
        attack2_damage = 2
    elif attack_roll2 == 'Success!':
        attack2_damage = 1
    else:
        attack2_damage = 0
    return attack1_damage + attack2_damage

def retractable_sword(success_threshold, critical_threshold, advantage_state):
    attack_roll = tiny_d6_test(success_threshold, critical_threshold, advantage_state)
    if attack_roll == 'Critical!':
        damage = 3
    elif attack_roll == 'Success!':
        damage = 2
    else:
        damage = 0
    return damage

def swarm_missiles(success_threshold, critical_threshold, advantage_state):
    num_tests = 6
    damage = 0
    while num_tests > 0:
        attack_roll = tiny_d6_test(success_threshold, critical_threshold, 'Disadvantage')
        if attack_roll == 'Success!':
            damage += 1
        num_tests -= 1
    if damage == 6:
        return 7
    else:
        return damage

def tiny_d6_simulate(weapon, success_threshold, critical_threshold, advantage_state):
    results = []
    for x in range(10000):
        results.append(weapon(success_threshold, critical_threshold, advantage_state))
    return mean(results)