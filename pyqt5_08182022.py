PyQt5 lecture RSM 7/18/2022

class PySide6.QtWidgets.QMessageBox(icon, title, text[, buttons=QMessageBox.StandardButton.NoButton[, 
parent=None[, flags=Qt.Dialog | Qt.MSWindowsFixedSizeDialogHint]]])
PySide6.QtWidgets.QMessageBox([parent=None])

PARAMETERS
parent – PySide6.QtWidgets.QWidget

icon – Icon

flags – WindowFlags

text – str

title – str

buttons – StandardButtons


format is 

a: Constant


b: Description

a: QMessageBox = noIcon  #note use small letter at the begining of word of func ex noIcon()

b: the message box does not have any icon.

follow the series...

QMessageBox.question   

an icon indicating that the message is asking a question.

QMessageBox.information

an icon indicating that the message is nothing out of the ordinary.

QMessageBox.warning

an icon indicating that the message is a warning, but can be dealt with.

QMessageBox.critical

an icon indicating that the message represents a critical problem.

####################
#QtWindowModality
https://www.riverbankcomputing.com/static/Docs/PyQt4/qwidget.html#setWindowModality

#solution to take effect the change of windowModality
https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QWidget.html#PySide2.QtWidgets.PySide2.QtWidgets.QWidget.windowModality

PySide2.QtWidgets.QWidget.windowModality()
Return type
WindowModality

This property holds which windows are blocked by the modal widget.

This property only makes sense for windows. A modal widget prevents widgets in other windows from getting input.
The value of this property controls which windows are blocked when the widget is visible. Changing this property 
while the window is visible has no effect; you must hide() the widget first, then show() it again.

By default, this property is NonModal .


####################
https://stackoverflow.com/questions/40622095/pyqt5-closeevent-method

If you want to close an PyQt5 app from a menu:

When menu event triggered call: self.MainWindow.close() (or what window do you want to close
Add this code before sys.exit(app.exec()): self.MainWindow.closeEvent = lambda event:self.closeEvent(event)
Declare def closeEvent(self,event): method when you really want to close call event.accept() (and perhaps 
return 1) and if you don't want to close the window call event.ignore() (not event.reject() (it's not working for me))


########################################

https://pythonspot.com/pyqt5-input-dialog/

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 input dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.getInteger()
        self.getText()
        self.getDouble()
        self.getChoice()
        
        self.show()
        
    def getInteger(self):
        i, okPressed = QInputDialog.getInt(self, "Get integer","Percentage:", 28, 0, 100, 1)
        if okPressed:
            print(i)

    def getDouble(self):
        d, okPressed = QInputDialog.getDouble(self, "Get double","Value:", 10.50, 0, 100, 10)
        if okPressed:
            print( d)
        
    def getChoice(self):
        items = ("Red","Blue","Green")
        item, okPressed = QInputDialog.getItem(self, "Get item","Color:", items, 0, False)
        if ok and item:
            print(item)

    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Get text","Your name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

########################################
4 kinds of layout
https://realpython.com/python-pyqt-layout/#getting-stocked-with-a-gallery-of-pyqt-layouts


//other layout setting
https://zetcode.com/gui/pyqt5/layout/


#########################################
https://realpython.com/python-pyqt-layout/#getting-stocked-with-a-gallery-of-pyqt-layouts
import sys

from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout Example")
        # Create a QHBoxLayout instance
        layout = QHBoxLayout()
        # Add widgets to the layout
        layout.addWidget(QPushButton("Left-Most"))
        layout.addWidget(QPushButton("Center"), 1)
        layout.addWidget(QPushButton("Right-Most"), 2)
        # Set the layout on the application's window
        self.setLayout(layout)
        print(self.children())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

#########################################

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout Example")
        self.resize(270, 110)
        # Create a QVBoxLayout instance
        layout = QVBoxLayout()
        # Add widgets to the layout
        layout.addWidget(QPushButton("Top"))
        layout.addWidget(QPushButton("Center"))
        layout.addWidget(QPushButton("Bottom"))
        # Set the layout on the application's window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

