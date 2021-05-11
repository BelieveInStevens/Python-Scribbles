print('Please enter your name:')
name = input()
print('Please enter your password:')
password = input()
if name == 'Mary':
    print('Hello Mary')
    if password == 'swordfish':
        print('Access Granted. Welcome, ' + name + '.')
    else:
        print('Access Denied. You''re in the wrong fucking neighborhood, ' + name + '!')
