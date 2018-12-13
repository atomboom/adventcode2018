import numpy as np
#import puzzle input


filename='data'
file=open(filename,mode='r')
data = file.read().splitlines()

data=list(map(str,data)) #data to string. list

instr=[]
alph=[chr(i) for i in range(ord('A'),ord('Z')+1)]
for i in range(len(data)):
    instr.append([data[i][5],data[i][-12]])


#find start
i=0
occ_right=[0]*27
for letter in alph:
    for k in range(len(instr)):
        if instr[k][1]==letter:
            occ_right[i] +=1
    i +=1

id_start=occ_right.index(0)

#function to check possibilites based on ready letters
def check_pos(done_list,instr):
    pos_list=[]
    rem_list=[]


    for i in range(len(done_list)):
        for k in range(len(instr)):
            if done_list[i]==instr[k][0]:
                if instr[k][1] not in pos_list and instr[k][1] not in done_list:
                    pos_list.append(instr[k][1])


    pos_list.sort()

    for i in range(len(pos_list)):
        for k in range(len(instr)):
            if pos_list[i]==instr[k][1]:
                if instr[k][0] not in done_list:
                    if i not in rem_list:
                        rem_list.append(i)

    rem_list.sort(reverse=True)
    for i in rem_list:
        pos_list.pop(i)

    pos_list.sort()


    return pos_list


#run logic
ex_order=[alph[id_start]]
go=1
while go==1:
    pos_list=check_pos(ex_order, instr)

    if pos_list==-1 or pos_list==[]:
        go=0
        break

    ex_order.append(pos_list[0])

#create solution key
str=''
for i in range(len(ex_order)):
    str=str+ex_order[i]

print('Solution 1',str)


workers=5
base_time=60
work_idle=workers
pos_list=[alph[id_start],'Z','Q','R','A']
t=0
work=[]
go=1
done_list=[]
recheck=1
rem_list=[]
while go==1:
    if recheck==1:
        rem_list=[]
        pos_list=check_pos(done_list, instr)
        for i in range(len(pos_list)):
            for j in range(len(work)):
                if pos_list[i]==work[j][2]:
                    rem_list.append(i)
        rem_list.sort(reverse=True)

        for i in rem_list:
            pos_list.pop(i)
        recheck=0


    if t==0:
        pos_list=alph[id_start]

    while work_idle>0 and pos_list != [] and pos_list != -1:

        t_st=t
        work_idle -= 1
        work_time=alph.index(pos_list[0])+base_time
        t_fin=t+work_time
        work.append([t_fin,t_st,pos_list[0]])
        work.sort(key=lambda x: x[0])

        print('START:',[t_fin,t_st,pos_list[0]],'@',t)
        if len(pos_list)==1:
            pos_list=[]
        else:
            pos_list.pop(0)


    while work!=[] and t>=work[0][0] :
        work_idle += 1
        done_list.append(work[0][2])
        recheck=1

        print('DONE',work[0],'@',t)
        sol=work[0][0]+1
        if len(work)==1:
            work=[]
        else:
            work.pop(0)

    t=t+1

    if t>500000:
        break


print(sol)

instr.sort(key=lambda x: x[0])
#for i in range(len(instr)):
   # print(instr[i])



