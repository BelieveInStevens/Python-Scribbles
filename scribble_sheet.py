import random as rand, pprint, re


def recursive_guess_the_number():
    print("I'm thinking of a number between 1 and 20.")
    print("If you guess the number correctly, I will give you one (1) attaboy.")
    the_number = rand.randint(1,20)
    def guessing_game(num, guesses_made, remaining_guesses):
        if remaining_guesses == 0:
            print('Nope. The number I was thinking of was ' + str(the_number) + '. Better luck next time!')
            return None
        guess = int(input())
        if guess == the_number:
            print('Good job! It took you ' + str(guesses_made + 1) + ' guesses to guess my number. Thanks for playing!')
        elif guess < the_number:
            print('Your guess is too low.')
            guessing_game(the_number, guesses_made + 1, remaining_guesses - 1)
        elif guess > the_number:
            print('Your guess is too high.')
            guessing_game(the_number, guesses_made + 1, remaining_guesses - 1)
    guessing_game(the_number, 0, 5)

def collatz(number):
    try:
        if number <= 0 or int(number) != float(number):
            print('Function \'collatz\' can only accept positive integers as an argument.')
            return None
        print(str(number))  
        if number == 1:
            return None
        elif number % 2 == 0:
            collatz(number // 2)
        else:
            collatz(3 * number + 1)
    except TypeError:
        print('Function \'collatz\' can only accept positive integers as an argument.')


def cat_list_maker():
    cat_list = []
    while True:
        print('Please enter the name of a cat to add to the list, or press \'Enter\' if you are finished with entering cat names.')
        entry = input()
        if entry == '':
            break
        else:
            cat_list = cat_list + [entry]
    print('The names of your cats are: ')
    for cat in cat_list:
        print(' ' + cat)

my_pets = ['Buddy', 'Ginger', 'Pepper', 'Teddy']
def pet_checker():
    print('Please enter the name of the pet you would like to check:')
    pet = input()
    if pet in my_pets:
        print('Yes ! ' + str(pet) + ' is in the list of pets.')
    else:
        print('I\'m sorry, but I don\'t own a pet named ' + str(pet))

all_guests = {'Alice': {'apples': 5, 'pretzels': 12},
              'Bob': {'ham sandwiches': 3, 'apples': 2},
              'Carol': {'cups': 3, 'apple pies': 1}}

def total_brought(guests, item):
    num_brought = 0
    for key, value in guests.items():
        num_brought += value.get(item, 0)
    return num_brought

'''print('Number of things being broughten:')
print(' - Apples:         ' + str(total_brought(all_guests, 'apples')))
print(' - Apple Pies:     ' + str(total_brought(all_guests, 'apple pies')))
print(' - Cups:           ' + str(total_brought(all_guests, 'cups')))
print(' - Ham Sandwiches: ' + str(total_brought(all_guests, 'ham sandwiches')))
print(' - Pretzels        ' + str(total_brought(all_guests, 'pretzels')))'''


inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'ruby', 'tourmaline', 'magic dagger', 'gold coin', 'arrow']

def inventory_printer(inventory):
    item_total = 0
    print('Inventory:')
    for key in inventory:
        item_total += int(inventory[key])
        print(str(inventory[key]) + ' ' + str(key))
    print('Total Number of Items: ' + str(item_total))

def loot(inventory, new_items):
    for item in new_items:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory[item] = 1
    inventory_printer(inventory)

def name_validator():
    while True:
        print('Enter your age: ')
        age = input()
        if age.isdecimal():
            break
        print('Please enter a number for your age.')

    while True:
        print('Select a new password (letters and numbers only, please):')
        password = input()
        if password.isalnum():
            break
        print('Passwords may only contain letters or numbers.')

def picnic_printer(items_dict, left_width, right_width):
    print('PICNIC ITEMS'.center(left_width + right_width, '-'))
    for k, v in items_dict.items():
        print(k.ljust(left_width) + str(v).rjust(right_width))
picnic_items = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
    
    
def d6_test(state, threshold):
	success = 0
	if state == "Advantage":
		dice = 3
	elif state == "Disadvantage":
		dice = 1
	else:
		dice = 2
	for i in range(dice):
		roll = rand.randint(1,6)
		if roll >= threshold:
			success = 1
	return success     

def d6_simulate(n, state, threshold):
	successes = []
	for i in range(n):
		successes.append(d6_test(state, threshold))
	return(sum(successes) / n)

def exploding_d6_test(iterations):
    totals = [] # Holds the total rolled result from each iteration of d6 rolls.
    total = 0 
    for i in range(iterations):
        while True:
            roll = rand.randint(1,6)
            total += roll
            if roll != 6:
                break 
        totals.append(total)
        total = 0
    return(round(sum(totals) / iterations, ndigits = 2))

def magic_8_ball():
    messages = ['It is certain.',
                'Yes!',
                'It is decidedly so.',
                'Reply hazy. Please try again later.',
                'Ask again later.',
                'Concentrate and ask again.',
                'No!',
                'Very doutful.',
                'It\'ll never happen.']
    print(messages[rand.randint(0,len(messages)-1)])

def list_pretty_print(my_list):
    if len(my_list) <= 1:
        print(my_list, end = '.')
    else:
        result_string = ''
        for i in my_list:
            if i == my_list[-1]:
                result_string += ('and ' + str(i) + '.')
            else:
                result_string += (str(i) + ', ')
        print(result_string)

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
        
def gridprint(grid):
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            print(grid[j][i], end = '')
        print()

table_data = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],    
            ['dogs', 'cats', 'moose', 'goose']]

another_table_data = [
['Buddy', 'Ginger', 'Teddy', 'Pepper'],
['Suzanne', 'Gordon', 'Steven', 'Sara'],
['Zach', 'Kyle', 'Steven', 'Enoch'],
['Zilch', 'Zero', 'Nada', 'Antidisestablishmentarianism']]

def table_printer(table):
    col_widths = [0] * len(table)
    # create one entry per table column to be printed.

    #First, we find and store the length of the longest entry in each table 
    # "column."
    count = 0
    while count < len(table):
        for word in table[count]:
            if len(word) > col_widths[count]:
                col_widths[count] = len(word)
        count += 1


    # Now we can print the table in a perfectly right-justified way.
    for word in range(len(table[0])):
        for item in range(len(table)):
            print(table[item][word].ljust(col_widths[item]), end = ' ')
        print()         
    
phone_number_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first three digits
    (\s|-|\.)?                      # separator
    (\d{4})                         # last four digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    # extension
    )''', re.VERBOSE)

phone_number_regex.search('801-815-1375').groups()
phone_number_regex.search('(801) 815 1375').groups()
phone_number_regex.search('(801)815 1375').groups()