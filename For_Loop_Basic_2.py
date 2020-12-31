#Biggie Size
def BiggieSize(li):
    newlist=[]
    for x in range(0,len(li),1):
        if li[x] > 0 :
            newlist.append("big")
        else:
            newlist.append(li[x])
    return newlist
print(BiggieSize([-1, 3, 5, -5]))
#Count Positives
def countPositives(li):
    count=0
    for x in range(0,len(li),1):
        if li[x] > 0 :
            count= count + 1
    li.pop()
    li.append(count)
    return li
print(countPositives([-1,1,1,1]))
#Sum Total
def sumTotal(li):
    sum=0
    for x in range(0,len(li),1):
        sum=sum+li[x]
    return sum
# print(sumTotal([1,2,3,4]))
#Average
def Average(li):
    sum = sumTotal(li)
    return sum/len(li)
# print(Average([1,2,3,4]))
#Lenght
def Length(li):
    return len(li)
# print(Lenght([1,2,3,4,5,6,7,8]))
#min
def min(li):
    
    if len(li) == 0:
        return False
    else:
        min=li[0]
        for x in range(0,len(li),1):
            if min > li[x]:
                min = li[x]
    return min
# print(min([37,2,1,-9]))
#Maximum
def max(li):
    
    if len(li) == 0:
        return False
    else:
        max=li[0]
        for x in range(0,len(li),1):
            if max < li[x]:
                max = li[x]
    return max
# print(max([1,5,3,423,425,3]))
#Ultimate Analysis
def ultAnalysis(li):
    newdic={'sumTotal': sumTotal(li),'average': Average(li), 'minimum':min(li),'maximum':max(li),'length':Length(li)}
    return newdic
print (ultAnalysis([1,2,3,4]))
#Reverse List
import math
def revList(li):
    temp=0
    middle= math.floor(len(li)/2)
    x=0
    for x in range (0,middle,1):
        temp=li[x]
        li[x]= li[len(li)-x-1]
        li[len(li)-x-1] = temp
    return li

print (revList([1,2,3,4,5]))
