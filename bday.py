#!python3

import os,sys,shelve
from datetime import datetime
import time

##Testing area
print(f'The number of system arguments given is {len(sys.argv)}')

##Declaration and initialization of variables
shelfFile = shelve.open('birthdays')
bdays = {'Me':'10 February 2000'}

##TODO: if no arguments is passed, list the next upcoming birthday

##TODO: if 'ls' is parsed, list bdays

##TODO: if 'add' is parsed, add the next two arguments as name and birthday (check for error handing as well)
if len(sys.argv) == 4 and sys.argv[1].lower() == 'add':
    print(f'Adding birthday of {sys.argv[2]} as {sys.argv[3]}')
    bdays[sys.argv[2]] = datetime.strptime(sys.argv[3],'%d/%m/%Y')
    print("Birthday added. Type 'bday ls' to find list of updated birthdays")

##TODO: if 'del' is parsed, add the next two arguments as name and birthday (check for error handing as well)
if len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
    print(f'Deleting birthday of {sys.argv[2]}')
    bdays.pop('sys.argv[2]')
    print("Birthday deleted. Type 'bday ls' to find list of updated birthdays")

##TODO: if 'plan' is parsed with no arguments behind, plan the next available birthday. Else, check if the next argument matches a name in the lists and plan for that birthday instead. To plan, copy a template file and add it into a folder of sorts.

shelfFile['bdays'] = bdays
shelfFile.close

