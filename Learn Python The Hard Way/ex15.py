#! python3


from sys import argv


script, filename = argv
txt = open(filename, 'r')

print(f'Here\'s your file: {filename}')
print(txt.read())
txt.close()

file_again = input(f'Type the filename again:  ')
txt_again = open(file_again, 'r')
print(txt_again.read())
txt_again.close()