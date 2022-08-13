#!/usr/bin/env python3

#RSM 08052022 database pract on PyQt5

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5  import QtGui, QtCore


MAX_DATA_ARRAY = 6

class paren(QWidget): #1

      
      _widge = list([None for i in range(0, MAX_DATA_ARRAY)])
      _data_array = list(["" for i in range(0, MAX_DATA_ARRAY)] for j in range(0,3))
      #total max length ng _data_array      
      lengt = 0

      #ang index ng mga textbox, process must be less 1 because of 
      #the array real index count 0 to up
      _drive_next = None

      #gamit ng add button nag rerepresent kung anung button
      statu = None

      #parameter line_edit ay sasalinan ng isang list ng
      #paren._widge
      def f_copy_widge(self, set_widge):#2
            #L230 

            #self.widge ay isasalin ng isa-isa sa 
            #line_edit function
            i = 0 
            while i < MAX_DATA_ARRAY:#3

                  print(f"L231 {i= }, {set_widge= } \n")
                  set_widge.f_input_widge(self._widge[i])
                  i+=1
            #3
      #2

      def f_initi_data(self): #2

            #L70 

            blank = ["","b","5","d", "1","0"]
            for i in range(0, 3): #3
                  
                  _text = ""
                  for j in range(0, len(self._data_array[i]) ): #4
                  
                        if j== 2 or j== 4 :#5

                              self._data_array[i][j] = blank[j] 
                              _text = _text + blank[j]
                              _text+= ", "
                        elif j ==5:#5.2  

                              self._data_array[i][j] = "%0.2f"%( float(self._data_array[i][2]) * float(self._data_array[i][4]) )
                              _text = _text + "%0.2f"%( float(self._data_array[i][2]) * float(self._data_array[i][4]) ) 
                        elif j ==0 :#5.4

                              self._data_array[i][j] = str(i + 1) 
                              _text = _text + blank[j] + " " + str(i + 1) 
                              _text+= ", "


                        else: #5.3

                              self._data_array[i][j] = blank[j] + " " + str(i + 1) 
                              _text = _text + blank[j] + " " + str(i + 1) 
                              _text+= ", "
                        #5.3

                        
                  #4
                  
                  self.front.insertItem(i, _text)
                  self.lengt+=1
            #3


            #
            #self.front.takeItem(1)
            #self.front.clear()
            
            print( f"L74 {self.front.setCurrentRow(0)= } \n ")

            #input the first index in QLineEdit
            for i in range(0, len(self._data_array[0])): #5

                  self._widge[i].setText(self._data_array[0][i])

            #5
            
            self._drive_next =1
            self.lengt_label.setText( str(self._drive_next) )

            print(f"L75 {self._drive_next= }, {self.lengt= }, {self._data_array= }")
      #2

      def __init__(self): #2

            #L10 
            QWidget.__init__(self)
            self.setWindowTitle("test of layout")
            self.setFixedSize(600,400)

            self.f_layou()

            print(f"L10 self._data_array {self._data_array} \n")

      #2

      def f_layou(self): #2

            #L20

            self.front = QListWidget(self)
                      
            self.front.clicked.connect(self.f_click_front)            

            self.lengt_label = QLabel(self, text="")
            self.lengt_title = QLabel(self, text="count")

            self.lengt_qhbox  = QHBoxLayout()
            self.lengt_qhbox.addWidget(self.lengt_title,1)            
            self.lengt_qhbox.addWidget(self.lengt_label,3)
            
            self.front_layou = QVBoxLayout()
            self.front_layou.addWidget(self.front)
            self.front_layou.addLayout(self.lengt_qhbox)

            #self.front_layou.addWidget(self.lengt_label)            

            self.lengt_label.setText(str(self.lengt))
            self.lengt_label.setStyleSheet("border: 1px solid blue;")

            #make it front
            self.front_layou.setAlignment(Qt.AlignHCenter | Qt.AlignTop)     
          
            self.id =  QLineEdit(parent= self)           
            self.produ_name =  QLineEdit(parent= self)            
            self.price_per =  line_edit(self)  #QLineEdit(parent= self) 

            self._widge[0] = self.id    
            
            print(f"L20 self.id.text() {self.id.text()  }\n")

            self._widge[1] = self.produ_name    
            self._widge[2] = self.price_per     
            
      
            self._left = QFormLayout()
            self._left.addRow("Id:", self.id )
            self._left.addRow("Product Name:", self.produ_name)
            self._left.addRow("Price per unit:", self.price_per)

            self.date =  QLineEdit(parent= self) 
            self.numbe_of =   line_edit(self)    #QLineEdit(parent= self) 
            self.total_amoun =  QLineEdit(parent= self) 
            
            self._widge[3] = self.date     
            self._widge[4] = self.numbe_of    
            self._widge[5] = self.total_amoun 

            #copy a set of widget to be use by line_edit
            self.f_copy_widge( self.price_per)
            self.f_copy_widge( self.numbe_of)
            
            self._right = QFormLayout()
            self._right.addRow("Date:", self.date)
            self._right.addRow("Number of unit:", self.numbe_of)
            self._right.addRow("Total amount:", self.total_amoun)
            
            self._top =  QHBoxLayout()
            self._top.addLayout(self._left)
            self._top.addLayout(self._right)
            
            self._add = QPushButton(parent = self, text="add")
            self._edit = QPushButton(parent = self, text="edit")
            self._delet = QPushButton(parent = self, text="delete")
            self._back = QPushButton(parent = self, text="back")
            self._next = QPushButton(parent = self, text="next")
            
            self.ok = QPushButton(parent = self, text="ok")
            self._stop = QPushButton(parent = self, text="stop")
            self._find = QPushButton(parent = self, text="Find")
            self._exit = QPushButton(parent = self, text="exit")

            #L23 
            #on event click button      
            self._add.clicked.connect(self.f_click_add)
            self._edit.clicked.connect(self.f_click_edit)
            self._delet.clicked.connect(self.f_click_delet)
            self._find.clicked.connect(self.f_click_find)
            
            self.ok.clicked.connect(self.f_click_ok)
            self._stop.clicked.connect(self.f_click_stop)
            self._back.clicked.connect(self.f_click_back)
            self._next.clicked.connect(self.f_click_next)

            self._exit.clicked.connect(self.f_click_exit)
                       
            self._down = QGridLayout()
            self._down.addWidget(self._add, 0, 0)
            self._down.addWidget(self._edit, 0, 1)
            self._down.addWidget(self._delet, 0, 2)
            self._down.addWidget(self._find, 0, 3, 1, 2)


            self._down.addWidget(self.ok, 1, 0)
            self._down.addWidget(self._stop, 1, 1)
            
            self._down.addWidget(self._back, 1, 3)            
            self._down.addWidget(self._next, 1, 4)            
            self._down.addWidget(self._exit, 2, 0, 1 , 5)
            
            self.cente = QVBoxLayout()
            self.cente.addLayout(self.front_layou)
            self.cente.addLayout(self._top)
            self.cente.addLayout(self._down)
            self.cente.addStretch()
            self.setLayout(self.cente)

            self.f_initi_butto()
            self.f_initi_data()

            self.statu = 0
            
      #2

      #del laman at lamnan ulit ang front
      def f_refil_front(self, lengt):#2
            #L250

            self.front.clear()
            i  = 0 
            while i < lengt:#5
                  
                  j= 0
                  n = len(self._data_array[i]) 
                  while j < n :#7


                        if j==0: #8

                              _text = " " + self._data_array[i][j]
                            
                        else :#8.3

                              _text += ", " +  self._data_array[i][j]

                        #8.3            

                        j+=1
                  #7

                  self.front.insertItem(i, _text)   
                  i+=1
            #5

      #2

      def f_click_front(self): #2
            #L220 

            #display ang laman sa isang row
            #pero kaylangan ng .text function
            _item = self.front.currentItem()
            print(f"L221 {_item.text()= }, {_item= }, {self.front.currentRow()= }\n")
      
            selec = self.front.currentRow()

            self._drive_next = selec+1
            self.lengt_label.setText(str(self._drive_next)) 
            
            i =0
            while i < MAX_DATA_ARRAY :#3

                  self._widge[i].setText( self._data_array[self._drive_next -1][i] )
                  i+=1
            #3
      #2

      def f_arran_find(self, _drive_next_p):#2

            #L170
            i = 0 
            while i < self.lengt:#3

                  #less 1 to follow 0 to 3 index
                  if (_drive_next_p-1) == i:#4

                        j = 0
                        while j < MAX_DATA_ARRAY: #5
                                             
                              self._widge[j].setText( self._data_array[i][j] )
                              j+=1
                        #5

                        break     
                  #4
                  i+=1
            #3
      #2

      def f_click_delet(self): #2

            #L120 
            self.statu = "_delet"
            _text, retur = QInputDialog.getText(self, "Mensahe", "anung id yung i-delete", QLineEdit.Normal, \
            self._widge[0].text())


            if retur == 0:#3

                  #block cancel
                  return
            #3

            if _text == "":#3

                  #block none enter value 
                  QMessageBox.critical(self, "mensahe","hindi pede blank na input")
                  return
            #3

            retur, _text = self.f_input_numbe(_text) 
            if retur != True:#3

                  #block none enter value 
                  QMessageBox.critical(self, "mensahe","not-valid number ang pedng input")
                  return
            #3

            _find = 0
            #execute delete
            for i in range(0, len(self._data_array)) :#4                 

                  print(f"L22_2 {i= }, {self._data_array[i][0].strip()= }, {str(int(_text))= }\n")

                  if self._data_array[i][0].strip() == str(int(_text)): #5

                        self._data_array.pop(i)
                        self.lengt-=1
                        _find = 1
                        
                        print(f"L22_3 {self.lengt= }, {len(self._data_array)= },\n{self._data_array= }\n")
                        break
                  #5
                  
            #4

            #if fail to find the id
            if _find != 1:#7

                  QMessageBox.critical(self, "mensahe","hindi nakita ung id {_text}")
                  return
            #7

            #reset the focus 
            if self.lengt == 0 :#8

                  #empty then reset data
                  for i in range(0, MAX_DATA_ARRAY): #2

                        self._widge[i].setText("")
                  #2
                  self._drive_next =0
                  self.lengt_label.setText(str(self._drive_next))

                  return
            #8

            #reset form start
            self._drive_next = 1
            self.lengt_label.setText(str(self._drive_next))

            for i in range(0, MAX_DATA_ARRAY): #3

                        self._widge[i].setText(self._data_array[self._drive_next -1][i] )
            #3           

      #2
      
      def f_input_numbe(self, _text):#2

            #L140 

            try:#3
                  int(_text)
            except: #3.2
                  _text = "0"
                  return False, _text
            #3.2

            return True, _text
      #2
      def f_click_add(self):#2
            
            #L110 
            self.statu = "_add"
            self._add.setEnabled(False)
            self._edit.setEnabled(False)
            self._delet.setEnabled(False)
            self._back.setEnabled(False)
            self._next.setEnabled(False)
            
            self.ok.setEnabled(True)
            self._stop.setEnabled(True)
            self._find.setEnabled(False)            
            
            i=0
            while i < 6:#3

                  self._widge[i].setEnabled(True)

                  if 5 == i :#4
                         self._widge[i].setEnabled(False)
                  #4 

                  self._widge[i].setText("")
                  i+=1
            #3           
      #2

      def f_save_add(self):#2

            #L80 
          
            try:#3
                  #test it kung may laman
                  self._data_array[self.lengt]

            except IndexError:#3.2
            
                  self._data_array.append( ["" for i in range(0,6) ] )
                  print("L82\n")
            #3
            
            i = 0
            
            while i < 6: #4

                  print(f"L83 {i= }, {self.lengt= }\n")
                  self._data_array[self.lengt][i] = self._widge[i].text()
                  i+=1
            #4

            print(f"L83_2 {self.front.count()= } \n")
            
            self.lengt+=1
            self.f_refil_front(self.lengt) 
            self.front.setCurrentRow(self.lengt-1)
            self.lengt_label.setText(str(self.lengt))  
            self._drive_next = self.lengt
           
            print(f"L85 {self.front.count()= }, {self._data_array= }\n")
                           
      #2

      def f_click_edit(self):#2
            
            #L100 
            self.statu = "_edit"   

            self._add.setEnabled(False)
            self._edit.setEnabled(False)
            self._delet.setEnabled(False)
            self._back.setEnabled(False)
            self._next.setEnabled(False)
            
            self.ok.setEnabled(True)
            self._stop.setEnabled(True)
            self._find.setEnabled(False)            
            
            i=0
            while i < 6:#3

                  self._widge[i].setEnabled(True)

                  if i == 5 :#4
                        self._widge[i].setEnabled(False)

                  #4
                  i+=1
            #3                    
            
            self._widge[0].setFocus()
      #2

      def f_save_edit(self):#2
            
            #L130 
            n = len(self._data_array[self._drive_next-1])
           
            for i in range(0, n):#3

                  self._data_array[self._drive_next-1][i] =  self._widge[i].text()
                
            #3

            self.f_refil_front(self.lengt)

            #set focus on front
            self.front.setCurrentRow(self._drive_next-1)
      #2

    

      def f_initi_butto(self):#2
                  
            #L90 
            self._add.setEnabled(True)
            self._edit.setEnabled(True)
            self._delet.setEnabled(True)
            self._back.setEnabled(True)
            self._next.setEnabled(True)
            
            self.ok.setEnabled(False)
            self._stop.setEnabled(False)
            self._find.setEnabled(True)

            i=0
            while i < 6:#3

                  self._widge[i].setEnabled(False)
                  i+=1
            #3

      #2

      def f_click_back(self):#2
            
            #L60 

            self._drive_next -=1

            if self.lengt == 0 : #3
                  QMessageBox.warning(self, "mali", "wlang laman pa ang database", QMessageBox.Ok, QMessageBox.Ok)
                  self._drive_next +=1
                  return
            #3
           
            if self._drive_next <= 0 : #3
                  QMessageBox.warning(self, "mali", "sagad na sa mababa", QMessageBox.Ok, QMessageBox.Ok)
                  self._drive_next +=1
                  return
            #3
          
            for i in range(0, len(self._data_array[self._drive_next-1] ) ): #4

                   self._widge[i ].setText( self._data_array[self._drive_next-1][i] )
            #4

            self.front.setCurrentRow( self._drive_next -1)
            self.lengt_label.setText( str(self._drive_next) )

      #2

      def f_click_next(self):#2
      
            #L50 

            self._drive_next +=1

            if self.lengt == 0 : #3
                  QMessageBox.warning(self, "mali", "wlang laman pa ang database", QMessageBox.Ok, QMessageBox.Ok)
                  self._drive_next -=1
                  return
            #3
           
            if self._drive_next > self.lengt : #3
                  QMessageBox.warning(self, "mali", "sagad na sa mataas", QMessageBox.Ok, QMessageBox.Ok)
                  self._drive_next -=1
                  return
            #3
 
          
            for i in range(0, len(self._data_array [ self._drive_next-1] ) ): #4

                  #print(f"L53 {i= }, {self._drive_next-1= } \n { type(self._data_array[self._drive_next-1][i])= } \n")
            
                  self._widge[i ].setText( self._data_array[self._drive_next-1][i] )
            #4

            self.lengt_label.setText( str(self._drive_next) )
            self.front.setCurrentRow( self._drive_next -1)
      #2
      
      def f_click_ok(self):#2
            
            #L30 
            if self.statu =="_add": #3
                  self.f_save_add()
            elif self.statu =="_edit" :#3.2
                  self.f_save_edit()
            elif self.statu =="_delet" :#3.2
                  #no code here
                  pass
            #3.2

            self.f_initi_butto()      
      
      #2     
      
      def f_click_find(self):#2
            
            #L40 
            #print(f"L40 _data_array \n")
            
            #blocks if no data
            if self.lengt == 0 :#3
            
                  QMessageBox.information(self, "mensahe", "wlang laman ang data!")
                  return
            #3

            _text, retur =QInputDialog.getText(self, "Mensahe", "input ang i-find na id", QLineEdit.Normal, "")
            
            if retur != True: #3

                  #user canceled the process
                  return
            #3

            retur, _text = self.f_input_numbe(_text)
            if retur != True:#4

                  QMessageBox.critical(self, "mensahe", "number lang dapat ang input")
                  return
            #4

            _id = _text.strip()
            _equal = 0

            i = 0
            while i < self.lengt:#5

                  if _id == self._data_array[i][0].strip():#2
                        _equal = 1
                        #output index 1 to 3
                        targe_i = i+1
                        QMessageBox.information(self, "mensahe", f"nakita ko ang id {_id}")
                        break
                  #2
                  i+=1
            #5 

            if _equal != 1: #3

                  QMessageBox.critical(self, "mensahe", f"hindi ko nakita ang id na {_id}")
                  return
            #3
            

            #i find it then focus on that index
            self._drive_next = targe_i
            self.lengt_label.setText(str(self._drive_next))

            self.f_arran_find(self._drive_next) 

      #2

      def f_click_stop(self):#2

            #L160 
            retur = QMessageBox.information(self, "message", "stop, Y/ N", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes   )
            
            if retur == QMessageBox.Yes: #3
                  
                  if self.statu == "_edit": #4

                        i=0
                        while i < MAX_DATA_ARRAY:#5

                              self._widge[i].setText( self._data_array[self._drive_next-1] [i] )
                              i+=1
                        #5

                  #4
 
                  if self.statu == "_add": #4

                        i=0
                        while i < MAX_DATA_ARRAY:#5

                              self._widge[i].setText( self._data_array[self._drive_next-1] [i] )
                              i+=1
                        #5

                  #4
                  self.f_initi_butto()
            #3
      #2     
            
      def f_click_exit(self):#2

            #150 
            retur = QMessageBox.information(self, "message", "press y to quit, n for canceled", QMessageBox.Yes |  QMessageBox.No, QMessageBox.Yes)     
      
            if retur == QMessageBox.Yes:#3

                  self.destroy()
                  apps.quit()
            #3
      #2
                        
