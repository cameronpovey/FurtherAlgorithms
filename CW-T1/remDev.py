import os

def remDev(inFile, outFile):
    #read file put in dict
    inFile = open(inFile, "r")
    numbers = inFile.read().split()
    inFile.close()
    
    dupes = {}
    output = {}
    
    #get list of duplicate numbers
    for i, number in enumerate(numbers): 
        if number not in dupes:
            #if not duplication add to list to check other numbers
            dupes[number] = [i]
        else:
            #if is duplication add position into dict
            dupes[number].append(i)
            
    print(dupes)
            
    for key, position in dupes.items():
        Vcount = len(position)
        if Vcount>1:
            #if even
            if Vcount%2 == 0:
                middle = int((Vcount/2)) #+1 for right -1 for array
            else:
                middle = int((Vcount/2)-0.5) #+ 0.5 for rounding and - 1 for array
            output[key] = position[middle]
        else:
            output[key] = position[0]
            #del dupes[key]
            
    sortedOutput = {k:v for k, v in sorted(output.items(), key=lambda item:item[1])} ##https://realpython.com/sort-python-dictionary/
    writeValues=(" ".join(str(key) for key in sortedOutput.keys())) 
    
    with open(outFile, 'w') as output:
        output.write(writeValues)
    
cwd = os.getcwd()
remDev(cwd+"/CW-T1/task1_1_numbers.txt",cwd+"/CW-T1/output.txt")