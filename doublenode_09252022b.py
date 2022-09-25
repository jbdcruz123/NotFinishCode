#doube node

# n.back  next data

class node:#1

      data = None
      back = None
      next = None
      
#1

def add(_node, tail ): #1
      
      print(f"\n\nadd mode: \n " )
      move = _node
      
      print( "input value para sa add:   ", end ="")
      data = input( )
      new = node( )
      new.data = data

      #print(f"L10 {tail.next= } \n  "   )
      tail.next = new
     
      #print(f"L10_b {tail.next.back.data= }    "   )
      
      tail.next.back = tail
     
      #print(f"L10_c  {tail.next.back.data= }   "   )
      tail = new
      
      #print(f"L10_d  {tail.data= }   "   )
      
      return tail
#1

def display( _node, tail ):#1

      move = _node
      print( "\n\ndisplay mode:    \n  " )
      
      if move == None: #20
            mv = None
      else: #20       
            mv = move.data 
      #20
      
      if move.back == None: #21
             bc = None
      else: #21   
             bc = move.back.data
      #21
      
      if move.next == None: #20
             nx = None
      else: #20       
             nx = move.next.data
      #20
      
      print(f"index -1, { mv= }, {bc= }, {nx= } \n")
      i = 0
      
      while move.next != None : #2
            
                              
            if move.next == None: #20
                  mv = None
            else: #20       
                   mv = move.next.data 
            #20
      
            if move.next.back == None: #21
                   bc = None
            else: #21   
                   bc = move.next.back.data
            #21
      
            if move.next.next == None: #20
                  nx = None
            else: #20       
                  nx = move.next.next.data
           #20
      
            
            print(f"index {i }, node { mv }, back {bc }, next {nx } \n")     
            
           #print( f"index {i},  data {move.next.data},  back { move.next.back.data} next {move.next.next }" )              
            i+=1
            move = move.next
      #2

#1

def delete( _node, tail, index ):#1
      i= 0
      move = _node
      while move.next != None: #2
      
            if index == i: #3
                  
                   print(f"tagumpay na-delete index {index } \n\n " )

                   if move.next == tail: #4
                   
                         s = tail.back
                         s.next = None
                         tail = s
                         print(f"L22 \n  " )
                         return tail
                   #4        
                   b = move                                             
                   move.next = move.next.next
                   move.next.back = b
                   print(f"L22_b \n  " )
                   return tail
            #3
            i+=1
            move = move.next
      #2
      
      print(f"wlang nakita na index {index } \n\n " )  
      return tail
#1

def insert(_node, tail, index, data ): #2

      move = _node
      new = node( )
      new.data = data
      i = 0
      while move.next :#3
            if i == index:#4
            
                  b = move.next.back
                  move.next.back = new
                  new.back = b
                  new.next = move.next
                  b.next = new
               
                  
                  print(f"\ntagumpay na nai-insert ang index {index }\n\n " )  
                  return tail                
            #4
            move = move.next
            i+=1
      #3
      
      print(f"\nwlang nakita na index {index } para i-insert data\n\n " )  
      return tail
#2

_node = node( )
#head value
_node.data ="head"
tail = _node

while True:#2

      print(f"\n\n##############\npress  q to leave\npress a add\npress d display\npress e delete\npress i to insert data", end ="   " )
      v = input( )
     
      if v == "q":#3
            break
      #3
      
      if v == "a": #4
            tail = add(_node, tail)
      #4
      
      if v == "d": #5
            display(_node, tail)
      #5
      
      if v == "e": #7
      
            print("\n\ndelete mode\n")
            index = input( "input index for delete   " )
            index = int( index )
            tail = delete(_node, tail,  index)
            
      #7
      
      if v == "i": #7
            #insert
            print("\n\ninsert data mode\n")
            index = input( "input index for insert data   " )
            index = int( index )
            data = input( "input data for insert data   " )
            tail = insert(_node, tail,  index, data)
            
      #7

#2






