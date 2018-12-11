import numpy as np

#import puzzle input
filename='data'
file=open(filename,mode='r')
data = file.read().splitlines()

data=list(map(str,data)) #data to string. list
str=list(data[0])
go=1
i=0
k=0
init=len(str)
count=0



while go==1:
    if i>=len(str)-1 or i<0:
        if k==0 and i>0:
            go=0
        i = 0
        k=0

    if str[i].lower()==str[i+1].lower() and str[i]!=str[i+1]:
        del(str[i:i+2])
        k=k+1
        i=i-10
        print(i,'/',len(str),'/',init)

    i=i+1

print(len(str))