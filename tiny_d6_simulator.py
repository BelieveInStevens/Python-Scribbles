#! python3
# tiny_d6_simulator: A program for testing the power of various things using the
# Tiny D6 system.


import matplotlib as plt
import numpy as np
import seaborn as sns
from statistics import mean


np.random.seed(777)
n_sims = 100000
cur_success = 5
cur_crit = 5
cur_state = 'Advantage'


def d6_roll():
    return np.random.randint(1,7)

def tiny_d6_test(success_threshold, critical_threshold, advantage_state):
    if advantage_state == 'Advantage':
        rolls = 3
    if advantage_state == 'Disadvantage':
        rolls = 1
    else:
        rolls = 2
    
    results = []
    for i in range(rolls):
        results.append(d6_roll())

    if (advantage_state == 'Advantage' and len(results) == 
                            len(list(filter(lambda x: x >= critical_threshold, results)))):
                                return "Critical!"
    elif len(list(filter(lambda x: x >= success_threshold, results))) >= 1:
        return "Success!"
    else:
        return 'Failure!'


def antimatter_missiles(success_threshold, critical_threshold, advantage_state):
    attack_roll = tiny_d6_test(success_threshold, critical_threshold, advantage_state)
    damage = d6_roll()
    if attack_roll == 'Critical!':
        return damage * 2
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
        return 6
    elif attack_roll == 'Success!':
        return 3
    else:
        return 0


def main_cannon(success_threshold, critical_threshold, advantage_state):
    attack_roll = tiny_d6_test(success_threshold, critical_threshold, advantage_state)
    if attack_roll == 'Critical':
        damage = 4
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
        damage = 4
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


record_antimatter_missiles = []
record_swarm_missiles = []
record_rapid_fire_lasers = []

for runs in range(n_sims):
    record_antimatter_missiles.append(antimatter_missiles(cur_success, cur_crit, cur_state))
    record_swarm_missiles.append(antimatter_missiles(cur_success, cur_crit, cur_state))
    record_rapid_fire_lasers.append(antimatter_missiles(cur_success, cur_crit, cur_state))

def tiny_d6_simulate(weapon, success_threshold, critical_threshold, advantage_state):
    results = []
    for x in range(10000):
        results.append(weapon(success_threshold, critical_threshold, advantage_state))
    return mean(results)

ax = sns.distplot(record_rapid_fire_lasers)
# plt.title("Histogram of Weapon Damage")
ax.set_xlabel("Damage")
ax.set_ylabel("Count")

sns.distplot(record_antimatter_missiles)
sns.distplot(record_rapid_fire_lasers)
sns.distplot(record_swarm_missiles)
