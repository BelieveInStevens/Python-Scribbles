#! python3


import os
import re



# file generation

# filenamez = ['Martinique', 'Reversi', 'Bridge', 'Hearts', 'Mao']
datez_folder = r'C:\Users\stevend\Documents\Python Scripts\Datez'
datez_subfolders = []
for subfolder in os.listdir(datez_folder):
    datez_subfolders.append(''.join([datez_folder, '\\', subfolder]))

# for folder in os.listdir(datez_folder):
#     if folder[0:3] == 'Mar':
#         month = "03"
#     elif folder[0:3] == 'Apr':
#         month = "04"
#     else:
#         month = "05"
#     for filename in filenamez:
#         file_path = ''.join([datez_folder, '\\', folder, '\\', filename,
#             ' - 10-', month, '-2021.txt']).strip()
#         file = open(file_path, 'w')
#         file.write('VERY IMPORTANT BUSINESS DATA')
#         file.close()


date_regex = re.compile(r'''
    (?P<day>[0-9]{1,2})-
    (?P<month>[0-9]{1,2})-
    (?P<year>[0-9]{2,4})
''',
re.VERBOSE)


# Testing that the date regex works the way I want it to.
# test_datez = ['10-04-2021', '28-05-2021', '18-03-2021', '5-1-21']
# for date in test_datez:
#     print(re.sub(date_regex, '\g<year>-\g<month>-\g<day>', date))

for folder in (datez_subfolders):
    for filename in os.listdir(folder):
        old_name = ''.join([folder, '\\', filename])
        new_name = ''.join([folder, '\\', re.sub(date_regex, 
                    '\g<year>-\g<month>-\g<day>', filename)])
        os.rename(old_name, new_name)



