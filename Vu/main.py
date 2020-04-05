import json 
import hashlib

jsonFileName = 'dictionary.json'
inputFileName = 'input.txt'
fileName = 'syllables.txt'

# Get number of words, ONE WORD EACH LINE ONLY
def getNumOfWords(fileName):
    numOfWordDict = 0  
    with open(fileName,'r',encoding = 'utf-8') as file: 
        listmyDict = file.readlines() 
        numOfWordDict = len(listmyDict)
    return numOfWordDict

numOfWordDict = getNumOfWords(fileName)
numOfInputWord = getNumOfWords(inputFileName)

with open(jsonFileName,encoding='utf-8') as f:
    myDict = json.loads(f.read())
# print(len(myDict.keys()))
# print(type(myDict)) # Return dict

# def checkExistKey(myDict, key): 
#     if key in myDict.keys(): 
#         return True
#     else: 
#         return False

inputFile = open(inputFileName,encoding = 'utf-8')
readInputFile = inputFile.readlines()

countExists = 0 
# TODO: Faster way to iterate 
for idx,word in enumerate(readInputFile): 
    encodeWord = hashlib.md5(word.upper().encode()).hexdigest()[:3:]
    # TODO: Add try catch to prevent error get from input
    # Check if key exists
    # TODO: Further optimize here
    try:
        for ele in myDict[encodeWord]: 
            # TODO: Change variable stripN to something understandable 
            stripN = word.upper().rstrip("\n")
            if ele == stripN: 
                countExists = countExists + 1
    except: 
        continue
    
print('Số từ trong input', numOfInputWord)
print('Số từ xuất hiện trong input tìm thấy trong dictionary', countExists)
print('Tỉ lệ số từ xuất hiện trong được tìm thấy trong dictionary ', 
        round(((countExists/numOfInputWord)*100),2))