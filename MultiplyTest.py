#simple project RSM 5/25/2022
#Multiplication game

import random as rnd
from os import system
from time import sleep

#main menu
def fMenu():#1C
      system("clear")

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
            sleep(.5)
            system("clear")
      #2
#1C

#input ng user, salain ang none numbers
def fInput():#1B

      try: #2
            answer = int(input())

      except: #2.2
            answer = 0
      #2.2

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

            answer = fInput()
            product = ques[i][0] * ques[i][1]

            if answer == product:#3
                  status[i]= 1
                  print(f"\n")
            else: #3.2
                  print(f"\nMali sagot, Ang sagot ay {product}\n")
            #3.2

            i+=1
       #2

#1A

list_1 = [2,3,4,5,6,7,8,9]
ques= [[0,0],[0,0],[0,0]]
status = [0,0,0]
ques_Front = ["Unang tanong","Pangalawang tanong", "Pangatlong tanong"]

fMenu()
