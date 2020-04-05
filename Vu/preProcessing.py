# --------------------------PRE-PROCESSING---------------------------------
# This program exports dictionary datatype to dictionary.json 
# HOW THIS WORKS? 
#   -> Hash by md5 
#   -> KEY = Take 3 first letter receive from md5 hash
#   -> VALUE = word.encode().toMD5Hashing [this line is pseudo code]
#---------------------------------------------------------------------------

# --------------------------SETTING PARAMETER-----------------------------
# If you want to use different list of word to create different dictionary 
# CHANGE FILE NAME HERE
fileName = 'syllables.txt' # Change list of words

# CHANGE NUMBER OF BUCKET FOR HASHTABLE HERE
numOfBuckets = 3 # Change value of numOfBuckets to create smaller 
                  # of buckets for hashtable
#---------------------------------------------------------------------------

# NOTICED: 
#   - File dictionary.json MUST BE EXISTED before run this program
#   - ONLY NEED TO COMPILE THIS FILE TO GET dicionary.json

import hashlib
from collections import OrderedDict 
import json

import time
start_time = time.time()

# Create hash key
    # TODO: Remember to change mode to 'a' 
    # So that next time function won't rewrite 
hashList = []
with open(fileName,mode = 'r',encoding= 'utf-8') as file: 
    rawFileInput = file.readlines() 
    for line in rawFileInput: 
        line = hashlib.md5(line.encode()).hexdigest()[:numOfBuckets:]
        hashList.append(line)

def removeDuplicate(inputList): 
    return list(OrderedDict.fromkeys(inputList))

removeDuplicate(hashList)

def fillKeyOnly(listOfKey,myDict):
    myDict = {key: [] for key in listOfKey} 
    return myDict 

def fillValueOnly(listOfValue,myDict): 
    for value in listOfValue: 
        hashValue = hashlib.md5(value.encode()).hexdigest()[:3:]
        #TODO: Add try catch here to prevent error
        myDict[hashValue].append(value.rstrip("\n")) 
    return myDict
myDict = {}
myDict = fillKeyOnly(hashList,myDict)
myDict = fillValueOnly(rawFileInput,myDict)

# Export to dictionary to *.json
# 'dictionary.json' MUST EXISTED
with open('dictionary.json','w',encoding= 'utf-8') as dictJson: 
    json.dump(myDict,dictJson, ensure_ascii = False, indent = None)
del hashList

print("Thời gian thực hiện pre-processing %s" % round((time.time() - start_time),2))

# Un-use function
# def checkDuplicate(self):
#     countDuplicate = 0
#     for elem in self.listOfKey: 
#         if self.listOfKey.count(elem) > 1:
#             countDuplicate = countDuplicate + 1 
#     if countDuplicate == 0: 
#         return 0
#     else: 
#         return countDuplicate     