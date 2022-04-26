class node:
    def __init__(self, numberP, nodeP = None):
        global head; global tail;
        print("node init")
        self.numberD = numberP
        self.next = nodeP
        
#ayaw dumaan sa init ng linkList        
class linkList:
    def __init___(self, nodeLink = None):
        global head; global tail; 
        
        print("loob ng link init")
        head = nodeLink
        tail = head

    def fAdd(self, nodeP):
        global head; global tail
    
        if head.next == None:
            head.next = nodeP
            tail = nodeP
            tail.next = None
        else:
            tail.next = nodeP
            tail = nodeP
            tail.next = None
        
    def fDisplay(self):
        global head; global tail
    
        print("\n\nDisplay:   ")
        DisplayI = 0
        i = head.next
        while i != None:
            print(f"[{DisplayI} {i.numberD} ] -> ",end="")    
            DisplayI+=1
            i = i.next

    def fDelete(self, inputP):
        global head; global tail
        notSeen = 1
        backI = head
        i = head.next    
        while i != None:
            if i.numberD == inputP:
                notSeen = 0
                backI.next = i.next 
                break   
            backI = i
            i = i.next
    
        if notSeen == 1:
            print(f"wlang nakitang value na {inputP}")
        
        
    def fInsert(self, indexP, insertN):
        global head; global tail

        countI = 0
        backI = head
        i = head.next
        while i != None:
            if indexP == countI:
                backI.next = insertN
                backI.next.next = i
                break

            backI = i
            i = i.next

#global control        
head = None; tail = None 

nodeLink = node(0)

linkListO = linkList(nodeLink) 

while 1:
    print(f"\n\n*****\nq quit,a d p i\n*****")
    inputV = input()
    if inputV =="q":
        print(f"\n\nexiting...  ", end = "")
        inputV = input()
        break
    elif inputV == "a":
        print(f"\n\ninput add data:  ", end = "")
        inputV = input()
        inputNode = node(int(inputV))
        linkListO.fAdd(inputNode)
        
    elif inputV == "p":
        linkListO.fDisplay()
        
    elif inputV == "d":
        print(f"\n\ninput data to delete:  ", end = "")
        inputV = input()
        fDelete(int(inputV))
    
    elif inputV == "i":
        print(f"\n\ninput index to insert:  ", end = "")
        inputV = input()
        print(f"\n\ninput data to insert:  ", end = "")
        inputSecondV = input()
        inputNode = node(int (inputSecondV)) 
        fInsert(int(inputV), inputNode)
        
    else:
        print("\n\nmali ang pindot mo na {inputV}\nala ito sa menu...", end="")        
        input()


