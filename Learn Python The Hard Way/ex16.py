#! python3


from sys import argv


script, filename = argv
print(f'We\'re going to erase {filename}.')
print(f'If you don\'t want that to happen, press Ctrl+C.')
input(f'If you do actually want {filename} to be deleted, press RETURN:  ')

print('Opening the file...')
target = open(filename, 'w')

# print('Truncating the file contents...')
# target.truncate()

print('Now I\'m going to ask you for three lines.')
line1 = input('Line 1: ')
line2 = input('Line 2: ')
line3 = input('Line 3: ')

print(f'I\'m going to write these to the file.')
target.write(f'''{line1}\n
            {line2}\n
            {line3}''')

print('And, finally, I\'ll close it.')
target.close()