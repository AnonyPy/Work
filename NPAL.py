#Launcher v0.1 Code

import urllib.request
import os
import sys
from PyQt5.QtWidgets import QLabel, QAction, qApp, QMainWindow, QWidget, QMessageBox, QPushButton, QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon, QImage, QPalette, QBrush   

class Launcher(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #The background
        background = QImage("BG_Image.jpg")
        palette = QPalette()
        palette.setBrush(10, QBrush(background))
        self.setPalette(palette)
       
        
        #Setup button
        button = QPushButton("SETUP",self)
        button.resize(button.sizeHint())
        button.move(940, 456)
        button.clicked.connect(self.setupEvent)
        button.resize(162,75)

        #Information label
        versionLabel = QLabel("Launcher Version: v0.1",self)
        self.statusBar().addPermanentWidget(versionLabel)

        #Drop down menu
        #Sub menus
        self.optionAct = QAction("&Options")
        self.optionAct.setShortcut("Ctrl+O")
        self.optionAct.setStatusTip("Customize Graphics and Downloads")
        
        exitAct = QAction("&Exit", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("Exit the launcher")
        exitAct.triggered.connect(sys.exit)

        #Menu
        
        menubar = self.menuBar()
        self.fileMenu = menubar.addMenu("&Config")
        self.fileMenu.addAction(self.optionAct)
        self.fileMenu.addAction(exitAct)
        self.fileMenu.menuAction().setStatusTip("Configure the Launcher")

        #The frames dimension on centering
        self.resize(1100,550)
        self.center()
        
        #The frames icon and title and the final command to display the launcher
        self.setWindowTitle("NPA LAUNCHER")
        self.setWindowIcon(QIcon("favourite old photo.png"))
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        

    def setupEvent(self):

        reply = QMessageBox.question(self, "Confirmation",
        "Are you sure you want to install NPA?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            print("Downloading")
            self.setup()

        else:
            print("Declined")
    
    def refreshStatusBar(self):
        self.statusBar().showMessage("Launcher Version: v0.1")
        
    #Install game button command (modified)
    def setup(self):
        path = "NPA"
        if not os.path.exists(path):
            self.statusBar().showMessage("Installing directory 'NPA'")
            os.makedirs(path)
            self.statusBar().showMessage("Installing directory 'Projects'")
            os.makedirs(path+"\Projects")
            self.statusBar().showMessage("Installing directory 'Assests'")
            os.makedirs(path+"\Assests")
            self.statusBar().showMessage("Fetching data from: https://nathanscomputingtestsite.weebly.com")
            #Fetch the download list
            fetch = urllib.request.urlopen("https://nathanscomputingtestsite.weebly.com/uploads/1/1/8/4/118415083/launcher_instructions.txt").read()
            downloads = []
            #Splits text into seperate instructions/names
            self.statusBar().showMessage("Unpackaging instructions")
            for word in (fetch.decode("utf-8")).split():
                downloads.append(word)
            print(downloads)
            #Loops the downloading until it is done
            baseUrl = "https://nathanscomputingtestsite.weebly.com/uploads/1/1/8/4/118415083/"
            for i in range (0, len(downloads), 2):
                self.statusBar().showMessage("Downloading project: "+downloads[i+1][1:])
                urllib.request.urlretrieve(baseUrl+downloads[i], "NPA\Projects"+downloads[i+1])
                self.statusBar().showMessage("Project: "+downloads[i+1][1:]+ " installed correctly")
            self.statusBar().showMessage("NPA Install sucessfully completed")
            
        else:
            reply = QMessageBox.question(self, "Error",
        "'NPA' Launcher Files have been found, if you still want to setup the program you must delete it", QMessageBox.Ok)

if __name__ == "__main__":    
    executable = QApplication(sys.argv)
    launcher = Launcher()
    sys.exit(executable.exec_())
