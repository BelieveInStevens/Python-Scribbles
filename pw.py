#! python3
# password_locker.py - An insecure password locker program.

import sys, pyperclip

passwords = {
    'e-mail': 'AlwaysSometimesEMails',
    'blog': 'BobLoblawsLawBlog',
    'luggage': '12345'
}

if len(sys.argv) < 2:
    print('Usage: python password_locker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] 
# first command line argument is the account name we are retrieving a password for.

if account in passwords.keys():
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('The ' + account + ' account does not exist in the password locker.')