class node:
    def __init__(self, numberP, nodeP = None):
        global head; global tail
        print("node init")
        self.numberD = numberP
        self.next = nodeP
        
#ayaw dumaan sa init ng linkList        
class linkList:
    def __init___(self, nodeLink = None):
        global head; global tail 
        
        print("loob ng link init")
        head = nodeLink
        tail = head
head = None; tail = None
inputN = node(1)
linkO = linkList(inputN)

