#!python3

import shutil
from pathlib import Path
import os,sys,shelve
from datetime import datetime,date,timedelta

##Testing area
##print(f'The number of system arguments given is {len(sys.argv)}') #-Working as intended
##print(f'type of today is {type(today)}')
##print(f'sys.argvs parsed are {sys.argv}') #-Working as intended

##Declaration and initialization of variables
#bdays = {'Me':'10 February 2000'} #-TO BE DELETED -- Initial test case
shelfFile = shelve.open('birthdays')
bdays = shelfFile['bdays']
today = date.today()
currentYear = today.year
nextYear = currentYear + 1

def getDate(name):
    '''Gets the birthday of a certain person and returns it as a string in the format %d/%m'''
    return bdays[name].strftime("%d/%m")

##TODO: if no arguments is passed, list the next upcoming birthday
def dayDifference(name):
    '''Finds the difference between bday and today and returns the number of days to the next birthday'''
    birthdate = getDate(name)
    this_yr_bday = birthdate + '/' + str(currentYear)
    next_yr_bday = birthdate + '/' + str(nextYear)

    bday1 = datetime.strptime(this_yr_bday,'%d/%m/%Y').date()
    bday2 = datetime.strptime(next_yr_bday,'%d/%m/%Y').date()

    if bday1 > today:
        difference = (bday1-today).days
    else:
        difference = (bday2-today).days

    ##print(f'There are {difference} more days to {name}\'s birthday')
    return difference

##Test cases
##NIL

if len(sys.argv) == 1:
    least = None
    list_of_names = []
    for name in bdays:
        diff = dayDifference(name)
        if least == None:
            least = diff
        elif diff < least:
            least = diff

    for name in bdays:
        diff = dayDifference(name)
        if diff == least:
            list_of_names.append(name)
    str_of_names = ''
    for name in list_of_names:
        str_of_names += name + ','

    print(f'Next birthday is {str_of_names} in {least} days')

##TODO: if 'bday upcoming' is parsed, list all birthdays within the next 60 days
if len(sys.argv) == 2 and sys.argv[1].lower() == 'upcoming':
    print('Checking upcoming birthdays...')
    for name in bdays:
        diff = dayDifference(name)
        if diff <= 60:
            print(f'{name}\'s birthday is in {diff} days')

##TODO: if 'bday upcoming (number)' is parsed, list all birthdays within the next (number) of days
if len(sys.argv) == 3 and sys.argv[1].lower() == 'upcoming':
    print('Checking upcoming birthdays...')
    for name in bdays:
        diff = dayDifference(name)
        if diff <= int(sys.argv[2]):
            print(f'{name}\'s birthday is in {diff} days')

##TODO: if 'ls' is parsed, list bdays
if len(sys.argv) == 2 and sys.argv[1].lower() == 'ls':
    print('Listing birthdays...')
    for key in bdays:
        print(f'{key} - {bdays[key].strftime("%d %B %Y")}')

##TODO: if 'add' is parsed, add the next two arguments as name and birthday (check for error handing as well)
if len(sys.argv) == 4 and sys.argv[1].lower() == 'add':
    print(f'Adding birthday of {sys.argv[2]} as {sys.argv[3]}')
    bdays[sys.argv[2]] = datetime.strptime(sys.argv[3],'%d/%m/%Y')
    print("Birthday added. Type 'bday ls' to find list of updated birthdays")

##TODO: if 'del' is parsed, add the next two arguments as name and birthday (check for error handing as well)
if len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
    print(f'Deleting birthday of {sys.argv[2]}')
    bdays.pop(sys.argv[2])
    print("Birthday deleted. Type 'bday ls' to find list of updated birthdays")

##TODO: if 'plan' is parsed with no arguments behind, plan the next available birthday. Else, check if the next argument matches a name in the lists and plan for that birthday instead. To plan, copy a template file and add it into a folder of sorts.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'plan':
    name = sys.argv[2]
    bday = date.today() + timedelta(days = dayDifference(name))
    #print(f'bday of said man iz {bday}') #-Working as intended
    cwd = str(Path.cwd())
    #print(f'Current working directory is {cwd}') #-Working as intended
    filename = str(name)+str(bday.strftime('%Y'))
    shutil.copyfile(f'{cwd}/template.md',f'{cwd}/{filename}.md')

shelfFile['bdays'] = bdays
shelfFile.close

