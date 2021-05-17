#! python3
# mcb.pyw - Saves and loads multiple pieces of text.
# Usage: py.exe mcb.pyw save <keyword> - Save keyword to clipboard.
#        py.exe mcb.pyw <keyword> - Load keyword from clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw del <keyword> - Remove keyword from clipboard.
#        py.exe mcb.pyw del-all - Removes all keywords from clipboard.


import pyperclip
import shelve
import sys


mcb_shelf = shelve.open('mcb')

# Save the clipboard content
if len(sys.argv) == 3:

    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()

    elif sys.argv[1] == 'del':
        mcb_shelf.pop(str(sys.argv[2]))

elif len(sys.argv) == 2:

    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))

    elif sys.argv[1] == 'del-all':
        mcb_shelf.clear()
        
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])

else:
    pyperclip.copy('AHHHHHHHH!')


mcb_shelf.close()