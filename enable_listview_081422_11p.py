#!/usr/bin/env python3

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5  import QtGui, QtCore


class paren(QWidget):#1

      MAXIM_LENGT = 5
      list_lengt = 0
      data_array = []
      disab = 0
      list_targe = 0

      def __init__(self):#2

            super().__init__()
            self.setWindowTitle("QListWidget")
            self.setFixedSize(600,300)
            self._grid = QGridLayout()
            
            self.push_butto = QPushButton(self, text = "disabled")
 
            self.list_view = QListWidget(self)
            
            self._grid.addWidget(self.list_view, 0, 0)
            self._grid.addWidget(self.push_butto, 1, 0)
            self.push_butto.clicked.connect(self.f_click_butto)
            self.list_view.clicked.connect(self.f_click_list_view)

            self.butto_back = QPushButton(self, text="back")
            self.butto_next = QPushButton(self, text="next")
            self.label_middl = QLabel(self, text ="test") 
            self.qhbox = QHBoxLayout()

            self.qhbox.addWidget(self.butto_back) 
            self.qhbox.addWidget(self.label_middl)
            self.qhbox.addWidget(self.butto_next)

            self.butto_back.clicked.connect(self.f_click_butto_back)
            self.butto_next.clicked.connect(self.f_click_butto_next)
            self.cente =  QVBoxLayout()
            self.cente.addLayout(self._grid)
            self.cente.addLayout(self.qhbox)
            self.setLayout(self.cente)

            self.f_initi_data()
      #2

      def f_refre_list_view(self): #2

            self.list_view.clear()

            i=0
            #start to copy again
            while i < self.list_lengt: #3

                  self.list_view.insertItem( i,  self.data_array[i])
                  
                  i+=1
            #3 

            self.list_view.setCurrentRow(self.list_targe -1)
      #2

      def f_initi_data(self):#2

            i = 0
            while i < self.MAXIM_LENGT:#3

                  self.data_array.append(f"mark_index {i+1}")
                  i+=1
            #3

           
            self.list_targe = 1
            self.label_middl.setText(self.data_array[self.list_targe-1])
      #2

      def f_click_list_view(self): #2

            self.list_targe = self.list_view.currentRow()

            self.list_targe+=1
            self.label_middl.setText(self.data_array[self.list_targe-1])

      #2

      def f_click_butto_back(self):#2
            
            self.list_targe-=1

            if self.list_targe <= 0:#3

                  QMessageBox.critical(self, "mensahe", "nasa 0 target")
                  self.list_targe+=1
                  return
            #3

            self.label_middl.setText(self.data_array[self.list_targe-1] )
            self.list_view.setCurrentRow(self.list_targe-1)

      #2

      def f_click_butto_next(self):#2

            print(f"L10 {self.list_lengt= }")
            self.list_targe+=1
            if self.list_targe > self.list_lengt:#3

                  QMessageBox.critical(self, "mensahe", f"mataas sa max na {self.list_lengt}")
                  self.list_targe-=1
                  return 
            #3

            self.label_middl.setText(self.data_array[self.list_targe-1] )
            
            self.list_view.setCurrentRow(self.list_targe-1)
            
      #2

      def f_input_item(self, _input):#2

            self.list_lengt+=1
                         
            self.list_view.insertItem(self.list_lengt-1, _input)
      #2

      #controls switcher of enabled and disable QListWidget
      def f_click_butto(self):#2

            n  = self.list_view.count()

            if self.disab != 1 :#3

                  i = 0
                 
                  while i < n: #4
             
                        _item = self.list_view.item(i)
                        _item.setFlags(Qt.NoItemFlags)                        
                        i+=1
                  #4

                  self.disab = 1
                  self.push_butto.setText("enabled")
                  self.butto_back.setEnabled(False)
                  self.butto_next.setEnabled(False)
                 
                  return
            #3


            i = 0
   
            while i < n: #4

                  _item = self.list_view.item(i)
                  _item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                  i+=1
            #4

            self.disab = 0
            self.push_butto.setText("disabled")
            self.butto_back.setEnabled(True)
            self.butto_next.setEnabled(True)
                 
            #2nd option iclear at icopy ulit lhat ng data            
            #self.f_refre_list_view()

            self.list_view.setCurrentRow(self.list_targe-1)
      #2

#1


apps = QApplication(sys.argv)


windo = paren()

#adding some items

i = 0 
n = 5
while i < n:#2

      print(f"L20 {i= }\n")
      windo.f_input_item(windo.data_array[i])
       
      i+=1
#2


print(f"L21 {windo.list_lengt= }\n")



windo.list_view.setCurrentRow(windo.list_targe-1)

windo.show()

apps.exec()

sys.exit()


