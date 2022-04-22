# date 4/22/2022 7:55pm
#linkedlist using array method, with stndby(for deleted adress)   
#not finish, fix the output alignment

#COMMENT ang program na ito ay linkedlist gamit ang galawan ng array imbis na
#pointer to adress
#ex: P->next, P->data   is   node[0] = next adress, data[0] = data

#node ang hahawak sa adress at next adress( maaring random ang adress gaya ng pointer adress makikita nalng sa mga code)
#ang -1 ay null, ang -2 ay new data ginawa kong -2 para mamonitor ng user ang bagong append sa node

#data ang hahawak sa data katugon ito ng node(pede siguro itong isang array nalang sa next kung
#test gamit ang 2 dimension array of list ex: nodeData[adress][nextAdress, data, extension para sa ibang data pa]

#head ito ang inital adress na susundan hanggang makarating ng end ung tail

#stndby ito ang storage para sa na idelete na adress at kung mag addnew ang node
#dito kukuha ng adress, para wlang masayang at para mabilis ang memory at kaunti lang ng memory
#ng array ng node at data ang magagamit

#stndbyL ito ang humahawak ng length ng stndby, pabawas ito ng pabawas habang nag aadnew ang node,pero pag 
#nag delete ay padag-dag ito ng pa dagdag

def fAdd(inpV):#1A
    global head; global tail; global node; global data; global stndby; global stndbyL
       
    if node[head] == -1:
        #initialize ung bagong head at tail
        rtrnL = fGetStndby()    
        tail = rtrnL
        #head and tail ay parehas
        node[tail]=-1 #null
        data[tail] = inpV
        node[head] = tail
        print(f"\ntagumpay na nai-add si {inpV}\npress any key...  ", end="") 
        input()
        return 
                
    #[tail] = added, tail =added, tail =-1
    rtrnL = fGetStndby()    
    node[tail] = rtrnL
    tail = rtrnL
    node[tail]= -1
    data[tail] = inpV
      
    #add new  
    print(f"\ntagumpay na nai-add si {inpV}\npress any key...  ", end="") 
    input()
#1A

#display
def fDspl():#1B

    global head; global tail; global node; global data
    
    if node[head] == -1:
        print(f"\n\nwala i-Didisplay wla na kasing laman")
        input("Pres any key...")
        return 
        
    print("\n\nDATA: depende sa pagkasunod sunod ng input\n")
    i = node[head]
    while i != -1: #2
        #kasma ang adress at data sa isang braket
        #print(f"[{node[i]} , {data[i]}]", end="")
        #solo value ang display sunod sunod
        print(f"{data[i]} ", end="")
        i = node[i]
    #2
    print("\n\n")  
    input("press any key...")
#1B

#delete
def fDlt(inpV): #1C
    
    global head; global tail; global node; global data; global stndby; global stndbyL 
    
    if head == -1:
        print(f"\n\nwala i-Dedelete kasi tail ay {tail}")
        input("Press any key...")
        return 
    
    noDlt = 1
    i = node[head]    
    iBck = head
    while i != -1: #2
        if inpV == data[i]:#3                                     
            #data[dltI] = data[node[dltI]]
            if node[i] == -1: #4
                #asusin ang dulo ng tail
                tail = iBck
            #4
            
            fAddStandby(i)            
            node[iBck]= node[i]                            
            noDlt = 0
            print(f"na-delete na ang data {inpV}", end="")
            input()
            break
        #3
        iBck = i                 
        i = node[i]         
    #2

    if noDlt == 1:
        print(f"wlang nakitang idedelete data na {inpV}", end="")
        input()

#1C 

def fAddStandby(i): #1D
    global head; global tail; global node; global data; global stndby; global stndbyL; 
    #naabot na ang pag ka puno mag dagdag  ng 1 slot
    if stndbyL == len(stndby):#2
        stndby.append(-2)
        
        
        print(f"L90 stndbyL {stndbyL}, i {i}")
    
    #2
    
    print(f"L91 stndbyL {stndbyL}, i {i}")
    
    #record new deleted
    stndby[stndbyL] = i
    stndbyL +=1
    
    print(f"L92 stndbyL {stndbyL}, i {i}")

#1D

#get standby array value, para gamitin sa head at tail
def fGetStndby():#1D
    
    global head; global tail; global node; global data; global stndby; global stndbyL; 
   
    if stndbyL == 0:
        #kung wlang laman ay i return nalng ang newI, gagawa ng bago dahil ala nang slot
        #para sa node at data
        node.append(-2)
        data.append(-2)
        n = len(node)-1        
        return n        
    #may nakitang laman sa stndby 
    rtrn = stndby[ stndbyL-1]
    stndby[ stndbyL-1 ] = -1
    stndbyL -=1           
    return rtrn
#1D 

#global code
data = [-2]
node = [-1]
head = 0
tail = -1
stndby = [-2]
stndbyL = 0
    
while 1:#2
    print(f"\n\n***********************\nMONITOR VARIABLE head {head}, tail {tail}, stndbyL {stndbyL}\nnode {node}\ndata {data}\nstndby {stndby} \n***********************")
    print(f"q to quit, a to add, d to delete, p to display:  ", end="")
    inpV = input()

    if inpV == "q":#3
        break
    elif inpV == "a":#3.4        
        print(f"\n\ninput data number to add:  ", end="")
        inp = input()
        fAdd(int(inp))        
    elif inpV == "p":#3.5        
        fDspl()            
    elif inpV == "d": #3.7        
        print(f"\n\ninput data number to delete:  ", end="")
        inpV = input()
        fDlt(int(inpV))        
    else: #3.7
        print(f"\n\nAng na input ninyo na \"{inpV}\" ay wla sa menu\npress any....   ", end="")
        input()
    #3.7    
    
#2    

print(f"exit...")
