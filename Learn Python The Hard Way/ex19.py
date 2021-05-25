#! python3

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f'You have {cheese_count} cheese!')
    print(f'You have {boxes_of_crackers} boxes of crackers!')
    print('Man! That\'s enough for a party!')
    print('Get a blanket, dude!')

    print(f'We can just give the function parameters directly:')
    cheese_and_crackers(20, 30)

    print('OR, we cam use varibles from our script:')
    amount_of_cheese = 10
    amount_of_crackers = 50

    cheese_and_crackers(amount_of_cheese, amount_of_crackers)

    print('We can even do math inside, too!')
    cheese_and_crackers(amount_of_cheese + 20, amount_of_crackers - 20)

    