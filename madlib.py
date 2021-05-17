#! python3
""" Make a fun little mad-lib for you.
    Usage: madlib.py <filename> - Load mad-lib with specified filename. """


import os
import re
import sys


madlib_path = 'C:\\Users\\stevend\\Documents\\Python Scripts\\Mad-Libs'
madlib_file = open(str(madlib_path + sys.argv[1] + '.txt') ,'r')
madlib = madlib_file.read()
madlib_file.close()
print('\nMad-Lib Text: ' + madlib)

speech_parts_regex = re.compile('NOUN|ADJECTIVE|VERB|ADVERB')
speech_parts_match = speech_parts_regex.findall(madlib)
madlib_text = re.sub(speech_parts_regex, '%s', madlib)
madlib_replacements = tuple(map(lambda x: input('Please enter a ' + x + ':'), 
    speech_parts_match))
madlib_return = madlib_text % madlib_replacements


print(madlib_return)  
