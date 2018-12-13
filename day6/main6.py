import numpy as np
import string

def dist_2d (point1,point2):
    return abs(point1[0]-point2[0])+abs((point1[1]-point2[1]))

#import puzzle input
filename='data'
file=open(filename,mode='r')
data = file.read().splitlines()

data=list(map(str,data)) #data to string. list

#create vector list
vec_list=[]
for i in range(len(data)):
    vec=data[i]
    vecx=int(vec[:vec.find(',')])
    vecy=int(vec[vec.find(',')+2:])
    vec_list.append([vecx,vecy])

#find miximum values
maxx=0
minx=10**6
miny=10**6
maxy=0
for i in range(len(vec_list)):
    if maxx<vec_list[i][0]:
        maxx=vec_list[i][0]
    if minx>vec_list[i][0]:
        minx=vec_list[i][0]
    if maxy<vec_list[i][1]:
        maxy=vec_list[i][1]
    if miny > vec_list[i][1]:
        miny = vec_list[i][1]


upper=max([maxx,maxy])
lower=0



field=[]
inf_id_list=[]

x_range=range(lower,upper)
y_range=range(lower,upper)
map=[]
inf_list=[]
if 0==1:
    for cor_x in x_range:
        for cor_y in y_range:
            dist_list=[]
            id=-1

            for i in range(len(vec_list)):
                dist_list.append(dist_2d([cor_x,cor_y],vec_list[i]))

            min_dist=min(dist_list)

            if dist_list.count(min_dist) == 1:
                id=dist_list.index(min_dist)
                map.append([cor_x, cor_y, id])
            else:
                id=-1
                # if cor_x >= max(x_range)-5 or cor_x <= min(x_range)+5 or cor_y >= max(y_range)-5 or cor_y <= min(y_range)+5:
                #     for k in range(len(dist_list)):
                #         if dist_list[k]==min_dist:
                #             id=k
                #             if id not in inf_list:
                #                 inf_list.append(id)
                #                 print('SPECIAL inf basterd @', cor_x, cor_y, len(inf_list), id)


            if cor_x==max(x_range) or cor_x==min(x_range) or cor_y==max(y_range) or cor_y==min(y_range):
                if id not in inf_list:
                    inf_list.append(id)
                    print('inf basterd @',cor_x,cor_y,len(inf_list),id)

    surf=[0]*1000
    for i in range(len(map)):
        id=map[i][2]
        if id not in inf_list:
            surf[id] = surf[id]+1

    print(surf)
    print(max(surf),'by',surf.index(max(surf)))
    print('rejects:',inf_list,'|L=',len(inf_list))

pos_sum=[]
for cor_x in x_range:
    for cor_y in y_range:
        dist_list = []
        id = -1

        for i in range(len(vec_list)):
            dist_list.append(dist_2d([cor_x, cor_y], vec_list[i]))
        pos_sum.append([cor_x,cor_y,sum(dist_list)])
print(pos_sum[100:200])

count=0
for i in range(len(pos_sum)):
    if pos_sum[i][2]<10000:
        count +=1

print(count)