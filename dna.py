from sys import argv, exit
import csv
import re

# if argv not equal to 3 print error
if len(argv) !=3:
    print("Try again.")
    exit(1)

# naming argvs
database = argv[1]
sequence = argv[2]
# opening database
with open(database, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        database_list = list(reader)
# opening sequences
with open(sequence, 'r') as txtfile:
        sequence_list = txtfile.readline().rstrip("\n")
string = sequence_list
# https://stackoverflow.com/questions/61131768/how-to-count-consecutive-substring-in-a-string-in-python-3 :
AGATC  = 0
pattern = "AGATC"
while pattern in string:
    AGATC += 1
    pattern += "AGATC"

TTTTTTCT  = 0
pattern = "TTTTTTCT"
while pattern in string:
    TTTTTTCT += 1
    pattern += "TTTTTTCT"

AATG  = 0
pattern = "AATG"
while pattern in string:
    AATG += 1
    pattern += "AATG"

TCTAG = 0
pattern = "TCTAG"
while pattern in string:
    TCTAG += 1
    pattern += "TCTAG"

GATA = 0
pattern = "GATA"
while pattern in string:
    GATA += 1
    pattern += "GATA"


TATC = 0
pattern = "TATC"
while pattern in string:
    TATC += 1
    pattern += "TATC"

GAAA = 0
pattern = "GAAA"
while pattern in string:
    GAAA += 1
    pattern += "GAAA"


TCTG = 0
pattern = "TCTG"
while pattern in string:
    TCTG += 1
    pattern += "TCTG"

for row in database_list:
# comparing databases with sequences
    if argv[1] == "databases/large.csv":
        for row in database_list:
            if int(row['AGATC']) == AGATC and int(row['TTTTTTCT']) == TTTTTTCT and int(row['AATG']) == AATG and int(row['TCTAG']) == TCTAG and int(row['GATA']) == GATA and int(row['TATC']) == TATC and int(row['GAAA']) == GAAA and int(row['TCTG']) == TCTG:
                print(row['name'])
                exit(0)
if argv[1] == "databases/small.csv":
        for row in database_list:
            if int(row['AGATC']) == AGATC and int(row['AATG']) == AATG and int(row['TATC']) == TATC:
                print(row['name'])
                exit(0)
print("No match")