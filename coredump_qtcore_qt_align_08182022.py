#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtCore

_posit = [None, None]

class paren(QtWidgets.QWidget): #1


      def __init__(self, _paren= None, _name = "paren", _index = 0):#3

            super().__init__()
            self._name = _name
            self._index = _index

            self.setWindowTitle("practice")
            self.setFixedSize( int( _posit[0] ), int( _posit[1] ) )
            self.qhbox = qhbox_layout(right_left = 0)
            self.qhbox_botto = qhbox_layout()
            
            self._qlabel = qlabel(self, _text = "input:  ")
            self._qline_edit = qline_edit(self)
            self._qpush_butto = qpush_butto(self, _text = "ok")

            self._qlabel_botto = qlabel(self, _text = "input bottom:  ")
            self._qline_edit_botto = qline_edit(self)
            self._qpush_butto_botto = qpush_butto(self, _text = "ok")

            

            self.qhbox.addWidget(self._qlabel,0)
            #self.qhbox.addStretch(3)
            self.qhbox.addWidget(self._qline_edit,2)
            self.qhbox.addWidget(self._qpush_butto,1)
                             
            
            #self.qhbox.addSpacing(10)
            self.qhbox.insertSpacerItem(0, QtWidgets.QSpacerItem(5,5))

            self.qhbox_botto.addWidget(self._qlabel_botto,0)
            self.qhbox_botto.addWidget(self._qline_edit_botto,2)
            self.qhbox_botto.addWidget(self._qpush_butto_botto,1)
            self.qvbox = qvbox_layout(top_botto = 0)
            
            self.qhbox_proce = qhbox_layout(right_left = 0)

            self.butto_proce_1 = qpush_butto(self, _text ="test QSizePolicy")
            self.butto_proce_2 = qpush_butto(self, _text ="test insertspacing")
            self.butto_proce_3 = qpush_butto(self, _text ="process3")
            
            self.butto_proce_1.clicked.connect(self.f_click_butto_proce_1)
            self.butto_proce_2.clicked.connect(self.f_click_butto_proce_2)
            self.butto_proce_2.clicked.connect(self.f_click_butto_proce_3)
      
            self.qhbox_proce.addSpacing(50)
            self.qhbox_proce.addWidget(self.butto_proce_1)
            self.qhbox_proce.addWidget(self.butto_proce_2)
            self.qhbox_proce.addWidget(self.butto_proce_3)
            self.qhbox_proce.addSpacing(50)

            self.qvbox.addLayout(self.qhbox_proce)
            self.qvbox.addLayout(self.qhbox)
            self.qvbox.addLayout(self.qhbox_botto)
            
            self.setLayout(self.qvbox)

      #3

      def f_click_butto_proce_1(self): #2
            #L30
            _qsize_policy = qsize_policy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.LineEdit )   
            
            #_qsize_policy = qsize_policy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Frame )   
            
            print(f"L31 {type(_qsize_policy) }\n")    
            print(f"L31_2 { _qsize_policy.controlType=  }\n")    

      #2

      def f_click_butto_proce_2(self): #2
            #L40
 
            a = qlayout_item()
            self.qvbox.insertItem(0, a)

      #2
      def f_click_butto_proce_3(self): #2
            #L50
            pass
      #2
#1

class qline_edit(QtWidgets.QLineEdit): #2

      def __init__(self, paren, _name= "qline_edit", _index = 0, _text = "" ): #3
            super().__init__(parent = paren, text = _text)
            self._name = _name
            self._index = _index
                        
      #3


#2

class qpush_butto(QtWidgets.QPushButton): #2

      def __init__(self, paren, _name= "qpush_button", _index = 0, _text = "" ): #3
            super().__init__(parent = paren, text = _text)
            self._name = _name
            self._index = _index
                        
      #3

#2

class qlabel(QtWidgets.QLabel): #2

      def __init__(self, paren, _name= "qpush_button", _index = 0, _text = "" ): #3
            super().__init__(parent = paren, text = _text)
            self._name = _name
            self._index = _index
                        
      #3

#2

class qhbox_layout(QtWidgets.QHBoxLayout): #4

      def __init__(self, paren=None, _name= "qpush_button", _index = 0, _text = "", right_left = 1 ): #3
            super().__init__(paren)
            self._name = _name
            self._index = _index
            if right_left == 1 : #2 
                  self.setDirection(self.RightToLeft)       
            else: #2.2
                  self.setDirection(self.LeftToRight)    
            #2.2
      #3

#4

class qvbox_layout(QtWidgets.QVBoxLayout): #4

      def __init__(self, paren=None, _name= "qpush_button", _index = 0, _text = "", top_botto = 1 ): #3
            super().__init__(paren)
            print(f"L21 \n")
            self._name = _name
            self._index = _index
            if top_botto == 1: #2
                  self.setDirection(self.TopToBottom)
            else :#2.2
                  self.setDirection(self.BottomToTop)
            #2.2
      #3

#4

class qsize_policy(QtWidgets.QSizePolicy): #2

      def __init__(self,horizontal=None, vertical=None, _type =None   ): #3
            super().__init__(horizontal, vertical, _type)
            
            
      #3
#2

class qlayout_item(QtWidgets.QLayoutItem): #2

      def __init__(self): #3
            qt_align = QtCore.Qt.AlignTop
            super().__init__(qt_align)
                 
      #3
#2

#L40
appli = QtWidgets.QApplication(sys.argv)


_text, retur = QtWidgets.QInputDialog.getText(None, "mensahe", "mag input ng size ex: \"numberxnumber\"\nrange 300 to 800", QtWidgets.QLineEdit.Normal, "")

if retur != True :#3

      QtWidgets.QMessageBox.information(None, "mensahe", "use default 400x300")
      _posit= ["600", "300"]
else:#3.2


      _posit = _text.split('x') 

      if int( _posit[0] ) < 300 or int( _posit[0] ) > 800 :#2

            QtWidgets.QMessageBox.information(None, "mensahe", "first value range 200 to 800\naalis na ito")
            sys.exit()
      elif int( _posit[1] ) < 300 or int( _posit[1] ) > 800:#2.2 

            QtWidgets.QMessageBox.information(None, "mensahe", "second value range 200 to 800\naalis na ito")
            sys.exit()
      #2.2

#3.2



print(f"L41  { _posit= } \n")
      

windo = paren()

windo.show()

appli.exec()

sys.exit()



"""
            #self.qvbox.insertItem(3, QtWidgets.QLayoutItem(QtCore.Qt.AlignHCenter)) #this is not working
            #insertSpacing()
            #self.qvbox.insertSpacing(3, 100)
            #QtCore.Qt.AlignHCenter        
            #self.qvbox.insertSpacing(1, 10)
            #self.qvbox.insertWidget(0, self.butto_proce_3, 10,a.alignment() )
"""
