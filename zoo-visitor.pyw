# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import zoo_model


class ZooMainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Window)
        self.setWindowTitle("Zoo Visitor")
        self.tv = QtWidgets.QTreeView()
        self.sti = QtGui.QStandardItemModel()
        self.tv.setHeaderHidden(True)

        self.rootitem1 = QtGui.QStandardItem('127.0.0.1:2181')

        self.model = zoo_model.ZooModel()
        # self.model.initModel()

        self.label = QtWidgets.QLabel("host:")
        self.label.setFont(QtGui.QFont('Arial', 9))

        self.zooHost = QtWidgets.QLineEdit("127.0.0.1:2181")
        self.zooHost.setFont(QtGui.QFont('Arial', 9))

        self.connectBtn = QtWidgets.QPushButton("Connect")

        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.zooHost)
        hbox.addWidget(self.connectBtn)

        vbox = QtWidgets.QVBoxLayout()

        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        vbox.addWidget(self.tv)
        self.setLayout(vbox)

        self.connectBtn.clicked.connect(self.setNewConnect)

    def setNewConnect(self):
        self.rootitem1.removeRows(0, self.rootitem1.rowCount())
        self.rootitem1.setText(self.zooHost.text())
        self.initModel(self.zooHost.text())

    def appendChilds(self, row, model):
        for child in model.childs:
            item = QtGui.QStandardItem(child.name)
            row.appendRow(item)
            self.appendChilds(item, child)

    def initModel(self, host):
        self.model.initModel(host)
        for node in self.model.model:
            item1 = QtGui.QStandardItem(node.name)
            self.appendChilds(item1, node)
            self.rootitem1.appendRow([item1])

        self.sti.removeRows(1, len(self.model.model))
        self.sti.appendRow([self.rootitem1])
        self.sti.setHorizontalHeaderLabels([host])
        self.tv.setModel(self.sti)


app = QtWidgets.QApplication(sys.argv)
window = ZooMainWindow()
window.show()
sys.exit(app.exec_())
