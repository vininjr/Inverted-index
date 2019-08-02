import os

def read_docs(path):
	docs_list = os.listdir(path)
	list_docs = []
	for D in docs_list:
		list_docs.append(path + D)
	return list_docs	

def tratar_consulta(qPath):
    aQuery = ''
    relevantNum = 0
    flag = 0
    relevants = list()
    odd = 1
    wholeDoc = readFile(qPath)
    wholeDoc = wholeDoc.split('\n')
    for doc in wholeDoc: 
        for desc in doc.split(' '):
            
            if desc == 'QU':
                flag = 1
                continue
            if desc == 'NR':
                flag = 2
                continue
            if desc == 'RD':
                flag = 3
                continue

            if(flag == 1):   
                aQuery+=desc+' '
            elif(flag == 2): 
                relevantNum = int(desc)
            elif(flag == 3):
                if(desc != ''):
                    if(odd): 
                        relevants.append(desc)
                    odd = not odd
    
    return(aQuery, relevantNum, relevants)

def readFile(path):
    file = open(path, 'r+')
    a = file.read()
    file.close()
    return a

def isEmpty(x):
    return len(x) == 0