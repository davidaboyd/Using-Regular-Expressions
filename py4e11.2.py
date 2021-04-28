#This project tests knowledge of Regular expressions
#This is for information purposes ONLY!!
#http://py4e-data.dr-chuck.net/regex_sum_1180527.txt

import re
name=input("Enter file name")
if len(name) < 1 : name = "regex_sum_1180527.txt:"
handle=open('regex_sum_1180527.txt')
lst=list()

for line in handle:
    line=line.rstrip()
    fndall=re.findall('[0-9]+',line)
    lst+=fndall
sum=0
for k in lst:
    sum+=int(k)

    #findalll=int(fndall)
    #total=sum(fndall)
print(sum)
