import threading
import time
import os
def gotoxy(x,y):
      print ("%c[%d;%df" % (0x1B, y, x), end='')
def thread_function(name): #1B
      global start_Timer
      i = 0 
      delay = 0
      while 1:#2
            if start_Timer >=1:#3
                  if start_Timer ==2: #4
                        start_Timer = 1
                        delay =3
                        i = 0
                  #4
                  time.sleep(1)
                  if i >= delay and start_Timer != 0:#5
                        start_Timer = 0
                        i=0
                        fRePrint()
                        gotoxy(40,15)
                        print(f"Time out na....",end="")
                        os.sys.stdout.flush()
                        fRePostion()                       
                        continue
                  elif start_Timer ==0: #5.2
                        continue
                  #5.2
                  fRePrint()
                  gotoxy(40,15)
                  print(f"count: {i+1}",end="")
                  os.sys.stdout.flush()
                  fRePostion()
                  i+=1
            else: #3.2
                  i=0           
            #3
      #2
#1B
def fRePrint():#1A
      global front
      os.system("clear")
      gotoxy(10,10)
      print(front, end="")
      os.sys.stdout.flush()
#1A
def fRePostion():#1C
      gotoxy(len(front)+10,10)
      print(end="")
      os.sys.stdout.flush()
#1C      

start_Timer = 0
front = "press s, para 3 sec, press q quit: "
x = threading.Thread(target=thread_function, args=(1,) ,daemon= True)
x.start()
fRePrint()
while 1: #2      
      ch  = input()
      if ch == "s":#4
            start_Timer = 2
           
      #4

      if ch == "q":#3
            break
      #3            
#2



