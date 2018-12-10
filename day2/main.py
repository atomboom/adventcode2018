import numpy as np

#import puzzle input
filename='data'
file=open(filename,mode='r')
data = file.read().splitlines()

data=list(map(str,data)) #data to string. list


count=[0] #init count

#build empty count vector
for i in range(len(data[0])-2):
    count.append(0)

#set counters to 0
i=0
count2=0
count3=0

#itterate through data
while go==1:
    try:
        str=data[i] #select string

        for k in range(len(str)-1): #for eachletter in string
            count[k]=str.count(str[k]) #count occurans
        if count.count(2)>0: #count how many are 2
            count2=count2+1
        if count.count(3)>0: #count how many are 3
            count3=count3+1

        i=i+1 #set step
    except:
        go=0 #stop system


print('checksum=',count2*count3) #print result