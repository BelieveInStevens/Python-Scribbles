#! python3

name = 'Steven Day'
age = 32 
height = 72
weight = 155
eyes = 'Hazel'
teeth = 'Yellowing'
hair = None

print('Let\'s talk about %s.' % name)
print('He\'s %d inches tall.' % height)
print('He only weighs %d pounds.' % weight)
print('Pretty skeletal, huh?')
print('He\'s got %s eyes and %s hair' % (eyes, hair))
print('His teeth are usually %s depending on how much coffee he\'s been drinking' % teeth)

print('If I add %d, %d, and %d, then I get %d.' % (age, height, 
    weight, age + height + weight))

print('\n\nNow, let\'s do it again, but better!\n\n')

print(f'Let\'s talk about {name}.')
print(f'He\'s {height} inches tall.')
print(f'He only weighs {weight} pounds.')
print(f'Pretty skeletal, huh?')
print(f'He\'s got {eyes} eyes and {hair} hair.')
print(f'His teeth are usually {teeth} \
depending on how much coffee he\'s been drinking')

print(f'If I add {age}, {height}, and {weight}, then I get \
{age + height + weight}.', sep = '')
