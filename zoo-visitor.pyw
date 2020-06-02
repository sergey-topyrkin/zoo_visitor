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

        # self.tv.setHeaderHidden(True)
        self.rootitem1 = QtGui.QStandardItem('127.0.0.1:2181')
        self.rootitem2 = QtGui.QStandardItem('')

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

        # self.tv.setSelectionModel(QtCore.QItemSelectionModel())
        self.tv.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

    def selectPath(self, prevIndex, newIndex):
        indexes = newIndex.indexes()
        for ind in indexes:
            print('-----> ' + ind.data())

    def setNewConnect(self):
        self.rootitem1.removeRows(0, self.rootitem1.rowCount())
        self.rootitem1.setText(self.zooHost.text())
        self.initModel(self.zooHost.text())

    def appendChilds(self, row, model):
        for child in model.childs:
            item = QtGui.QStandardItem(child.name)
            data = ""
            if(child.value[0] != None):
                data = child.value[0].decode('UTF-8')
            item2 = QtGui.QStandardItem(data)
            row.appendRow([item, item2])
            self.appendChilds(item, child)

    def initModel(self, host):
        self.model.initModel(host)
        for node in self.model.model:
            item1 = QtGui.QStandardItem(node.name)
            data = ""
            if(node.value[0] != None):
                data = node.value[0].decode('UTF-8')
            item2 = QtGui.QStandardItem(data)
            self.appendChilds(item1, node)
            self.rootitem1.appendRow([item1, item2])

        self.sti.removeRows(1, len(self.model.model))
        self.sti.appendRow([self.rootitem1])
        self.sti.appendRow([self.rootitem2])
        self.sti.setHorizontalHeaderLabels([host, 'data'])
        self.tv.setModel(self.sti)
        self.tv.setSelectionModel(QtCore.QItemSelectionModel())
        self.tv.selectionModel().selectionChanged.connect(self.selectPath)


app = QtWidgets.QApplication(sys.argv)
window = ZooMainWindow()
window.show()
sys.exit(app.exec_())
