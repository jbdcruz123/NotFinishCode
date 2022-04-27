#retype ni Ron Medrano
class node:
    def __init__(self, numberP, nodeP = None):
        global head; global tail
        self.number = numberP
        self.next = nodeP
        print(f"node __init__")
class linkList:
    def __init__(self, nodeP = None):
        global head; global tail; global tailCount
        tailCount = 0
        head = nodeP
        tail = head
        print(f"linkList  __init__")
    def fAdd(self, nodeP: node):
        global head; global tail; global tailCount
        if head.next == None:
            head.next = nodeP
            tail = nodeP
        else:
            tail.next = nodeP
            tail = nodeP
        tailCount +=1
        print(f"\n\nTagumpay na nai-add ang value na {nodeP.number}\npress kahit ano...   ",end="")
        input()
    def fDisplay(self):
        global head; global tail; global tailCount
        print(f"\n\nDisplay\n")
        countI = 0
        i = head.next
        while i != None:
            print(f"[ {countI}, {i.number} ] -> ", end="")
            i = i.next
            countI+=1
        print(f"total count {tailCount}\npress kahit na ano... ",end = "")
        input()
    def fDelete(self, countP):
        global head; global tail; global tailCount
        countI = 0
        backI = head
        i = head.next              
        while i != None:
            if countI == countP:
                backI.next = i.next
                if countP == (tailCount-1):
                    tail = backI
                tailCount-=1
                print(f"\n\nTagumpay  na na delete ang index {countP}\npress kahit ano...   ",end="")
                input()
                return
            backI = i
            i = i.next
            countI +=1
        print(f"Hindi nakita ang i-dedelete na {countP}\npress kahit ano... ", end ="")
        input()               
head = None; tail = None; tailCount =None
inputN = node(0)
linkO = linkList(inputN)
while 1:
    print(f"\n\n**********\nq quit, a add, p display, d delete\n**********\n\ninput command:   ", end= "")
    inputV = input()
    
    if inputV == "q":
        print(f"pa-exit na...   ", end="")
        input()
        break
    elif inputV == "a":
        print(f"\n\ninput data sa add:   ", end="")
        inputV = input()
        inputN = node(int(inputV))
        linkO.fAdd(inputN)
        
    elif inputV == "p":
        linkO.fDisplay()
        
    elif inputV == "d":
        print(f"\n\ninput index para delete:   ", end="")
        inputV = input()
        linkO.fDelete(int(inputV))
        
        
        
    
    
    
    
