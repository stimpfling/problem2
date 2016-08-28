# Super cool (read: hacky) way to assign values to each char of the alphabet
# However access should be linear since the keys are one char long. 
Alphabet = 'abcdefghijklmnopqrstuvwxyz'
Score = 1
ScoreDict = {}
for c in Alphabet:
    ScoreDict[c] = Score
    Score += 1

class nameObj:
    def __init__(self, name, score):
        self.name  = name
        self.score = score
        self.lchild = None
        self.rchild = None

#This is a fun function that adds the names and their scores to a bTree for fast inserting
def insert(node, nameobj):
    count = 0
    tmpScore = nameobj.score
    
    # If they have the same score, figure out the tie-breaker
    if nameobj.score == node.score:
        # If the names are exactly the same, make a decision 
        if node.name.lower() == nameobj.name.lower():
            tmpScore += -1
        else:
            # Check each char in the name for a possible tie-breaker
            for char in nameobj.name:
                if ScoreDict[char.lower()] > ScoreDict[node.name[count].lower()]:
                    tmpScore += 1
                    break
                elif ScoreDict[char.lower()] < ScoreDict[node.name[count].lower()]:
                    tmpScore += -1
                    break
                count += 1
    # Now you can do the simple btree insert based on the calculated score
    if tmpScore > node.score:
        if node.lchild == None:
            node.lchild = nameobj
        else:
            insert(node.lchild, nameobj)
    else:
        if node.rchild == None:
            node.rchild = nameobj
        else:
            insert(node.rchild, nameobj)

# Flatten bTree into an array and lose the score metadata
def convertNameTree(node,array):
    if(node == None):
        return
    if node.lchild != None:
        convertNameTree(node.lchild,array)
    array.append(node.name)
    if node.rchild != None:
        convertNameTree(node.rchild,array)

    
def answer(names):  
    nameTree = None;
    array = []
    for name in names:
        nameScore = 0 
        for char in name:
            nameScore += ScoreDict[char.lower()]
        tempObj = nameObj(name, nameScore)
        if nameTree != None:
            insert(nameTree, tempObj)
        else:
            nameTree = tempObj
    convertNameTree(nameTree,array)
    return array

print answer(["","bae","BAE","MeiIsBae"])
print answer(["","bae","BAE"])
print answer(["ab"])
print answer(["AL","CJ"])
print answer(["annie","bonnie","liz"])
print answer(["vi","abcdefg"])