#########################################

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Example")
        # Create a QGridLayout instance
        layout = QGridLayout()
        # Add widgets to the layout
        layout.addWidget(QPushButton("Button at (0, 0)"), 0, 0)
        layout.addWidget(QPushButton("Button at (0, 1)"), 0, 1)
        layout.addWidget(QPushButton("Button at (0, 2)"), 0, 2)
        layout.addWidget(QPushButton("Button at (1, 0)"), 1, 0)
        layout.addWidget(QPushButton("Button at (1, 1)"), 1, 1)
        layout.addWidget(QPushButton("Button at (1, 2)"), 1, 2)
        layout.addWidget(QPushButton("Button at (2, 0)"), 2, 0)
        layout.addWidget(QPushButton("Button at (2, 1)"), 2, 1)
        layout.addWidget(QPushButton("Button at (2, 2)"), 2, 2)
        # Set the layout on the application's window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

#########################################

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Example")
        # Create a QGridLayout instance
        layout = QGridLayout()
        # Add widgets to the layout
        layout.addWidget(QPushButton("Button at (0, 0)"), 0, 0)
        layout.addWidget(QPushButton("Button at (0, 1)"), 0, 1)
        layout.addWidget(QPushButton("Button Spans two Cols"), 1, 0, 1, 2)
        # Set the layout on the application's window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
#########################################

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QFormLayout,
    QLabel,
    QLineEdit,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout Example")
        self.resize(270, 110)
        # Create a QFormLayout instance
        layout = QFormLayout()
        # Add widgets to the layout
        layout.addRow("Name:", QLineEdit())
        layout.addRow("Job:", QLineEdit())
        emailLabel = QLabel("Email:")
        layout.addRow(emailLabel, QLineEdit())
        # Set the layout on the application's window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

#########################################

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nested Layouts Example")
        # Create an outer layout
        outerLayout = QVBoxLayout()
        # Create a form layout for the label and line edit
        topLayout = QFormLayout()
        # Add a label and a line edit to the form layout
        topLayout.addRow("Some Text:", QLineEdit())
        # Create a layout for the checkboxes
        optionsLayout = QVBoxLayout()
        # Add some checkboxes to the layout
        optionsLayout.addWidget(QCheckBox("Option one"))
        optionsLayout.addWidget(QCheckBox("Option two"))
        optionsLayout.addWidget(QCheckBox("Option three"))
        # Nest the inner layouts into the outer layout
        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(optionsLayout)
        # Set the window's main layout
        self.setLayout(outerLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
#########################################

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QFormLayout,
    QLineEdit,
    QStackedLayout,
    QVBoxLayout,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout Example")
        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Create and connect the combo box to switch between pages
        self.pageCombo = QComboBox()
        self.pageCombo.addItems(["Page 1", "Page 2"])
        self.pageCombo.activated.connect(self.switchPage)
        # Create the stacked layout
        self.stackedLayout = QStackedLayout()
        # Create the first page
        self.page1 = QWidget()
        self.page1Layout = QFormLayout()
        self.page1Layout.addRow("Name:", QLineEdit())
        self.page1Layout.addRow("Address:", QLineEdit())
        self.page1.setLayout(self.page1Layout)
        self.stackedLayout.addWidget(self.page1)
        # Create the second page
        self.page2 = QWidget()
        self.page2Layout = QFormLayout()
        self.page2Layout.addRow("Job:", QLineEdit())
        self.page2Layout.addRow("Department:", QLineEdit())
        self.page2.setLayout(self.page2Layout)
        self.stackedLayout.addWidget(self.page2)
        # Add the combo box and the stacked layout to the top-level layout
        layout.addWidget(self.pageCombo)
        layout.addLayout(self.stackedLayout)

    def switchPage(self):
        self.stackedLayout.setCurrentIndex(self.pageCombo.currentIndex())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

#########################################


import sys

from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTabWidget Example")
        self.resize(270, 110)
        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Create the tab widget with two tabs
        tabs = QTabWidget()
        tabs.addTab(self.generalTabUI(), "General")
        tabs.addTab(self.networkTabUI(), "Network")
        layout.addWidget(tabs)

    def generalTabUI(self):
        """Create the General page UI."""
        generalTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("General Option 1"))
        layout.addWidget(QCheckBox("General Option 2"))
        generalTab.setLayout(layout)
        return generalTab

    def networkTabUI(self):
        """Create the Network page UI."""
        networkTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("Network Option 1"))
        layout.addWidget(QCheckBox("Network Option 2"))
        networkTab.setLayout(layout)
        return networkTab

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


