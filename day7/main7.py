import numpy as np

#import puzzle input
filename='data'
file=open(filename,mode='r')
data = file.read().splitlines()

data=list(map(str,data)) #data to string. list

#formtat
# #ID, @POS, :SIZE
ID=[]
POSx=[]
POSy=[]
SIZEx=[]
SIZEy=[]

for i in range(len(data)):
    str=data[i]
    ID.append(int(str[1:str.find('@')-1]))
    POSx.append(int(str[str.find('@') + 1:str.find(',')]))
    POSy.append(int(str[str.find(',')+1:str.find(':')]))
    SIZEx.append(int(str[str.find(':')+2:str.find('x')]))
    SIZEy.append(int(str[str.find('x')+1:]))

print(len(data),len(SIZEy))
map=np.zeros((1000,1000))
map[2:5,2]=1

for i in range(len(data)):
    map[POSx[i]:POSx[i]+SIZEx[i],POSy[i]:POSy[i]+SIZEy[i]] +=1


print('awnser 1',sum(sum(map>1)))

