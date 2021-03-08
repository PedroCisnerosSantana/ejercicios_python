!#/usr/bin/python3
import csv
import json

f = open("ejemplo.txt", "r")
f.read()
f.read(4)
f.tell()
f.readline()
f.readlines()
f.close()

fcsv = open("ejemplo.csv")
content = csv.reader(fcsv)
list(content)
fcsv.close()

data = '{"name":"pedro","years":19}'
dataLoad = json.loads(data)
