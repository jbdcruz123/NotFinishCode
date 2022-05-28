import time
import threading
import os
import signal
import random as rnd

def thread_function(name):#1A
        global start_Timer
        
        i=0
        while 1:#2

                if start_Timer >= 1: #4 	

                        if start_Timer == 2: #5
                                #inital count, value 2 intial, 1 middle iterate
                                start_Timer = 1
                                delay = 3
                                i = 0      
                                print(f"count: ", end="")                  
                        #5
                        																																																																																																											
                        time.sleep(1)
                        #para mapigilan ang bilis ng pag lipat
                        if i >= delay and start_Timer != 0:#3
                                os.kill(os.getpid(), signal.SIGINT)
                                start_Timer = 0
                                continue
                        elif start_Timer == 0:#3.2
                                #para hindi makadaan sa printout ng i
                                continue
                        #3.2
                        print(f"{i+1} ") 
                       
                #4               
                i+=1        
        #2

#1A																																																																								

#main menu
def fMenu():#1C
      os.system("clear")

      while 1: #2
            print(f"\n\nMultiply test\nPasok 3 tanong: \n")
            fRandom()	
            fQues()
            print(f"Ang bilang ng tumama ay {fAnswer()}\n\npress q para mag leave, press kahit ano to continue  ", end="")
            answer = input()

            if answer == "q":#3
                  print(f"\n\nPalabas na ng prog...")
                  break
            #3
            #pause panadalian then burahin lahat ng nasa screen
            print(f"Pa-antay lng po")
            time.sleep(.5)
            os.system("clear")
      #2
#1C

#input ng user, salain ang none numbers
def fInput():#1B

        try: #2
                answer = int(input())                
        except KeyboardInterrupt: #2.2
                #para pag naabutan ng timer
                answer = -1        
        except: #2.3  
                #para sa hindi number na napindot      
                answer = 0
        #2.3

        return answer

#1B

#Count lahat ng tamang sagot
def fAnswer(): #1D
      count = 0
      n =3
      i=0
      while i < n:#2

            if status[i] == 1:#3
                   count +=1
            #3
            i+=1
      #2

      return count
#1D

#pag assign ng random question
def fRandom(): #1E

      n_1= 3
      n_2 =2
      i =0
      while i < n_1: #2
            j=0

            while j < n_2: #3
                  ques[i][j] = rnd.choice(list_1)
                  j+=1
            #3
            i+=1
      #2

#1E

#fQuestion, process ng display at input at computation 
def fQues():#1A
        global start_Timer
        n_1 = 3

        #initialize
        i= 0
        while i < n_1:#5
                status[i]= 0
                i+=1
        #5

        i = 0
        while i < n_1:#2
                print(f"{ques_Front[i]}\n\n  {ques[i][0]} \n* {ques[i][1]}\n-------")
                #sets the timer                
                start_Timer = 2  
                answer = fInput()
                product = ques[i][0] * ques[i][1]

                if answer == product:#3
                        status[i]= 1
                        print(f"\n")
                elif answer == -1:#3.4 
                        print(f"Naabutan ka ng oras...")        
                else: #3.2
                        print(f"\nMali sagot, Ang sagot ay {product}\n")
                #3.2

                i+=1
        #2
        start_Timer = 0
#1A

start_Timer = 0
x = threading.Thread(target=thread_function, args=(1,), daemon= True)
x.start()																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																											

#value 0 disable, 2 initial loop, 1 middle loop

list_1 = [2,3,4,5,6,7,8,9]
ques= [[0,0],[0,0],[0,0]]
status = [0,0,0]
ques_Front = ["Unang tanong","Pangalawang tanong", "Pangatlong tanong"]

fMenu()

