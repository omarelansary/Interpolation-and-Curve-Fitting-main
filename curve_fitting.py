# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'curve fitting3.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1270, 770)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Signal_graphicsView_2 = PlotWidget(self.centralwidget)
        self.Signal_graphicsView_2.setObjectName("Signal_graphicsView_2")
        self.verticalLayout.addWidget(self.Signal_graphicsView_2)
        self.gridLayout.addLayout(self.verticalLayout, 5, 0, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout.addWidget(self.line_8, 7, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.EfficacyLayout = QtWidgets.QHBoxLayout()
        self.EfficacyLayout.setObjectName("EfficacyLayout")
        self.Efficacy_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Efficacy_label.setFont(font)
        self.Efficacy_label.setWhatsThis("")
        self.Efficacy_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Efficacy_label.setObjectName("Efficacy_label")
        self.EfficacyLayout.addWidget(self.Efficacy_label)
        spacerItem = QtWidgets.QSpacerItem(57, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.EfficacyLayout.addItem(spacerItem)
        self.Efficacy_Slider = QtWidgets.QSlider(self.centralwidget)
        self.Efficacy_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Efficacy_Slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Efficacy_Slider.setTickInterval(10)
        self.Efficacy_Slider.setObjectName("Efficacy_Slider")
        self.EfficacyLayout.addWidget(self.Efficacy_Slider)
        self.Efficacy_lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Efficacy_lcdNumber.setFont(font)
        self.Efficacy_lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Efficacy_lcdNumber.setObjectName("Efficacy_lcdNumber")
        self.EfficacyLayout.addWidget(self.Efficacy_lcdNumber)
        self.verticalLayout_2.addLayout(self.EfficacyLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.Chunk_Num_Layout = QtWidgets.QHBoxLayout()
        self.Chunk_Num_Layout.setObjectName("Chunk_Num_Layout")
        self.Chunks_Num_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Chunks_Num_label.setFont(font)
        self.Chunks_Num_label.setObjectName("Chunks_Num_label")
        self.Chunk_Num_Layout.addWidget(self.Chunks_Num_label)
        self.Chunks_Num_Slider = QtWidgets.QSlider(self.centralwidget)
        self.Chunks_Num_Slider.setMaximum(100)
        self.Chunks_Num_Slider.setMinimum(1)        
        self.Chunks_Num_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Chunks_Num_Slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Chunks_Num_Slider.setTickInterval(10)
        self.Chunks_Num_Slider.setObjectName("Chunks_Num_Slider")
        self.Chunk_Num_Layout.addWidget(self.Chunks_Num_Slider)
        self.Chunks_lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.Chunks_lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Chunks_lcdNumber.setProperty("intValue", 1)
        self.Chunks_lcdNumber.setObjectName("Chunks_lcdNumber")
        self.Chunk_Num_Layout.addWidget(self.Chunks_lcdNumber)
        self.verticalLayout_2.addLayout(self.Chunk_Num_Layout)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.Poly_Layout = QtWidgets.QHBoxLayout()
        self.Poly_Layout.setObjectName("Poly_Layout")
        self.Polynomial_Degree_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Polynomial_Degree_label.setFont(font)
        self.Polynomial_Degree_label.setObjectName("Polynomial_Degree_label")
        self.Poly_Layout.addWidget(self.Polynomial_Degree_label)
        self.Polynomial_Degree_Slider = QtWidgets.QSlider(self.centralwidget)
        self.Polynomial_Degree_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Polynomial_Degree_Slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.Polynomial_Degree_Slider.setTickInterval(10)
        self.Polynomial_Degree_Slider.setObjectName("Polynomial_Degree_Slider")
        self.Poly_Layout.addWidget(self.Polynomial_Degree_Slider)
        self.Polynomial_Degree_lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.Polynomial_Degree_lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.Polynomial_Degree_lcdNumber.setObjectName("Polynomial_Degree_lcdNumber")
        self.Poly_Layout.addWidget(self.Polynomial_Degree_lcdNumber)
        self.verticalLayout_2.addLayout(self.Poly_Layout)
        self.gridLayout.addLayout(self.verticalLayout_2, 7, 0, 1, 1)
        self.Signal_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Signal_label.setFont(font)
        self.Signal_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Signal_label.setObjectName("Signal_label")
        self.gridLayout.addWidget(self.Signal_label, 4, 0, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 5, 2, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout.addWidget(self.line_7, 5, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Overlaping_label = QtWidgets.QLabel(self.centralwidget)
        self.Overlaping_label.setObjectName("Overlaping_label")
        self.horizontalLayout_6.addWidget(self.Overlaping_label)
        self.Overlaping_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.Overlaping_spinBox.setObjectName("Overlaping_spinBox")
        self.horizontalLayout_6.addWidget(self.Overlaping_spinBox)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.CMap_label = QtWidgets.QLabel(self.centralwidget)
        self.CMap_label.setObjectName("CMap_label")
        self.horizontalLayout_5.addWidget(self.CMap_label)
        self.CMap_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.CMap_comboBox.setObjectName("CMap_comboBox")
        self.CMap_comboBox.addItem("")
        self.CMap_comboBox.addItem("")
        self.CMap_comboBox.addItem("")
        self.CMap_comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.CMap_comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Xaxis_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.Xaxis_groupBox.setObjectName("Xaxis_groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Xaxis_groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Xaxis_Polynomial_radioButton = QtWidgets.QRadioButton(self.Xaxis_groupBox)
        self.Xaxis_Polynomial_radioButton.setObjectName("Xaxis_Polynomial_radioButton")
        self.gridLayout_2.addWidget(self.Xaxis_Polynomial_radioButton, 0, 1, 1, 1)
        self.Xaxis_NumofChunks_radioButton = QtWidgets.QRadioButton(self.Xaxis_groupBox)
        self.Xaxis_NumofChunks_radioButton.setObjectName("Xaxis_NumofChunks_radioButton")
        self.gridLayout_2.addWidget(self.Xaxis_NumofChunks_radioButton, 0, 2, 1, 1)
        self.Xaxis_Overlap_radioButton = QtWidgets.QRadioButton(self.Xaxis_groupBox)
        self.Xaxis_Overlap_radioButton.setObjectName("Xaxis_Overlap_radioButton")
        self.gridLayout_2.addWidget(self.Xaxis_Overlap_radioButton, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.Xaxis_groupBox, 0, 0, 1, 1)
        self.Yaxis_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.Yaxis_groupBox.setObjectName("Yaxis_groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Yaxis_groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Yaxis_Overlap_radioButton = QtWidgets.QRadioButton(self.Yaxis_groupBox)
        self.Yaxis_Overlap_radioButton.setObjectName("Yaxis_Overlap_radioButton")
        self.gridLayout_3.addWidget(self.Yaxis_Overlap_radioButton, 0, 0, 1, 1)
        self.Yaxis_NumofChunks_radioButton = QtWidgets.QRadioButton(self.Yaxis_groupBox)
        self.Yaxis_NumofChunks_radioButton.setObjectName("Yaxis_NumofChunks_radioButton")
        self.gridLayout_3.addWidget(self.Yaxis_NumofChunks_radioButton, 0, 2, 1, 1)
        self.Yaxis_Polynomial_radioButton = QtWidgets.QRadioButton(self.Yaxis_groupBox)
        self.Yaxis_Polynomial_radioButton.setObjectName("Yaxis_Polynomial_radioButton")
        self.gridLayout_3.addWidget(self.Yaxis_Polynomial_radioButton, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.Yaxis_groupBox, 1, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Overlap_LineEdit_label = QtWidgets.QLabel(self.centralwidget)
        self.Overlap_LineEdit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Overlap_LineEdit_label.setObjectName("Overlap_LineEdit_label")
        self.verticalLayout_4.addWidget(self.Overlap_LineEdit_label)
        self.Overlap_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Overlap_lineEdit.setObjectName("Overlap_lineEdit")
        self.verticalLayout_4.addWidget(self.Overlap_lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.PolynomialDegree_LineEdit_label = QtWidgets.QLabel(self.centralwidget)
        self.PolynomialDegree_LineEdit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.PolynomialDegree_LineEdit_label.setObjectName("PolynomialDegree_LineEdit_label")
        self.verticalLayout_5.addWidget(self.PolynomialDegree_LineEdit_label)
        self.PolynomiaDegreelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PolynomiaDegreelineEdit.setObjectName("PolynomiaDegreelineEdit")
        self.verticalLayout_5.addWidget(self.PolynomiaDegreelineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.NumofChunks_lineEdit_label = QtWidgets.QLabel(self.centralwidget)
        self.NumofChunks_lineEdit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.NumofChunks_lineEdit_label.setObjectName("NumofChunks_lineEdit_label")
        self.verticalLayout_6.addWidget(self.NumofChunks_lineEdit_label)
        self.NumofChunks_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NumofChunks_lineEdit.setObjectName("NumofChunks_lineEdit")
        self.verticalLayout_6.addWidget(self.NumofChunks_lineEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_3.addWidget(self.line_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Start_pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Start_pushButton.sizePolicy().hasHeightForWidth())
        self.Start_pushButton.setSizePolicy(sizePolicy)
        self.Start_pushButton.setMinimumSize(QtCore.QSize(92, 0))
        self.Start_pushButton.setSizeIncrement(QtCore.QSize(78, 0))
        self.Start_pushButton.setObjectName("Start_pushButton")
        self.horizontalLayout_4.addWidget(self.Start_pushButton)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_4.addWidget(self.progressBar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_3, 7, 4, 1, 1)
        self.ErrorLcd_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ErrorLcd_label.setFont(font)
        self.ErrorLcd_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorLcd_label.setObjectName("ErrorLcd_label")
        self.gridLayout.addWidget(self.ErrorLcd_label, 0, 4, 1, 1)
        self.Error_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Error_label.setFont(font)
        self.Error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Error_label.setObjectName("Error_label")
        self.gridLayout.addWidget(self.Error_label, 4, 4, 1, 1)
        self.Error_graphicsView = PlotWidget(self.centralwidget)
        self.Error_graphicsView.setObjectName("Error_graphicsView")
        self.gridLayout.addWidget(self.Error_graphicsView, 5, 4, 1, 1)
        self.Latex_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.Latex_label.setFont(font)
        self.Latex_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Latex_label.setObjectName("Latex_label")
        self.gridLayout.addWidget(self.Latex_label, 0, 0, 1, 1)
        self.Error_lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.Error_lcdNumber.setObjectName("Error_lcdNumber")
        self.gridLayout.addWidget(self.Error_lcdNumber, 1, 4, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 5, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 7, 2, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 8, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 6, 4, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout.addWidget(self.line_10, 3, 0, 1, 1)
        self.Polynomial_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Polynomial_textBrowser.sizePolicy().hasHeightForWidth())
        self.Polynomial_textBrowser.setSizePolicy(sizePolicy)
        self.Polynomial_textBrowser.setMinimumSize(QtCore.QSize(0, 37))
        self.Polynomial_textBrowser.setMaximumSize(QtCore.QSize(16777215, 35))
        self.Polynomial_textBrowser.setObjectName("Polynomial_textBrowser")
        self.gridLayout.addWidget(self.Polynomial_textBrowser, 1, 0, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout.addWidget(self.line_11, 2, 4, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1270, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Efficacy_label.setText(_translate("MainWindow", "Efficacy"))
        self.Chunks_Num_label.setText(_translate("MainWindow", "Number of chunks"))
        self.Polynomial_Degree_label.setText(_translate("MainWindow", "Polynomial Degree"))
        self.Signal_label.setText(_translate("MainWindow", "Signal"))
        self.Overlaping_label.setText(_translate("MainWindow", "Overlaping"))
        self.CMap_label.setText(_translate("MainWindow", "C-Map"))
        self.CMap_comboBox.setItemText(0, _translate("MainWindow", "New Item"))
        self.CMap_comboBox.setItemText(1, _translate("MainWindow", "New Item"))
        self.CMap_comboBox.setItemText(2, _translate("MainWindow", "New Item"))
        self.CMap_comboBox.setItemText(3, _translate("MainWindow", "New Item"))
        self.Xaxis_groupBox.setTitle(_translate("MainWindow", "X-axis"))
        self.Xaxis_Polynomial_radioButton.setText(_translate("MainWindow", "Polynomial Degree"))
        self.Xaxis_NumofChunks_radioButton.setText(_translate("MainWindow", "Num. of Chunks"))
        self.Xaxis_Overlap_radioButton.setText(_translate("MainWindow", "Overlap"))
        self.Yaxis_groupBox.setTitle(_translate("MainWindow", "Y-axis"))
        self.Yaxis_Overlap_radioButton.setText(_translate("MainWindow", "Overlap"))
        self.Yaxis_NumofChunks_radioButton.setText(_translate("MainWindow", "Num. of Chunks"))
        self.Yaxis_Polynomial_radioButton.setText(_translate("MainWindow", "Polynomial Degree"))
        self.Overlap_LineEdit_label.setText(_translate("MainWindow", "Overlap"))
        self.PolynomialDegree_LineEdit_label.setText(_translate("MainWindow", "Polynomial Degree"))
        self.NumofChunks_lineEdit_label.setText(_translate("MainWindow", "Num of Chunks"))
        self.Start_pushButton.setText(_translate("MainWindow", "Start"))
        self.ErrorLcd_label.setText(_translate("MainWindow", "Error%"))
        self.Error_label.setText(_translate("MainWindow", "Error"))
        self.Latex_label.setText(_translate("MainWindow", "Latex"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
# import matplotlib.pyplot as plt
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())