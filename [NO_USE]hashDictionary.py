# New approach 
# Maybe similar ideas to tree but this one use hastable 
# So that hashtable 
# import sys 
# reload(sys) 
# sys.setdefaultencoding('UTF8')

# Hash by length after encode it to uft-8
class HashTable(object): 
    def __init__(self,length):
        self.array = [None*length]
    
    def hash(self,key): 
        length = len(self.array)
        return hash(key) % length 
    
    def add(self,key,value): 
        index = self.hash(key)
        if self.array[index] is not None: 
            for iterKey in self.array[index]: 
                if iterKey == key: 
                    iterKey


def main(): 
    file = open('syllables.txt',mode = 'r',encoding= 'utf-8')
    listFromFile = file.readlines()





if __name__ == "__main__":
    main()

