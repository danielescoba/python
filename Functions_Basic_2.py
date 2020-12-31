#Countdown
def Countdown(x):
    while x >= 0:
        print (x)
        x=x-1
#Print and Return
def Print_and_Return(li):
    print(li[0])
    return li[1]
print(Print_and_Return([1,2]))
#First Plus Length
def firstPluslength(li):
    return li[0] + len(li)
print(firstPluslength([5,2,3,4,5]))
#Values Greater than Second
def valuesGreaterThanSecond(li):
    x=0
    newlist=[]
    if len(li)<=1:
        return False
    else:
        while x<len(li):
            if li[x] > li[1]:
                newlist.append(li[x])
                x=x+1
            else:
                x=x+1
    return newlist
print (valuesGreaterThanSecond([5,2,1,3,4]))
print(valuesGreaterThanSecond([1]))
#This Lenght, That Value
def thisLenghtThatValue(a,b):
    c=0
    newlist=[]
    while c < a :
        newlist.append(b)
        c=1+c
    return newlist
print(thisLenghtThatValue(3,4))
print(thisLenghtThatValue(6,2))
