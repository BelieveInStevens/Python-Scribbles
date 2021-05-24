#! python3


from sys import argv


script, user_name = argv
prompt = '==>'

print(f'Hi {user_name}!, I\'m the {script} script!')
print('I\'m gonna ask you a few questions.')
likes = input(f'Do you like me, {user_name}?')
lives = input(f'Where do you live, {user_name}?')
computer = input('What kind of computer do you have?')

print (f'''
Alright, so you said {likes} about liking me.
You live in {lives}. Not really sure where that is.
And you have a {computer} computer. Nice.''')

