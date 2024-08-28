from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
import main


class Ui_MainWindow(object):

    def __init__(self):
        self.wavPath = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 304)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(40, 50, 22, 171))
        self.verticalSlider.setMinimum(-60)
        self.verticalSlider.setMaximum(0)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.verticalSlider.valueChanged.connect(self.slider1_moved)
        self.verticalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_2.setGeometry(QtCore.QRect(130, 50, 22, 171))
        self.verticalSlider_2.setMinimum(-60)
        self.verticalSlider_2.setMaximum(0)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalSlider_2.valueChanged.connect(self.slider2_moved)
        self.verticalSlider_3 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_3.setGeometry(QtCore.QRect(220, 50, 22, 171))
        self.verticalSlider_3.setMinimum(-60)
        self.verticalSlider_3.setMaximum(0)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.verticalSlider_3.valueChanged.connect(self.slider3_moved)
        self.verticalSlider_4 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_4.setGeometry(QtCore.QRect(310, 50, 22, 171))
        self.verticalSlider_4.setMinimum(-60)
        self.verticalSlider_4.setMaximum(0)
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.verticalSlider_4.valueChanged.connect(self.slider4_moved)
        self.verticalSlider_5 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_5.setGeometry(QtCore.QRect(400, 50, 22, 171))
        self.verticalSlider_5.setMinimum(-60)
        self.verticalSlider_5.setMaximum(0)
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.verticalSlider_5.valueChanged.connect(self.slider5_moved)
        self.verticalSlider_6 = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider_6.setGeometry(QtCore.QRect(490, 50, 22, 171))
        self.verticalSlider_6.setMinimum(-60)
        self.verticalSlider_6.setMaximum(0)
        self.verticalSlider_6.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_6.setObjectName("verticalSlider_6")
        self.verticalSlider_6.valueChanged.connect(self.slider6_moved)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(560, 50, 131, 21))
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")

        self.button_browse = QtWidgets.QPushButton(self.centralwidget)
        self.button_browse.setGeometry(QtCore.QRect(560, 80, 131, 28))
        self.button_browse.setObjectName("button_browse")
        self.button_browse.clicked.connect(self.browseFiles)

        self.button_play = QtWidgets.QPushButton(self.centralwidget)
        self.button_play.setGeometry(QtCore.QRect(560, 210, 131, 28))
        self.button_play.setObjectName("button_play")
        self.button_play.setEnabled(False)
        self.button_play.clicked.connect(self.playAudio)

        self.label_0_100 = QtWidgets.QLabel(self.centralwidget)
        self.label_0_100.setGeometry(QtCore.QRect(30, 230, 41, 16))
        self.label_0_100.setObjectName("label_0_100")
        self.label_101_722 = QtWidgets.QLabel(self.centralwidget)
        self.label_101_722.setGeometry(QtCore.QRect(120, 230, 61, 16))
        self.label_101_722.setObjectName("label_101_722")
        self.label_723_1966 = QtWidgets.QLabel(self.centralwidget)
        self.label_723_1966.setGeometry(QtCore.QRect(200, 230, 71, 16))
        self.label_723_1966.setObjectName("label_723_1966")
        self.label_1967_4453 = QtWidgets.QLabel(self.centralwidget)
        self.label_1967_4453.setGeometry(QtCore.QRect(290, 230, 71, 16))
        self.label_1967_4453.setScaledContents(False)
        self.label_1967_4453.setWordWrap(False)
        self.label_1967_4453.setObjectName("label_1967_4453")
        self.label_4454_9428 = QtWidgets.QLabel(self.centralwidget)
        self.label_4454_9428.setGeometry(QtCore.QRect(380, 230, 71, 16))
        self.label_4454_9428.setObjectName("label_4454_9428")
        self.label_9429_21900 = QtWidgets.QLabel(self.centralwidget)
        self.label_9429_21900.setGeometry(QtCore.QRect(470, 230, 81, 16))
        self.label_9429_21900.setObjectName("label_9429_21900")
        self.label_0_100_value = QtWidgets.QLabel(self.centralwidget)
        self.label_0_100_value.setGeometry(QtCore.QRect(40, 26, 31, 20))
        self.label_0_100_value.setObjectName("label_0_100_value")
        self.label_101_722_value = QtWidgets.QLabel(self.centralwidget)
        self.label_101_722_value.setGeometry(QtCore.QRect(130, 19, 31, 31))
        self.label_101_722_value.setObjectName("label_101_722_value")
        self.label_723_1966_value = QtWidgets.QLabel(self.centralwidget)
        self.label_723_1966_value.setGeometry(QtCore.QRect(220, 20, 31, 31))
        self.label_723_1966_value.setObjectName("label_723_1966_value")
        self.label_1967_4453_value = QtWidgets.QLabel(self.centralwidget)
        self.label_1967_4453_value.setGeometry(QtCore.QRect(310, 20, 31, 31))
        self.label_1967_4453_value.setObjectName("label_1967_4453_value")
        self.label_4454_9428_value = QtWidgets.QLabel(self.centralwidget)
        self.label_4454_9428_value.setGeometry(QtCore.QRect(400, 20, 31, 31))
        self.label_4454_9428_value.setObjectName("label_4454_9428_value")
        self.label_9429_21900_value = QtWidgets.QLabel(self.centralwidget)
        self.label_9429_21900_value.setGeometry(QtCore.QRect(490, 20, 31, 31))
        self.label_9429_21900_value.setObjectName("label_9429_21900_value")

        self.checkBox_is_bih = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_is_bih.setGeometry(QtCore.QRect(560, 120, 111, 20))
        self.checkBox_is_bih.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.checkBox_is_bih.setObjectName("checkBox_is_bih")
        self.checkBox_is_bih.stateChanged.connect(self.changeFilterType)

        self.checkBox_reverb = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_reverb.setGeometry(QtCore.QRect(560, 150, 111, 20))
        self.checkBox_reverb.setObjectName("checkBox_reverb")

        self.checkBox_clipping = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_clipping.setGeometry(QtCore.QRect(560, 180, 111, 20))
        self.checkBox_clipping.setObjectName("checkBox_clipping")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Equalizer"))
        self.button_play.setText(_translate("MainWindow", "Play"))
        self.button_browse.setText(_translate("MainWindow", "Browse"))
        self.label_0_100.setText(_translate("MainWindow", "0-100"))
        self.label_101_722.setText(_translate("MainWindow", "101-722"))
        self.label_723_1966.setText(_translate("MainWindow", "723-1966"))
        self.label_1967_4453.setText(_translate("MainWindow", "1967-4453"))
        self.label_4454_9428.setText(_translate("MainWindow", "4454-9428"))
        self.label_9429_21900.setText(_translate("MainWindow", "9429-21900"))
        self.label_0_100_value.setText(_translate("MainWindow", "0"))
        self.label_101_722_value.setText(_translate("MainWindow", "0"))
        self.label_723_1966_value.setText(_translate("MainWindow", "0"))
        self.label_1967_4453_value.setText(_translate("MainWindow", "0"))
        self.label_4454_9428_value.setText(_translate("MainWindow", "0"))
        self.label_9429_21900_value.setText(_translate("MainWindow", "0"))

        self.checkBox_is_bih.setText(_translate("MainWindow", "Bih filter"))
        self.checkBox_reverb.setText(_translate("MainWindow", "Reverberation"))
        self.checkBox_clipping.setText(_translate("MainWindow", "Clipping"))

    def browseFiles(self):
        wavFile = QFileDialog.getOpenFileName(None, 'Open .wav file', './audio/', 'WAV files (*.wav)')
        if wavFile[0] == '':
            return
        main.wavPath = wavFile[0]

        fileNameSplit = wavFile[0].split('/')
        self.lineEdit.setText(fileNameSplit[len(fileNameSplit) - 1])
        self.button_play.setEnabled(True)

    def playAudio(self):
        main.playAudio()
        if main.isPlaying:
            self.button_play.setText("Stop")
            self.button_browse.setEnabled(False)
        else:
            self.button_play.setText("Play")
            self.button_browse.setEnabled(True)

    def changeFilterType(self):
        if self.checkBox_is_bih.isChecked():
            main.isKih = False
        else:
            main.isKih = True

    def slider1_moved(self):
        self.label_0_100_value.setText(str(self.verticalSlider.value()))
        main.dbGainValues[0] = self.verticalSlider.value()

    def slider2_moved(self):
        self.label_101_722_value.setText(str(self.verticalSlider_2.value()))
        main.dbGainValues[1] = self.verticalSlider_2.value()

    def slider3_moved(self):
        self.label_723_1966_value.setText(str(self.verticalSlider_3.value()))
        main.dbGainValues[2] = self.verticalSlider_3.value()

    def slider4_moved(self):
        self.label_1967_4453_value.setText(str(self.verticalSlider_4.value()))
        main.dbGainValues[3] = self.verticalSlider_4.value()

    def slider5_moved(self):
        self.label_4454_9428_value.setText(str(self.verticalSlider_5.value()))
        main.dbGainValues[4] = self.verticalSlider_5.value()

    def slider6_moved(self):
        self.label_9429_21900_value.setText(str(self.verticalSlider_6.value()))
        main.dbGainValues[5] = self.verticalSlider_6.value()


