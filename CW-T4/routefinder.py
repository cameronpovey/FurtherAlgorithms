import csv
import time

import time
start = time.time()

csvFile = "CW-T4/task1_4_railway_network.csv"
displayStations = []
routes = {}

def findTravel(routes, start, end):
    costs = {node: 9999 for node in routes}
    costs[start] = 0
    
    visited = set()
    
    #keep track of visited station
    prev = {}
    for station in routes:
        prev[station] = None
    
    while visited != set(routes.keys()):
        #get cheapest next station
        currNode = min([node for node in costs if node not in visited], key=costs.get)
        
        if currNode == end: break
                
        visited.add(currNode) #visited node
        for station, cost in routes[currNode].items():
            newCost = costs[currNode] + int(cost)
            if station not in visited or newCost < costs[station]:
                costs[station] = newCost
                prev[station] = currNode
                
    path = [end]
    node = end
    while prev[node] != None:
        path.append(prev[node])
        node = prev[node]
    path.reverse()
        
    return(path, costs[end])

#READABLE OUTPUT
file = open(csvFile, newline='')
reader = csv.reader(file)
print (reader)
for row in reader:
    dep_station = row[0].strip().upper()
    dest_station = row[1].strip().upper()
    cost = int(row[2])
    
    if dep_station not in routes:
        routes[dep_station] = {}
    if dest_station not in routes:
        routes[dest_station] = {}
        
    routes[dep_station][dest_station] = cost
    routes[dest_station][dep_station] = cost
    
    displayStations.append(row[0])
    displayStations.append(row[1])
    
displayStations = [x.upper() for x in sorted(list(set(displayStations)))]

print("NUMBER OF STATIONS: ")
print(len(displayStations),"/520")

#comment for testing
dep = input("Enter departing station: ")
dest = input("Enter destination: ")

#uncomment for testing different settings
##TESTING - long
#dep = "BRISTOL TEMPLE MEADS"
#dest = "THURSO"

##TESTING2 - med
#dep = "PENZANCE"
#dest = "LONDON"

##TESTING3 - short
#dep = "BRISTOL PARKWAY"
#dest = "LONDON"

dep = dep.strip().upper()
dest = dest.strip().upper()
if dep not in displayStations or dest not in displayStations:
    print("STATION NOT FOUND")
    exit()
    
path, cost = findTravel(routes, dep, dest)
print(path, cost)

end = time.time()
print(end - start)


###BEFORE FIX### using list --------------
#BRISTOL TO THURSO #long
#0.29260802268981934
#0.28790879249572754
#0.28838396072387695

#PENZANCE TO LONDON #medium
#0.04954886436462402
#0.048548221588134766
#0.049102067947387695

#BRISTOL TO LONDON #short
#0.01887798309326172
#0.016264915466308594
#0.0165407657623291


###AFTER FIX### using set --------------
#BRISTOL TO THURSO #long
#0.01983785629272461
#0.01983785629272461
#0.01983785629272461

#PENZANCE TO LONDON #medium
#0.00703120231628418
#0.0071370601654052734
#0.007174968719482422

#BRISTOL TO LONDON #short
#0.004931211471557617
#0.0048389434814453125
#0.004686117172241211