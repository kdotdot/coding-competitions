import re
from decimal import *

fi=open("wordcount.txt", "r")
finput=open("submitInput.txt", "r")
fo=open("output.txt","w+")

f1 = fi.readlines()

def getUnicodeValue(word):
    res = '0.'
    for w in word:
        res+=str(ord(w)).zfill(3)
    check =['candideces','candidez']
    if word in check:
        print(res)
    return 1-Decimal(res)



ranking = dict()
for line in f1:
    word,count = line.split()
    count = int(count)
    ranking[word] = count
ranking = {k: v for k, v in sorted(ranking.items(), key=lambda item: (item[1],getUnicodeValue(item[0])), reverse=True)}

for key in ranking:
    if ranking[key]==4:
        #print(key)
        pass

f2 = finput.readlines()
f2.pop(0)
for i,line in enumerate(f2):
    line = line.rstrip()
    if re.match("[0-9]+",line):
        #es numero
        n = int(line)-1
        word = list(ranking.keys())[n]
        fo.write("Case #{}: {} {}\n".format(i+1,word,ranking[word]))
    else:
        #es palabra
        n = list(ranking.keys()).index(line)
        fo.write("Case #{}: {} #{}\n".format(i+1,ranking[line],n+1))


