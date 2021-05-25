#! python3


from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f'Copying from {from_file} to {to_file}...')
in_file = open(from_file)
indata = in_file.read()

print(f'This file is {len(indata)} bytes long!')

print(f'Does the output file exist? {exists(to_file)}')
input("Ready? Press ENTER to continue, Ctrl+C to abort.")

out_file = open(to_file, 'w')
out_file.write(indata)

print('Alright! I\'m done here!')

out_file.close()
in_file.close()
