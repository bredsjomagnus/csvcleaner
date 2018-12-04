import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore, Back, Style
from colorama import init
init(autoreset=True)

import math
import sys

# list over allowed filetypes
allowedfiletypes = ['mylaps', 'hardcard']

# setting up mylaps header and datatypes
mylapsheadertitles = ['#', 'no', 'name', 'laps', 'lead', 'lap_time', 'speed', 'elapsed_time', 'passing_time', 'hits', 'strength', 'noice', 'photocell_time', 'transponder', 'backup_tx', 'backup_passing_time', 'class', 'deleted']
mylapsheaderdatatypes = [int, int, str, int, int, str, float, str, str, int, int, int, str, int, int, str, str, str]
mylaps = zip(mylapsheadertitles, mylapsheaderdatatypes)

# setting up hardcard header and datatypes
hardcardheadertitles = ['tagid', 'frequency', 'signalstrength', 'antenna', 'time', 'datetime', 'hits', 'competitorid', 'competitionnumber', 'firstname', 'lastname', 'lap_time', 'deleted']
hardcardheaderdatatypes = ['str', 'str', 'int', 'float', 'float', 'int', 'str', 'str', 'int', 'int', 'int', 'str', 'str', 'time', 'str']
hardcard = zip(hardcardheadertitles, hardcardheaderdatatypes)

# dictionary with inforamtion of allowed filetypes
allowedheaders = {'mylaps': mylaps, 'hardcard': hardcard}

# colors example from colorama; https://pypi.org/project/colorama/
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

# get arguments: list
args = sys.argv

if len(args) < 4:
    print("Wrong number of arguments: [file to load, file to save, filetype]")
    sys.exit(0)

# Begin
print("\nREADY!\n")

# filename
filename = args[1]

# savename on converted file
savename = args[2]

# type of file [mylaps or hardcard]
filetype = args[3]

print("Processing '%s' file '%s'" % (filetype, filename))
if filetype not in allowedfiletypes:
    print("Not allowed filetype. Needs to be set to 'mylaps' or 'hardcard'")
    print("\nEnding process. sys.exit(0)\n")
    sys.exit(0)

# read csv: DataFrame file
file = pd.read_csv(filename)

# get header: List header
header = list(file.columns)

# header to lowercase
header = list(map(lambda el: el.lower(), header))

print("\n"+Style.BRIGHT + Fore.LIGHTCYAN_EX+"********** FIXING HEADERS **********")

# index of chosen filetype
try:
    filetypeindex = allowedfiletypes.index(filetype)
except:
    print("Index error. sys.exit(0)")
    sys.exit(0)


# header template title and datatype
headertemplate = zip(*list(allowedheaders[allowedfiletypes[filetypeindex]]))
headertemplate = list(headertemplate)
headertemplate_title = headertemplate[0]
headertemplate_datatype = headertemplate[1]



# check list lengths
if len(header) != len(headertemplate_title):
    print("Header length not correlating to template '%s'." % (filetype))
    print("Check if '%s' is correct filetype for '%s'" % (filetype, filename))
    print("\nEnding process. sys.exit(0)\n")
    sys.exit(0)

# print("Header template '%s':\n%s\n" % (filetype, headertemplate_title))

# check if header needs correction
if len(set(header) & set(headertemplate_title)) < len(header):
    print("%s out of %s titles need correction" % (len(header) - len(set(header) & set(headertemplate_title)), len(header)))

    counter = 1
    for index, title in enumerate(header, 0): 
        if header[index] != headertemplate_title[index]:
            print("\t"+str(counter)+". header["+ str(index)+"]: "+Style.BRIGHT+Fore.RED+"'"+str(header[index])+"'"+Style.RESET_ALL+" \n\t\t set to -> "+Style.BRIGHT+Fore.GREEN+"'"+ str(headertemplate_title[index])+"'")
            counter += 1
    
    file.columns = headertemplate_title

    print("\n"+Style.BRIGHT + Fore.LIGHTCYAN_EX+"********** FIXING DATATYPES **********")
    print("Removing non numerical values.")
    print("Setting " + Fore.CYAN + " 'NaN' " + Fore.WHITE + "to -1.")
    print("Converting to int64 for columns: [ ", end = '')
    columns = ""

    for columnindex, column in enumerate(file):
        # c pandas Series. A column from dataframe
        # c = file.loc[:,column]

        # print(type(file[column]))

        

        if headertemplate_datatype[columnindex] == int:
            """ converting to int64 
                1. Remove non numeric values with to_numeric
                2. Fill NaN with int -1
                3. Convert rest of column to int
            """
            print(Style.BRIGHT+Fore.GREEN + column + " ", end ='')

            file[column] = pd.to_numeric(file[column], errors='coerce')
            file[column] = file[column].fillna(-1).astype(int)
            file[column] = file[column].astype(int)
    print("]")    
print("\n"+Style.BRIGHT+Fore.GREEN +"SUCCESS!\n")

# write dataframe to csv
file.to_csv(savename, index=False)

print("Saved to '" + str(savename) + "'")
print()