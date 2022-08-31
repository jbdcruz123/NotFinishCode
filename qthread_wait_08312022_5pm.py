
#08312022-5pm gumamit ako ng .wait() para magclose muna ung infinite loop
#ng run ng qthread bago isara ung main window

import sys
from PyQt5 import QtWidgets, QtCore
import datetime
import time

#global swither to leave na program

class paren(QtWidgets.QWidget):#1

      def __init__(self, _name):#2
            super().__init__()
            self._name = _name
            self.setWindowTitle("main parent")
            self.setFixedSize(600,400)
            self.move(200,200)
            self.label = QtWidgets.QLabel(parent=self, text="this is the parent")
            self.label.resize(200, 50)
            self.label.move(250,150)
            self.butto = QtWidgets.QPushButton(parent=self, text="close")
            self.butto.resize(200, 50)
            self.butto.move(250,200)
            
            self.butto.clicked.connect(self.f_click)
      #2

      def f_exec_timer(self,_qdialog = None, _timer = None):#4

            #setting up nung mga widgets galing sa labas
            self._qdialog = _qdialog          
            self._timer = _timer
            self._timer.start()            
            self._timer.currentTimeSignal.connect(self.timeReceiverFunction)

      #4

      def timeReceiverFunction(self, received_time):#2
            
            #self._qdialog.setWindowTitle(f"enter password (is 123)  {received_time}")
            self.setWindowTitle(f"Main Window {received_time}")
          
      #2

      def f_click(self):#3         
            print(f"L60 \n")             
            self._timer._quit= True
            self._timer.wait()

            self.close()
      #3
  
      def closeEvent(self, event):#2

            print(f"L50 \n")            
            self._timer._quit= True
            self._timer.wait()                       

      #2
      
#1


class child(QtWidgets.QDialog):#1

      def __init__(self, paren = None, _name = "first"):#2
            super().__init__(paren)
            self._name = _name
            self.setWindowTitle("enter password   ")
            self.setFixedSize(400,300)
            self.move(100,100)

            self.label = QtWidgets.QLabel(parent=self, text="input: ")
            self.label.resize(150, 30)
            self.label.move(70,10)

            self.edit = QtWidgets.QLineEdit(parent=self, text="")
            self.edit.resize(200, 30)
            self.edit.move(120,10)
            
            self.butto = QtWidgets.QPushButton(parent=self, text="ok")
            self.butto.resize(150, 30)
            self.butto.move(40,60)
            
            self.butto_2 = QtWidgets.QPushButton(parent=self, text="cancel")
            self.butto_2.resize(150, 30)
            self.butto_2.move(200,60)

            self.butto.clicked.connect(self.f_click)
            self.butto_2.clicked.connect(self.f_click_butto_2)
            
            self.paren=None
            self.setModal(True)
      #2
      def f_click(self):#3

            if self.edit.text() == "123":#2
               
                  #need parameter to close
                  #self.done(0)
                  self.accept()
                  self.paren.label.setText("password is right")
                  return
            #2

            QtWidgets.QMessageBox.information(self, "mensahe", "wrong password")
      #3

      def f_click_butto_2(self):#4
            
            print(f"L20 \n")
            #call the close() nag error runing ito
            
            self._timer._quit= True
            self._timer.wait()
            print(f"L21 \n")
            
            appli.quit()

      #4
     
      def closeEvent(self, event):#3
           
            #L30 
            print(f"L30 \n")
            self._timer._quit= True
            self._timer.wait()
            appli.quit()
      #3

      def keyPressEvent(self, event):#2
            #L20
            #prevent the base class to call this
            #super().keyPressEvent(event)
            
            print(f"{event.key()= }")
            if 16777216 == event.key() :#3
                  event.ignore()
                  print(f"L20 \n")
            #3
      #2

      def f_input_timer(self, _timer):#2
            self._timer = _timer
      #2
#1

class TimeThread(QtCore.QThread):#1
     
      currentTimeSignal = QtCore.pyqtSignal(str)
      #flag to close the thread
      _quit = False
      def run(self):#2

            while True:#3
                  #format ng date 
                  #strftime('%b %d, %Y %I:%M:%S %p')
                  current_date = datetime.datetime.now().strftime('%I:%M:%S %p')
                  self.currentTimeSignal.emit(current_date)
                 
                  print(f"{self._quit= }, {current_date= } ")
                  
                  if self._quit == True:#4
                        break
                  #4
                  time.sleep(0.5)
            #3
      
      #2
#1

appli = QtWidgets.QApplication(sys.argv)


_paren = paren("parents") 

_child = child(_paren, "child")
_child.paren = _paren

_timer = TimeThread(_child)

_paren.f_exec_timer(_child, _timer)
_child.f_input_timer(_timer)

_paren.show()
_child.show()

appli.exec()
sys.exit()




