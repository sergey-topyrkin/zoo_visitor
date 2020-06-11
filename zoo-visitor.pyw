# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtWidgets, QtCore
import sys
#import zoo_model
import zoo_tree


class ZooMainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Window)
        self.setWindowTitle("Zoo Visitor")
        self.zoo_view = zoo_tree.ZooTreeView()

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
        vbox.addWidget(self.zoo_view)
        self.setLayout(vbox)

        self.connectBtn.clicked.connect(self.setNewConnect)

    def setNewConnect(self):
        self.zoo_view.setNewConnect(self.zooHost.text())


app = QtWidgets.QApplication(sys.argv)
window = ZooMainWindow()
window.show()
sys.exit(app.exec_())
