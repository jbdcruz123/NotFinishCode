import threading
import time
import getch

def thread_function(name):#1A
      file_1 = open("a.txt", "w")    
      i =0  
      while i>=0 :#2
            time.sleep(.5)
            file_1.write(f"count: {i}\n")   
            file_1.flush()                                 
            i+=1      
      #2
      file_1.close()
#1A

thread_1 = threading.Thread(target= thread_function, args=(1,), daemon = True)
thread_1.start()
while 1:#2
      print("input:  ", end="")
      ch = getch.getch()
      #ch = input()      
      if ch =="q":#3
            break      
      #3
#2
