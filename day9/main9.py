import numpy as np
#import puzzle input


filename='data'
file=open(filename,mode='r')
data = file.read()

data=list(map(str,data)) #data to string. list




players=430
point=71588


order=[0,1]
act=1
placed=[0,1]
i=0
points=[0]*(players+1)
curr_player=1
to_place=1
while True:
    curr_player +=1
    to_place+= 1
    if curr_player > players:
        curr_player = 1

    if to_place%23==0:
        act += - 7
        if act<0:
            act += len(order)
        points[curr_player] += to_place + order[act]

        order.pop(act)

    else:
        place_id=act+2

        if place_id>len(order):
            place_id=place_id%len(order)

        order.insert(place_id,to_place)
        act=place_id



    # if len(placed)%1000 ==0:
    #     print(max(points))
    #
    #     print(len(placed),'|',point)
    #print(curr_player,'|',order)
    if to_place >= point :
        break


print(points.index(max(points)),max(points),17+2*23)

print(type(points[0]))
print(type(to_place))
print(point)
print(len(order)+252)
print(point/23)
print((23*250+1)%23)



