# --------------------------SETTING PARAMETER-----------------------------
jsonFileName = 'dictionary.json' # Change import dictionary file
inputFileName = 'input.txt'# User input file use to comparision 
fileName = 'syllables.txt' # file to create dictionary
#---------------------------------------------------------------------------

import json 
import hashlib
import time
start_time = time.time()
# Get number of words, ONE WORD EACH LINE ONLY
def getNumOfWords(fileName):
    numOfWordDict = 0  
    with open(fileName,'r',encoding = 'utf-8') as file: 
        listmyDict = file.readlines() 
        numOfWordDict = len(listmyDict)
    return numOfWordDict

# Get number of words from dic and input file
numOfWordDict = getNumOfWords(fileName)
numOfInputWord = getNumOfWords(inputFileName)

# Read dictionary from *.json
with open(jsonFileName,encoding='utf-8') as f:
    myDict = json.loads(f.read())

# Read input file (bao2.txt or input.txt)
inputFile = open(inputFileName,encoding = 'utf-8')
readInputFile = inputFile.readlines()

# Comparision between bao2.txt (input.txt) and dictionary.json
countExists = 0 
for idx,word in enumerate(readInputFile): 
    encodeWord = hashlib.md5(word.upper().encode()).hexdigest()[:3:]
    # Prevent error from non-exist key in dictionary
    try:
        for ele in myDict[encodeWord]: 
            wordStripN = word.upper().rstrip("\n")
            if ele == wordStripN: 
                countExists = countExists + 1
    except: 
        continue

del readInputFile

print('Số từ có trong input', numOfInputWord)
print('Số từ xuất hiện trong input tìm thấy trong dictionary', countExists)
print('Tỉ lệ số từ xuất hiện trong được tìm thấy trong dictionary ', 
        round(((countExists/numOfInputWord)*100),2))

print("Thời gian thực hiện pre-processing %s" % round((time.time() - start_time),2))