#########################################

import sys

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDialog's Top-Level Layout Example")
        dlgLayout = QVBoxLayout()
        # Create a form layout and add widgets
        formLayout = QFormLayout()
        formLayout.addRow("Name:", QLineEdit())
        formLayout.addRow("Job:", QLineEdit())
        formLayout.addRow("Email:", QLineEdit())
        # Add a button box
        btnBox = QDialogButtonBox()
        btnBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        # Set the layout on the dialog
        dlgLayout.addLayout(formLayout)
        dlgLayout.addWidget(btnBox)
        self.setLayout(dlgLayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())

#########################################

import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QVBoxLayout Example")
        self.resize(270, 110)
        # Create a QVBoxLayout instance
        layout = QVBoxLayout()
        # Add widgets to the layout
        layout.addWidget(QPushButton("Top"))
        layout.addWidget(QPushButton("Center"))
        layout.addWidget(QPushButton("Bottom"))
        layout.addStretch()
        # Set the layout on the application's window
        self.setLayout(layout)

apps = QApplication(sys.argv)

windo = Window()

windo.show()

apps.exec()
sys.exit()
#########################################

import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout Example")
        self.resize(270, 110)
        # Create a QHBoxLayout instance
        layout = QFormLayout()
        # Add widgets to the layout
        layout.setVerticalSpacing(30)
        layout.addRow("Name:", QLineEdit())
        layout.addRow("Job:", QLineEdit())
        emailLabel = QLabel("Email:")
        layout.addRow(emailLabel, QLineEdit())
        # Set the layout on the application's window
        self.setLayout(layout)


apps = QApplication(sys.argv)

windo = Window()

windo.show()

apps.exec()

#########################################
QLabel

      # setting up border
        self.label_2.setStyleSheet("border: 1px solid black;")
  
        # changing the text of label
        self.label_2.setText(new_info)
  
#########################################
reference Listview   QLIstWidget
https://www.geeksforgeeks.org/pyqt5-qlistwidget-python/
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QListWidgetItem


class Ui_MainWindow(QWidget):
	def __init__(self, parent = None):
		super(Ui_MainWindow, self).__init__(parent)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = QWidget()
	listWidget = QListWidget()
	window.setWindowTitle("Demo for QListWidget")

	QListWidgetItem("Geeks", listWidget)
	QListWidgetItem("For", listWidget)
	QListWidgetItem("Geeks", listWidget)

	listWidgetItem = QListWidgetItem("GeeksForGeeks")
	listWidget.addItem(listWidgetItem)
	
	window_layout = QVBoxLayout(window)
	window_layout.addWidget(listWidget)
	window.setLayout(window_layout)

	window.show()

	sys.exit(app.exec_())

#########################################
#keypress on QLineEdit
https://stackoverflow.com/questions/67659834/python-space-key-press-event-not-captured-when-using-qlineedit

table format of acsii code
https://github.com/codito/pyqtkeybind/blob/master/pyqtkeybind/win/keycodes.py


# for class object type definition solo of QLineEdit
import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)

        self.w = LineEdit()
        layout.addWidget(self.w, 0, 0)


class LineEdit(QtWidgets.QLineEdit):

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        super(LineEdit, self).keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_Tab:
            print("Tab Key pressed")

        if event.key() == QtCore.Qt.Key_Space:
            print("Space Key pressed")

        if event.key() == QtCore.Qt.Key_Return:
            print("Return Key pressed")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())


###for main parent keyPress
import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        layout = QtWidgets.QGridLayout()
        self.setLayout(layout)

        self.w = QtWidgets.QLineEdit()
        self.w.textChanged.connect(self.keyPress)
        layout.addWidget(self.w, 0, 0)

    def keyPress(self, key):
        if key[-1] == " ":
            print("Space Key pressed")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())

#########################################
QListWidget
https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QListWidget.html#PySide2.QtWidgets.PySide2.QtWidgets.QListWidget.row

