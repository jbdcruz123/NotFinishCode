
#node 
#rsm singly list type

class node :#2

      data = None
      next = None
      
#2

class head :#2
      next = None
      tail = None
#2

class _operate: #2

      def add(self, param): #3
            new = node() 
            
            print("\n\nadd mode\n")
            new.data = input("input data:   ")
            
            if param.tail == None : #4
                  param.next = new
                  param.tail = new
                  return
            #4
            
            param.tail.next = new
            
            param.tail = new
            print("\n\n")
      #3
      
      def display(self, param):#3
            
            print("\n\ndisplay mode\n")
            move = param
            i=0
            while move.next != None: #4
                  print( f"index: {i },  data: {move.next.data }")       
                  i +=1
                  move = move.next  
            #4
            print("\n\n")
      #3
          
      def delete(self,  param, index):#3
            move = param
            i=0
            print("\n\ndelete mode\n")
            while move.next != None: #4
                  #print(f"L10 {index=}, { i} \n")
                  if index == i :#5
                        data = move.next.data
                                  
                        if param.tail == move.next and i == 0: #7
                              param.tail = None                      
                                                           
                        elif param.tail == move.next : #7
                              param.tail = move
                        #7
                        
                        move.next = move.next.next
                        print(f"nadelete na ang index {index}, data {data}" )
                        return
                  #5
                  i +=1
                  move = move.next  
            #4
            
            print(f"walang nakitang index {index} ")
            print("\n\n")
      #3
      
      def edit( self, param, index):#3
      
            print("data to edit: \n")
            move = param
            
            i =0
            while move.next != None :#4
                  
                  if i == index :#5
                        print(f"input edit data:    " , end="")
                        data = input()
                        move.next.data = data
                        print("nai-edit na ang index {index}\n{data} " )
                        return
                  #5
                  
                  i+=1
                  move = move.next
                  
            #4
            
            print(f"walang nakita sa index {index} " )
            print("\n\n")
            
      #3
      
#2

def check_int(num):#2

      num = num.strip( )
      try: #3
            num = int(num)
            return num
      except: #3.2
      
            return -1      
      #3.2
#2

_head = head()
operate_obj = _operate()

main_loop = True
while main_loop:#3

      print(f"\n##############################\nentering prog\npress q to leave\npress a add\npress d display\npress e delete\npress i to edit    ", end="")    
      v = input( )        
      
      if v == "q": #4
            break
      #4
      
      if v == "a":#5
            operate_obj.add( _head)
      #5
      
      if v == "d": #7
            operate_obj.display( _head)
      #7
      
      
      if v == "e": #7
            #delete
            print(f"\n\ndelete mode:   \n")
            while 1: #9
                  print("input index to delete:   ", end ="")
                  index = input()
                  index =  check_int( index)
                  if index >= 0: #8
                  
                        break
                  #8
                  
                  print("\ndapat int ang input\nhindi pede ang negative numbers    \n")      
            #9
            
            operate_obj.delete( _head, index)
      #7
      
      if v == "i": #8
      
            while True :#4
                  print("mag input ng index para i-edit:", end= "   ")      
                  v = input()
                  v = check_int( v)
                  
                  #edit it
                  if v >= 0: #5
                        operate_obj.edit(_head, v )
                        break
                  #5
                  print("number lng ang pedeng input\n ")
            #4
          
      #8
      
#3



