# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtWidgets, QtCore
import zoo_model


class ZooTreeView(QtWidgets.QTreeView):
    def __init__(self, parent=None):
        QtWidgets.QTreeView.__init__(self, parent)
        self.sti = QtGui.QStandardItemModel()
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        self.model = zoo_model.ZooModel()
        self.rootitem = QtGui.QStandardItem('127.0.0.1:2181')

    def initModel(self, host):
        nodes = self.model.initModel(host)

        for node in nodes:
            data = ""
            if(node.value[0] != None):
                data = node.value[0].decode('UTF-8')
                self.appendChildRow(self.rootitem, node.name, data)

        self.sti.removeRows(1, self.rootitem.rowCount())
        self.sti.appendRow([self.rootitem])
        self.sti.setHorizontalHeaderLabels([host, 'data'])
        self.setModel(self.sti)
        self.setSelectionModel(QtCore.QItemSelectionModel())
        self.selectionModel().selectionChanged.connect(self.selectPath)
        self.expanded.connect(self.itemExpand)
        self.sti.itemChanged.connect(self.itemChanged)

    def itemChanged(self, changedItem):
        changedData = changedItem.text()
        parentIndex = self.sti.indexFromItem(changedItem.parent())
        index = self.sti.index(changedItem.row(), 0, parentIndex)
        node = self.sti.itemFromIndex(index).text()
        self.model.updateNodeData(node, changedData.encode())

    def appendChildRow(self, row, row_name, row_data):
        appended = QtGui.QStandardItem(row_name)
        appended.setData("model", QtCore.Qt.UserRole + 1)
        appended.appendRow(
            [QtGui.QStandardItem(""), QtGui.QStandardItem("")])
        row.appendRow([appended,
                       QtGui.QStandardItem(row_data)])

    def itemExpand(self, modelIndex):
        self.setCursor(QtCore.Qt.WaitCursor)
        modelData = modelIndex.data(QtCore.Qt.UserRole + 1)
        currItem = self.sti.itemFromIndex(modelIndex)

        if(modelData == "model" and currItem.hasChildren()):
            currItem.removeRows(0, currItem.rowCount())
            childs = self.model.get_childs(currItem.text())
            for node in childs:
                data = ""
                if(node.value[0] != None):
                    data = node.value[0].decode('UTF-8')
                    self.appendChildRow(currItem, node.name, data)
        self.unsetCursor()

    def setNewConnect(self, host):
        self.rootitem.removeRows(0, self.rootitem.rowCount())
        self.rootitem.setText(host)
        self.initModel(host)

    def selectPath(self, prevIndex, newIndex):
        indexes = prevIndex.indexes()
        for ind in indexes:
            print(ind.data())

    def contextMenuEvent(self, event):
        dropIndex = self.indexAt(event.pos())
        if(dropIndex.isValid()):
            menu = QtWidgets.QMenu(self)
            renameNode = menu.addAction("Rename")
            deleteNode = menu.addAction("Delete")
            addNode = menu.addAction("Add")
            action = menu.exec_(self.mapToGlobal(event.pos()))
