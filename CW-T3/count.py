import os, multiprocessing as mp
import time

def readNames(input):
    #txt to python
    input = open(input, "r")
    names = input.read().split()
    input.close()
    return(names)

def readText(input):
    #txt to python
    input = open(input, "r")
    text = input.read()
    input.close()
    return(text)

def writeText(outText):
    #python to txt
    outFile = cwd+"/CW-T3/output.txt"
    output = open(outFile, 'w')
    output.write(outText)
    output.close

def searchNames(name, text):
    #count the names
    count = text.count(name)
    return(name, str(count))

if __name__ == "__main__":
    start = time.time() 
    #create pool (*number of theads*)
    pool = mp.Pool()   #https://docs.python.org/3/library/multiprocessing.html
                        #https://towardsdatascience.com/parallelization-in-python-the-easy-way-aa03ed04c209
                        #https://www.machinelearningplus.com/python/parallel-processing-python/
    
    cwd = os.getcwd()
    names = readNames(cwd+"/CW-T3/task1_3_names.txt")
    text = readText(cwd+"/CW-T3/task1_3_text.txt")

    #add task to pool
    results = [pool.apply(searchNames, args=(name, text)) for name in names]
    pool.close()
    
    ##FOR COMPARISON
    
    #results = []
    #for name in names:
        #hi = searchNames(name, text)
        #results.append(hi)
        
    writeValues = ''
    
    for result in results:
        print(' '.join(result))
        writeValues += str(result[0] + " : " + result[1])+'\n'
    
    writeText(writeValues)
        
    end = time.time()
    print(end - start)
    
#CORES FOR EACH PERSON
#0.13667607307434082
#0.12579083442687988
#0.12723088264465332