#1

class line_edit(QLineEdit):#10

      #L180 

      #_widge = list([None for i in range(0, MAX_DATA_ARRAY)] )

      _widge = [None, None, None, None, None, None ]

      widge_index = 0

      #def __str__():#2
          
      #2

      def keyPressEvent(self, event: QtGui.QKeyEvent)-> None: #2
            #L190
            super(line_edit,self).keyPressEvent(event)
            
            print(f"L180 {event.key()= }, {self.text()= }, {event.text()= } \n")
            
            if event.key() != QtCore.Qt.Key_Return and event.key() != QtCore.Qt.Key_Backspace and \
            event.key() != QtCore.Qt.Key_Left and event.key() != QtCore.Qt.Key_Right: #3
            
                  #filter none numbers
                  retur, _text = self.f_input_float(self.text() )
                  if retur != 1:#4
                  
                        QMessageBox.critical(self, "mensahe", "maginput ng numbers only")
                        #return
                  #4

                  #numbers and . will pass
            #3 

            #computation 
            self.f_nuetr_keypress()
                        
      #2

      #isalin ng isa-isa ang sa element ng self._widge
      #ang galing sa parameter _widge
      def f_input_widge(self, give_widge):#2
            #L240

            print(f"L241 {self.widge_index= },{give_widge= }, \n{self._widge= }\n")

            self._widge[self.widge_index] = give_widge
            self.widge_index+=1
      #2
     
      def f_input_float(self, _text):#2
            #L210

            if _text == ".":#4
                  
                  return 1, 0
            #4


            try :#3
                  float(_text)
            except :#3.2
                  
                  return 0, 0
            #3.2

            return 1, float(_text)
      #2
            
      def f_nuetr_keypress(self):#1
            #L200 

            retur, _float = self.f_input_float( self._widge[2].text() )
            
            a = _float
            
            retur, _float = self.f_input_float( self._widge[4].text() )
            
            b = _float

            self._widge[5].setText( str(b *a) )

      #1

#10

#testing mode
def f_testmode():#1
      #L260
      """
      a test i didnt put comment here to get warn that this function
      must be disable or continue testing
      global windo
      windo.front.clear()

      windo.front.insertItem(0,"abc1")
      windo.front.insertItem(1,"def")
      windo.front.insertItem(2,"ghi")
      """
      
#1

apps = QApplication(sys.argv)

windo = paren()

windo.show()

#disable muna kung wala pang testting
#f_testmode()

apps.exec()
sys.exit()
