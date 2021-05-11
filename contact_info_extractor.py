#! python3
# contact_info_extractor.py - A program for taking text copied from the clipboard 
# and extracting e-mail addresses and phone numbers from it.

import sys, pyperclip, re

email_regex = re.compile(r'''
# Rules for the Local portion of the address (john.smythe, blndassassn, etc.)                   
(?P<localgroup>
    ([^<>()\[\]\.,;:\s@\"]+ 
    (\.[^<>()\[\]\.,;:\s@\"]+)*)    
    # The local address may contain any character with the exception of those
    # in the group above, and those characters may be separated by periods.
|   (\".+\")                      
    # Or, if someone surrounds their entire local address with double quotes,
    # they can use whatever characters they want.
)   
# End of the local address rules          
                                
@                               
# The "@" symbol

# Rules for the domain portion of the address (gmail.com, hotmail.com, etc.)
(?P<domaingroup>                   
    ([^<>()\[\]\.,;:\s@\"]+\.)+     
    # May contain any character save for the preceding.
    [^<>()[\]\.,;:\s@\"]{2,}       
    # The top-level domain (com, org, co.uk, etc.) 
)                
# End of the rules for the domain group
''',              
re.VERBOSE)

phone_number_regex = re.compile(r'''
(
    \(?
    (?P<areacode>\d{3})?
    [-\)\s.]*?
)?
(?P<phonenumber>
    \d{3}
    [-\)\s.]*?
    \d{4}
)
(
    \s*
    (ext|ext.|x)
    \s*
    (?P<extension>(\d){2,5})
)?
'''
, re.VERBOSE)

# message = pyperclip.copy()