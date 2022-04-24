import sys #dddd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import pandas as pd
import pyqtgraph
from pyqtgraph import PlotWidget
from curve_fitting import Ui_MainWindow
import qdarkstyle
from math import ceil

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ahmed=0 #this is how we initialize a variable
        self.xaxisfromcsv=[]
        self.yaxisfromcsv=[]
        self.chunkSize=1000
        self.ploynomialOrder=1

        #Trigering and button to function connection
        self.ui.actionOpen.triggered.connect(self.Browsefile)
        self.ui.Chunks_Num_Slider.valueChanged[int].connect(self.changechunksize)
        self.ui.Polynomial_Degree_Slider.valueChanged[int].connect(self.changePloynomialordervalue)

    def Browsefile(self):
        self.path = QFileDialog.getOpenFileName(self, 'Open a file', '') #open browse window
        if self.path != ('', ''):
            self.data = self.path[0]
            print("File path: " + self.data)

        self.col= pd.read_csv(self.data)
        self.tempxaxis=self.col.iloc[:,0:1].values #dool metala3ly array 3aml keda [[1],[2],[3],....] list of lists
        self.tempyaxis=self.col.iloc[:,1:2].values
        for i in range(len(self.tempxaxis)): #keda ba2a list of elements
            self.xaxisfromcsv.append(self.tempxaxis[i,0])
            self.yaxisfromcsv.append(self.tempyaxis[i,0])
        self.ui.Signal_graphicsView_2.plot(self.xaxisfromcsv,self.yaxisfromcsv)

    def plotdottedline(self):
        self.ui.Signal_graphicsView_2.clear()
        self.ui.Signal_graphicsView_2.plot(self.xaxisfromcsv,self.yaxisfromcsv)
        for i in range(0,len(self.xaxisfromcsv)-1,self.chunkSize):
            tempxaxis=self.xaxisfromcsv[i:i+self.chunkSize-1]
            tempyaxis=self.yaxisfromcsv[i:i+self.chunkSize-1]
            self.ui.Signal_graphicsView_2.plot(tempxaxis,tempyaxis,pen=None ,symbol="o", symbolsize=0.5, symbolBrush=('b'))

    def changechunksize(self):
        self.ui.Chunks_lcdNumber.display(self.ui.Chunks_Num_Slider.value())
        self.chunkSize= ceil(len(self.xaxisfromcsv)/self.ui.Chunks_Num_Slider.value())
        print(self.chunkSize)
        self.plotdottedline()

    def changePloynomialordervalue(self):
        self.ui.Polynomial_Degree_lcdNumber.display(self.ui.Polynomial_Degree_Slider.value())
        self.ploynomialOrder=self.ui.Polynomial_Degree_Slider.value()
        self.plotdottedline()    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
