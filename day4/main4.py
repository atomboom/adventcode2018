import numpy as np

#import puzzle input
filename='data'
file=open(filename,mode='r')
data = file.read().splitlines()

data=list(map(str,data)) #data to string. list

#format [*year*-*mont*-*day* *hour*:*minute*]

#sort
go=1
i=0

log=[]
tup_list=[]


for i in range(len(data)):
    str=data[i]

    tup=(str[1:5],str[6:8],str[9:11],str[12:14],str[15:17],str[19:])
    tup_list.append(tup)

def n2(elem): #month
    return elem[1]
def n3(elem): #day
    return elem[2]
def n4(elem): #hour
    return elem[3]
def n5(elem): #minute
    return elem[4]

sort_list=tup_list

sort_list=sorted(sort_list, key=n5)
sort_list=sorted(sort_list, key=n4)
sort_list=sorted(sort_list, key=n3)
sort_list=sorted(sort_list, key=n2)

tup=[]
clock=np.zeros((5000,61))
for i in range(len(sort_list)):
    str=sort_list[i]
    Y=str[0]
    M=str[1]
    D=str[2]
    h=str[3]
    m=str[4]
    comm=str[5]
    if comm[0]=='G':
        curr_guard = comm[comm.find('#') + 1:comm.find(' b')]
        tup.append((Y,M,D,h,m,curr_guard,'B'))
    if comm[0]=='w':
        tup.append((Y, M, D, h, m, curr_guard, 'W'))
    if comm[0] == 'f':
        tup.append((Y, M, D, h, m, curr_guard, 'S'))

for i in range(len(tup)):
    curr=tup[i]
    if curr[6]=='B':
        curr_guard=int(curr[5])

    if curr[6]=='W':
        T_w=int(curr[4])
        clock[curr_guard,T_s:T_w] +=1

    if curr[6] == 'S':
        T_s=int(curr[4])



tot_log=[]

for i in range(len(clock)):
    tot_sl=sum(clock[i,:])
    g_id=i
    tot_log.append((g_id,tot_sl))


mem=0
for i in range(len(tot_log)):
    if tot_log[i][1]>mem:
        mem=tot_log[i][1]
        guard=tot_log[i][0]

time=list(map(int,clock[guard,:]))

mem=0
for i in range(len(time)):
    if mem<time[i]:
        mem=time[i]
        min=i


print('max sleepy at:',min)
print('by guard:',guard)
print('çhecksum',guard*min)

mem=0
guard=[]

for i in range(5000):
    for k in range(60):
        if mem<clock[i,k+1]:
            mem=clock[i,k+1]
            guard=i


time=list(map(int,clock[guard,:]))


for i in range(len(time)):
    if mem==time[i]:
        mem=time[i]
        min=i

print(min,'by',guard)
print('checksum',guard*min)