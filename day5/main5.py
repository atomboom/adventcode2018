import numpy as np
import string


def mutate(str_in):
    go=1
    i=0
    k=0

    while go==1:
        if i >= len(str_in) - 1 or i < 0: #if i out of bounds, reset i
            if k == 0 and i > 0:#stop loop if no deletion
                go = 0

            #reset counters
            i = 0
            k = 0

        if str_in[i].lower() == str_in[i + 1].lower() and str_in[i] != str_in[i + 1]:#if same letter but diffrent cap.
            del (str_in[i:i + 2])
            k = k + 1
            i = i - 10
        i=i+1
    return len(str_in)


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


awnser_1=mutate(str)
print('awnser 1=',awnser_1)


alph=list(string.ascii_lowercase[:26])
str=list(data[0])
result=[]

for letter in alph:
    target=list(data[0])
    target=list(filter(lambda x: x != letter, target))
    target = list(filter(lambda x: x != letter.upper(), target))

    val=mutate(target)
    result.append(val)
    #print(letter,'|',val)

print('awnser 2=',min(result),'@',alph[result.index(min(result))])

