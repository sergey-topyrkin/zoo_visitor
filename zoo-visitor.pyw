# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtWidgets, QtCore
import sys
#import zoo_model
import zoo_tree
import zoo_shell
import zoo_command


class ZooMainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Window)
        self.setWindowTitle("Zoo Visitor")
        self.zoo_view = zoo_tree.ZooTreeView()
        self.zoo_shell = zoo_shell.ZooShellEdit()
        self.zoo_shell.mainWindow = self
        self.splitter = QtWidgets.QSplitter()

        self.label = QtWidgets.QLabel("host:")
        self.label.setFont(QtGui.QFont('Arial', 9))

        self.zooHost = QtWidgets.QLineEdit("127.0.0.1:2181")
        self.zooHost.setFont(QtGui.QFont('Arial', 9))

        self.connectBtn = QtWidgets.QPushButton("Connect")
        self.connectBtn.setFont(QtGui.QFont('Arial', 9))

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.zooHost)
        hbox.addWidget(self.connectBtn)

        vbox = QtWidgets.QVBoxLayout()

        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.addWidget(self.zoo_view)
        self.splitter.addWidget(self.zoo_shell)

        # vbox.addWidget(self.zoo_view)
        vbox.addWidget(self.splitter)

        # self.toolBar = QtWidgets.QToolBar()
        # self.toolBar.addAction("Run")
        # vbox.addWidget(self.toolBar)

        self.setLayout(vbox)

        self.connectBtn.clicked.connect(self.setNewConnect)

    def setNewConnect(self):
        host = self.zooHost.text()
        self.zoo_view.setNewConnect(host)
        self.zoo_shell.connect(host)

    def shellCommand(self, command):
        cli_command = zoo_command.ZooCommand(command)
        if cli_command.error:
            self.zoo_shell.printError(cli_command.error)
        else:
            self.zoo_view.model.executeCommand(cli_command)
            self.zoo_shell.printResult()


app = QtWidgets.QApplication(sys.argv)
window = ZooMainWindow()
window.resize(1200, 600)
window.show()
sys.exit(app.exec_())
