import os

def readFile(input):
    #read file and return sorted
    f = open(input, "r")
    numbers = f.read().split()
    f.close()
    numbers = sorted(numbers)
    return numbers

def readOps(input):
    #read all the operations from file
    f = open(input, "r")
    ops = f.read().split()
    f.close()
    return ops

def search(tgt, data):
    #search function
    try:
        loc = data.index(tgt) #location within data
        return True, loc
    except:
        return False
    
def insert(input, data):
    #insert number and sort
    data.append(input)
    data = sorted(data)
    return data
    
def delete(tgt, data):
    #delete all occurences of the target data
    data = list(filter(lambda x: x != tgt, data)) ##https://stackoverflow.com/questions/1157106/remove-all-occurrences-of-a-value-from-a-list
    return(data)
    
def exeOps(ops, data):
    #loop through operations and execute each case
    for i in range(1,len(ops),2):
        opp = int(ops[i-1])
        num = ops[i]
        match opp:
            case 1:
                print(search(num, data))
            case 2:
                data = insert(num, data)
                print("INSERTED")
            case 3:
                data = delete(num, data)
                print("DELETED")
            case _:
                print("error - no opperation with", opp)
    return(data)

cwd = os.getcwd()
numbers = readFile(cwd+"/CW-T2/task1_2_numbers.txt")
ops = readOps(cwd+"/CW-T2/task1_2_operations.txt")
output = (exeOps(ops, numbers))