PySide2.QtWidgets.QListWidget.takeItem(row)
Parameters
row – int

Return type
PySide2.QtWidgets.QListWidgetItem

Removes and returns the item from the given row in the list widget; otherwise returns None .

Items removed from a list widget will not be managed by Qt, and will need to be deleted manually.

#burahinlahat ng laman ng Qlist
PySide2.QtWidgets.QListWidget.clear()
Removes all items and selections in the view.

Warning

All items will be permanently deleted.

PySide2.QtWidgets.QListWidget.setSortingEnabled(enable)
Parameters
enable – bool

This property holds whether sorting is enabled.

If this property is true , sorting is enabled for the list; if the property is false, 
sorting is not enabled.

The default value is false.


#########################################
reference site
https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QListWidget.html#PySide2.QtWidgets.PySide2.QtWidgets.QListWidget.count

#inserting in row a value of string
PySide2.QtWidgets.QListWidget.addItem(label)
Parameters
label – str

#inserting in row the value of object QListWidgetItem
PySide2.QtWidgets.QListWidget.addItem(item)
Parameters
item – PySide2.QtWidgets.QListWidgetItem

Inserts the item at the end of the list widget.

Warning

A QListWidgetItem can only be added to a QListWidgetonce. Adding the same QListWidgetItemmultiple 
times to a QListWidget will result in undefined behavior.


para sa i highlight ang target na row
PySide2.QtWidgets.QListWidget.setCurrentRow(row)
Parameters
row – int

This property holds the row of the current item..

Depending on the current selection mode, the row may also be selected.

PySide2.QtWidgets.QListWidget.setCurrentRow(row, command)¶
Parameters
row – int

command – SelectionFlags

Sets the current row to be the given row , using the given command ,

#return ng kung saan nakahiglight ang index position nito
PySide2.QtWidgets.QListWidget.currentRow()
Return type
int

This property holds the row of the current item..

Depending on the current selection mode, the row may also be selected.

            .takeItem(int) isa-isa i delete item sa QListWidget
            .front.clear() delete lahat ng item
#########################################

for reference of QListWidgetItem ang laman ng QListWidget
https://doc.qt.io/qtforpython-5/PySide2/QtCore/Qt.html

#########################################
QListView icon list lang ang supported
reference
https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QListView.html#PySide2.QtWidgets.PySide2.QtWidgets.QListView


#########################################

#documentation of QWidget
https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QWidget.html

#########################################
#reference Qt accesories  the key press and etc..
https://doc.qt.io/qtforpython-5/PySide2/QtCore/Qt.html

important topic:
PySide2.QtCore.Qt.ItemFlag¶
This enum describes the properties of an item:

Constant

Description

Qt.NoItemFlags

It does not have any properties set.

Qt.ItemIsSelectable

It can be selected.

Qt.ItemIsEditable

It can be edited.

Qt.ItemIsDragEnabled

It can be dragged.

Qt.ItemIsDropEnabled

It can be used as a drop target.

Qt.ItemIsUserCheckable

It can be checked or unchecked by the user.

Qt.ItemIsEnabled

The user can interact with the item.

Qt.ItemIsAutoTristate

The item’s state depends on the state of its children. This enables automatic management
 of the state of parent items in QTreeWidget (checked if all children are checked,
 unchecked if all children are unchecked, or partially checked if only some children are checked).

Qt.ItemIsTristate

This enum value is deprecated. Use instead.

Qt.ItemNeverHasChildren

The item never has child items. This is used for optimization purposes only.

Qt.ItemIsUserTristate

The user can cycle through three separate states. This value was added in Qt 5.5.

Note that checkable items need to be given both a suitable set of flags and an initial state,
 indicating whether the item is checked or not. This is handled automatically for model/view 
components, but needs to be explicitly set for instances of QListWidgetItem , QTableWidgetItem 
, and QTreeWidgetItem .

Note that it is undefined behavior to reimplement hasChildren to return true for an index if
 that index has the flag set.


#########################################

font color styles of widget
https://doc.qt.io/qtforpython-5/overviews/stylesheet-examples.html

#########################################
#########################################
#########################################




