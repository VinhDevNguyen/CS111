# Algorithm ideas 
# Description: 
#   - Base on tree structure 
#   - Alphabet order: Each branch categorize by alphabet (24 branches) (layer 1)
#        + In each branch, categorized by A, Á, Â,... (layer 2)
#        + And after that, categorized by length (layer 3 -> word_max_length)       
#   - After tree is initialized,
# Program functionality: 
#    - Benchmark performance between algorithm (brute-force?) 
#    - count occupants from list appeard in dictionary 

import codecs #encode utf-8

# HOW TO USE class Tree

class Tree(object):
    #Constructor
    def __init__(self, name='root', children=None):
        self.name = name # Name will be data itself
        self.children = [] #by index, left will always be children[0] 
        if children is not None:
            for child in children:
                self.add_child(child)

    # return obj representation, MUST RETURN STRING
    def __repr__(self):
        return self.name
    
    def add_child(self, node):
        # assert isinstance(node, Tree) #Check added child is valid (should be tree obj)
        self.children.append(node)

# def initializedTree(dictionary):

# def traversalTree(tree): 

def main(): 
    # f = codecs.open("syllables.txt",encoding = "utf-8")
    # for i in range(5): print(f.readline()) 
    t = Tree('root',
            [
                Tree('1'),
                Tree('2'),
                Tree(['3'])
            ]
    )
    t.add_child(Tree('4'))
    print(t.children[3])









if __name__ == "__main__":
    main()









