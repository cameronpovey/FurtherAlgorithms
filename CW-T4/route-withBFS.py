import csv
import time

import time
start = time.time()

csvFile = "CW-T4/task1_4_railway_network.csv"
displayStations = []
routes = {}

def findTravel(routes, start, end):
    pathCost = 0
    costs = {start: pathCost}
    visited = [start]
    paths = {start: [start]}
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        
        for station, nextCost in routes[node].items():
            pathCost = costs[node] + nextCost #update cost of path
            
            if station not in visited or pathCost < costs[station]: #if not visited or cheaper than best
                    
                visited.append(station)
                costs[station] = pathCost
                paths[station] = paths[node] + [station]
                
                if station not in queue:
                    queue.append(station)
                    
    if end not in paths:
        return "NOT FOUND"
    else:
        return(paths[end], costs[end])

# READABLE OUTPUT
file = open(csvFile, newline='')
reader = csv.reader(file)
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

#BRISTOL TO THURSO #long
#0.007873058319091797
#0.006751060485839844
#0.0078008174896240234

#PENZANCE TO LONDON #medium
#0.008661031723022461 
#0.008332014083862305
#0.009160995483398438

#BRISTOL TO LONDON #short
#0.007301807403564453
#0.007301807403564453
#0.007301807403564453