import os, multiprocessing as mp
import time

def readNames(input):
    #txt to python
    input = open(input, "r")
    names = input.read().split()
    input.close()
    return(names)

def readText(input, threads):
    #txt to python
    reText = []
    input = open(input, "r")
    text = input.read()
    input.close()
    perT = int(len(text)/threads)
    for i in range(threads):
        reText.append(text[(i)*perT:((i)*perT)+perT])
    return(reText)

def writeText(outText):
    #python to txt
    outFile = cwd+"/CW-T3/output.txt"
    output = open(outFile, 'w')
    output.write(outText)
    output.close

def searchNames(names, text):
    #count the names
    count={}
    for name in names:
        count[name] = text.count(name)
    return count
        

if __name__ == "__main__":
    start = time.time() 
    threads = 4         #create pool (*number of theads*)
    pool = mp.Pool(threads)   #https://docs.python.org/3/library/multiprocessing.html
                        #https://towardsdatascience.com/parallelization-in-python-the-easy-way-aa03ed04c209
                        #https://www.machinelearningplus.com/python/parallel-processing-python/
    
    cwd = os.getcwd()
    names = readNames(cwd+"/CW-T3/task1_3_names.txt")
    text = readText(cwd+"/CW-T3/task1_3_text.txt", threads)
    print(len(text))
    #add task to pool
    results = [pool.apply(searchNames, args=(names, text[i])) for i in range(threads)]
    pool.close()
    writeValues = ''
    
    #set names dict to 0
    ovrcount = {name: 0 for name in names}
    
    #add results to ovrcount of names
    for i in range(threads):
        for name in names:
            ovrcount[name] += results[i][name]
    
    #create output dict
    writeValues = ''
    for name in names:
        writeValues += (name + "   :  " + str(ovrcount[name]) + "\n")
    
    writeText(writeValues)
        
    
    writeText(writeValues)
        
    end = time.time()
    print(end - start)
    
#CORES FOR WHOLE TEXT
#0.08019781112670898
#0.08150506019592285
#0.07891321182250977
