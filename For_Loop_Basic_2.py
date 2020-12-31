for x in range(1,151): print(x)
for x in range(5,1001):
    if x%5 == 0 :
        print (x)
for x in range(1,101):
    if x%10==0: print ("Coding Dojo")
    elif x%5==0: print ("Coding")
    else: print(x)
y=0
for x in range(0,500001):
    if x%2==1:
        y=x+y
print(y)
z=2018
while z > 0:
    print(z)
    z=z-4
lowNum=2
highNum=9
mult=3
for lowNum in range (lowNum,highNum+1):
    if lowNum%mult==0:
        print (lowNum)