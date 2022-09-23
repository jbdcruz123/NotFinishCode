
#node

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
            new.data = input("input data:   ")
            
            if param.tail == None : #4
                  param.next = new
                  param.tail = new
                  return
            #4
            
            param.tail.next = new
            
            param.tail = new
         
      #3
      
      def display(self, param):#3
            move = param
            i=0
            while move.next != None: #4
                  print( f"index: {i },  data: {move.next.data }")       
                  i +=1
                  move = move.next  
            #4
            
      #3
#2

_head = head()
operate_obj = _operate()

main_loop = True
while main_loop:#3

      print(f"entering prog, q to leave, \npress a add\npress d display    ")    
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
      
#3



