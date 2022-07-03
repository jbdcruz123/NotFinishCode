from copy import deepcopy

dct_1 = { "A":[1,2,3,5], "B":[11,17, 12,], "X": [30,31], "N":[8]}
dct_2 = { "A":[4,2,5,1], "B":[10,12,18], "X": [34,31], "N":[8]}

#mano mano kong linipat ung dict prm_1 sa rtrn dict
#gumamit ako ng lst_ind (para sa index) at lst_val (para sa value)
def fCpy(prm_1): #1c

      #nag manual debuging ako gamit kong output ay ung print ng python sa terminal
      
      #initial
      lst_ind = list([])
      rtrn = dict({})

      #copying the index of prm_1
      for ind, val in prm_1.items(): #2

            lst_ind.append(ind)
            
      
      #2
      print(f"L51 lst_ind {lst_ind}\n")
      i=0
      while i < len(prm_1): #2
            
            #gamit ng temporary pang lipat
            tmp = prm_1[lst_ind[i]]
            #ilipat ng mano mano tmp iikot ito at assign bangong list
            lst_val = list([])
            j =0                        
            while j < len(tmp):#3
                  lst_val.append( tmp[j] )
                  j+=1
            #3

            print(f"L52 lst_ind[i] {lst_ind[i]}, lst_val {lst_val}\n")
            #mag update ng bagong kopya
            rtrn.update({lst_ind[i]: lst_val})
                
            i+=1
      #2
      
      print(f"L54 rtrn {rtrn}\n")
      #break point ung input
      input()
      return rtrn            
#1c


def Srt(prm_1, prm_2): #1a
      #ikutan ng prm_2
      for ind_prm_2, val_prm_2 in prm_2.items(): #2
            lst_prm_2 = val_prm_2
            #kada isang prm_2 ikutan ng tig isang prm_1
            for ind_prm_1, val_prm_1 in prm_1.items(): #3
                  lst_prm_1 = val_prm_1
                                    
                  fLst_prc(ind_prm_1, ind_prm_2, lst_prm_1, lst_prm_2)
            #3
      #2
#1a

def fLst_prc(ind_prm_1, ind_prm_2, lst_prm_1, lst_prm_2): #1B
  
      #mag compare kung parehas ng index dict
      #pag same start process
      if ind_prm_1== ind_prm_2:#4
            
            #isang element ng lst_prm_2
            ind_lst_prm_2 = 0 
            while ind_lst_prm_2  < len(lst_prm_2): #5

                  #pakat sa 0 kung wlang kamukha
                  equ = 0

                   #isang element ng lst_prm_2 ay ikutan ng tig isang lst_prm_1
                  ind_lst_prm_1 = 0
                  while ind_lst_prm_1 < len(lst_prm_1): #7
                        
                        #pag may kamukha sa lst_prm_1 sa lst_prm_2 another set ng loop
                        if lst_prm_1[ind_lst_prm_1] == lst_prm_2[ind_lst_prm_2]: #8
                              equ=1
                              break
                        #8
                        ind_lst_prm_1 +=1

                  else: #7.2
                        #pag wlang kamukha sa lst_prm_1 at lst_prm_2
                        #add isang element sa lst_prm_1
                        if equ ==0: #10
     
                              lst_prm_1.append(lst_prm_2[ind_lst_prm_2])
                        #10
                  #7.2
                  ind_lst_prm_2 +=1                  
            #5      
                                                          
      #4
      #acsend order
      fAscnd(lst_prm_1)
#1B
  
def fAscnd(prm_1): #1c
      i=0
      while i < len(prm_1)-1: #2
            j = i
            ind = j
            while j < len(prm_1)-1:#3
                  if prm_1[ ind ]> prm_1 [j +1]: #4
                        t = prm_1[ ind ]
                        prm_1[ ind ] = prm_1 [j +1]
                        prm_1 [j +1] = t
                  #4
                  j+=1
            #3
            i+=1
      #2
      
#1c

#new module na nai-advice sa akin, sucessful
#dsp_1 = deepcopy(dct_1)
#dsp_1 = dct_1.copy()


######################################
#try na seperate ng mano mano
dsp_1 = fCpy(dct_1)

####################################3


#habang hindi pa nag babago ang dct_1
print(f"\n\nhabang hindi pa nag process\ndefined dsp_1 {dsp_1}\n\ndct_2 {dct_2}\n")

Srt(dct_1, dct_2)   

#bakit umipekto sa dsp_1 ang pag babago ng dct_1, samantalang copy lang ito ng dct_1
print(f"\n\nung nag bago ng value ang dct_1 \n\ninput 1(dsp_1): {dsp_1}\n\ninput 2(dct_2): {dct_2}\n\n")

print(f"result dct_1 {dct_1}\n")
print(f"result dct_2 {dct_2}\n")






