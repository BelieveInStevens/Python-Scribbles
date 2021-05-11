#! python3
# bulletpointAdder.py - Adds Wikipedia bullet points to the start of each line
# of text on the clipboard.
import sys, pyperclip

old_text = pyperclip.paste()

lines = old_text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

new_text = '\n'.join(lines)

pyperclip.copy(new_text)