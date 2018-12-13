import numpy as np
#import puzzle input


filename='data'
file=open(filename,mode='r')
data = file.read()

data=list(map(int,data.split(' '))) #data to string. list



go=1
header=[]

child_count=[]
meta_count=[]
i=0
meta_dat=[]
result=[]
ID=[]
child_list=[]
ID_log=[]
while go==1:

    if i>2:
        if child_count == [] and i > 2:
            child_count = [-1]
        if meta_count == [] and i > 2:
            meta_count = [-1]
        if child_count[0]+meta_count[0]==-2:
            go=0
            break

    if i==0:
        header.append([data[0],data[1]])
        child_count.append(header[0][0])
        meta_count.append(header[0][1])
        meta_dat.append([])
        ID.append(0)
        ID_log.append(0)
        i=2

    if child_count[-1]>0:
        child_count[-1] += -1
        header.append([data[i],data[i+1]])
        child_count.append(header[-1][0])
        meta_count.append(header[-1][1])
        meta_dat.append([])
        ID_log.append(ID_log[-1]+1)
        ID.append(ID_log[-1])
        child_list.append([ID[-2],ID_log[-1]])
        i=i+2

    if child_count[-1]==0:
        meta_data=data[i:i+meta_count[-1]]

        children=[]
        for k in range(len(child_list)):
            if child_list[k][0]==ID[-1]:
                children.append(child_list[k][1])


        result.append([ID[-1],header[-1],meta_data,children])
        i=i+meta_count[-1]
        meta_count.pop(-1)
        child_count.pop(-1)
        ID.pop(-1)
        header.pop(-1)


#meta sum
meta_sum=0
for i in range(len(result)):
    meta_sum += sum(result[i][2])


score=[0]*len(result)
i=0
evaluated=[]

for i in range(len(result)):

    #points to no child nodes
    if result[i][1][0]==0: #if no child
        score[result[i][0]]=sum(result[i][2]) #score= meta
        evaluated.append(result[i][0])

i=0
evaluated.sort()
all( dep in evaluated for dep in result[3][3])
print('checker',all( dep in evaluated for dep in result[3][3]))
print(score[7])
j=0


while True:
    if i>len(result):
        i=0

    if result[i][0] not in evaluated:

        if all( dep in evaluated for dep in result[i][3]):

            for k in range(len(result[i][2])):

                if result[i][2][k]!=0 and result[i][2][k]<=result[i][1][0]:
                    score[result[i][0]] += score[result[i][3][result[i][2][k]-1]]

            evaluated.append(result[i][0])



    i=i+1
    if len(evaluated)==len(result):
        break




meta_sum=0
score_sum=0

for i in range(len(result)):
    meta_sum += sum(result[i][2])
    score_sum+=score[i]


print('meta sum',meta_sum)
print('score main node',score[0])
