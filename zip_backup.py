#! python3
# zip_backup.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.


import os
import zipfile


def zip_backup(folder):
    # Backup the entire contents of 'folder' into a ZIP file.

    folder = os.path.abspath(folder) # make sure the folder path is absolute.

    # Figure out the filename this code should use based on what files
    # already exist.
    number = 1
    while True:
        zip_file_name = os.path.basename(folder) + ' ' + str(number) + '.zip'
        if not os.path.exists(zip_file_name):
            break
        number +=1
    
    # Creating the ZIP file
    print(f'Creating {zip_file_name}...')
    backup_zip = zipfile.ZipFile(zip_file_name, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, _, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP file.
        backup_zip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            new_base = os.path.basename(folder) + ' '
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue # Don't backup ZIP files
            backup_zip.write(os.path.join(foldername, filename))
    backup_zip.close()
    print('Done.')

zip_backup('C:\\Users\\stevend\\Documents\\Python Scripts')

    