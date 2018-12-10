#imort packages


#import puzzle input
filename='data'
file=open(filename,mode='r')

data = file.read().splitlines()

data=list(map(int,data)) #data to int. list

#build empty lists
hist=[0]
log_pos=[0]
log_neg=[0]
for i in range(1000000):
    hist.append(0)
    log_pos.append(0)
    log_neg.append(0)

#set initial frequentie
freq=0

#build single pass
for i in range(len(data)):
    freq=freq+data[i]
    hist[i+1]=freq

print('awnser 1=',freq)

#run pass until log entry is double

go=1
k=0
i=0
freq=0

while go==1:
    if k>=len(data):
        k=0

    freq=freq+data[k]
    hist[i+1]=freq

    if freq>=0:
        log_pos[freq]=log_pos[freq]+1
    else:
        log_neg[-freq] = log_neg[-freq] + 1

    k=k+1
    i=i+1

    if log_neg[abs(freq)]==2 or log_pos[abs(freq)]==2:
        print('awnser 2=',freq)
        go=0
