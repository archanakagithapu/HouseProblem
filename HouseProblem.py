'''There are n houses build in a line ,each of which contains some value in it.
A thief is going to steal the maximal value of these houses,but he can't steal
in 2 adjacent houses because the owner of the stolen houses will tell his 2
neighbours left and right side------> what is the maximum stolen value'''

house=list(map(int,input().split()))
eMax=sum(house[0::2])
oMax=sum(house[1::2])
tMax=0
while(max(house)!=0):
    tMax+=max(house)
    i=house.index(max(house))
    if i==0:
        house[0],house[1]=0,0
    elif i==len(house)-1:
        house[-2],house[-1]=0,0
    else:
        house[i],house[i+1],house[i-1]=0,0,0
print(max([oMax,eMax,tMax]))


    
    
