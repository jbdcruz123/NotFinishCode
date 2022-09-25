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

      print( "\n\ndisplay mode:    \n  " )
      i = 0
      move = _node
      while move.next != None : #2
            
            print( f"index {i},  data {move.next.data},  back { move.next.back.data} next {move.next.next }" )              
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
                   
                         tail = tail.back
                         tail.next = None
                         return tail
                   #4        
                   b = move                                             
                   move = move.next.next
                   move.back = b
                   return tail
            #3
            i+=1
            move = move.next
      #2
      
      print(f"wlang nakita na index {index } \n\n " )  
      return tail
#1

_node = node( )
#head value
_node.back = "@#$&"
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

#2
