# Algorithm ideas 
# Description: 
#   - Base on tree structure 
#   - Alphabet order: Each branch categorize by alphabet (24 branches) (layer 1)
#        + In each branch, categorized by A, Á, Â,... (layer 2)
#        + And after that, categorized by length (layer 3 -> word_max_length)       
#   - After tree is initialized, export to  *.json files
#   - Next time after running, only need update *.json files (Used DictImporter from Anytree)
#   - 
#  Program functionality: 
#    - Benchmark performance between algorithm (brute-force?) 
#    - count occupants from list appeard in dictionary 
# Input restriction: 
#    - Does not support lowercase
#    - To solve this, str.upper()/lower().encode('utf-8')
#    - Check encode https://www.utf8-chartable.de/ 
#    - Ex: á = c3 a1; à = c3 a0; b
from anytree import RenderTree,Node
import numpy as np #Efficient library to iterate through <list>



def main(): 
    file = open('syllables.txt',encoding = 'utf8',errors ='ignore')
    # file.seek('int position') # move back/forward pointer to position 
    # file.tell() # tell current pointer 
    # import os
    # fileSize = file.seek(0,os.SEEK_END)
    root = Node('root')
    strUTF = file.readlines()
    for idx,data in enumerate(strUTF): 
        print(data)
        if idx == 5: break



if __name__ == "__main__":
    main()









