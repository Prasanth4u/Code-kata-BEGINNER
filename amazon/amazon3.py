"""
3
CHENNAI
MUMBAI
DELHI
2
CHENNAI MUMBAI
DELHI CHENNAI

"""

#program
cityNames=[]
routeNames=[]
revRoutes=[]
#n no.of cities
nCity=int(input())
#n city names
for i in range(0,nCity):
    eleCityNames=str(input())
    cityNames.append(eleCityNames)
#n no.of routes
nRoutes=int(input())
#2 column
C=2
#n routes names
for i in range(nRoutes):
    a =[]
    a=list(map(str,input().strip().split(" ")))[:nRoutes]
    #a.append(str(input()))
    routeNames.append(a)

routeNamesCopy=routeNames

for i in range(len(routeNamesCopy)):
    routeNamesCopy.append(routeNames[i].reverse())

print("routeNames:::::")
for r in routeNames:
    print(r)
    
print("routeNamesRev:::::")
for r in routeNamesCopy:
    print(r)

    
