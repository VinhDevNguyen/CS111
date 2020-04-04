import json 
import hashlib

jsonFileName = 'dictionary.json'
inputFileName = 'input.txt'
fileName = 'syllables.txt'

# Get number of words, ONE WORD EACH LINE ONLY
def getNumOfWords(fileName):
    numOfWordDict = 0  
    with open(fileName,'r',encoding = 'utf-8') as file: 
        listData = file.readlines() 
        numOfWordDict = len(listData)
    return numOfWordDict

numOfWordDict = getNumOfWords(fileName)

with open(jsonFileName,encoding='utf-8') as f:
    data = json.loads(f.read())
# print(len(data.keys()))
# print(type(data)) # Return dict

inputFile = open(inputFileName,encoding = 'utf-8')
readInputFile = inputFile.readlines()

countExists = 0 

for idx,word in enumerate(readInputFile): 
    encodeWord = hashlib.md5(word.upper().encode()).hexdigest()[:3:]
    print(data.get(encodeWord,word,True))
    if idx == 5: break