import random as r

def get_answer(answer_number):
    if answer_number == 1:
        return 'It is certain.'
    elif answer_number == 2:
        return 'It is decidedly so.'
    elif answer_number == 3:
        return 'Yes!'
    elif answer_number == 4:
        return 'Reply hazy, try again later.'
    elif answer_number == 5:
        return 'Ask again later.'
    elif answer_number == 6:
        return 'Concentrate and ask again.'
    elif answer_number == 7:
        return 'My reply is no.'
    elif answer_number == 8:
        return 'Outlook not so good.'
    else:
        return 'You have broken the skeins of fate.'

print(get_answer(r.randint(1,9)))
