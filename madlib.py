#! python3
""" Make a fun little mad-lib for you.
    Usage: madlib.py <filename> - Load mad-lib with specified filename. """


import os
import sys


os.chdir('C:\\Users\\stevend\\Documents\\Python Scripts\\Mad-Libs')


# madlib_file = open(str('.\\' + sys.argv[1] + '.txt') ,'r')
madlib_file = open('.\\nantucket.txt')
madlib = madlib_file.read()
madlib_file.close()
print('\nMad-Lib Text: ' + madlib)

