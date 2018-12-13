import numpy as np
#import puzzle input


filename='data'
file=open(filename,mode='r')
data = file.read()

data=list(map(str,data.split())) #data to string. list

header=[]

for i in range(len(data)):
    if len(data[i])==2:
        header.append(data[i][0:2])

checksum=0
for i in range(len(header)):
    metacount=int(header[i][1])
    checksum += metacount

print(checksum)


