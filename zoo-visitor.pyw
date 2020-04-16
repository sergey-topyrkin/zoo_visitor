# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtWidgets
import sys
import zoo_model


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QStandardItemModel")
tv = QtWidgets.QTreeView(parent=window)
sti = QtGui.QStandardItemModel(parent=window)

rootitem1 = QtGui.QStandardItem('QAbstractItemView')
rootitem2 = QtGui.QStandardItem('Базовый класс')

model = zoo_model.ZooModel()
model.initModel()

for node in model.model:
    item1 = QtGui.QStandardItem(node.name)
    rootitem1.appendRow([item1, item1])

# rootitem1 = QtGui.QStandardItem('QAbstractItemView')
# rootitem2 = QtGui.QStandardItem('Базовый класс')
# item1 = QtGui.QStandardItem(s)
# item2 = QtGui.QStandardItem('Список')
# rootitem1.appendRow([item1, item2])
# item1 = QtGui.QStandardItem('QTableView')
# item2 = QtGui.QStandardItem('Таблица')
# rootitem1.appendRow([item1, item2])
# item1 = QtGui.QStandardItem('QTreeView')
# item2 = QtGui.QStandardItem('Иерархический список')
# rootitem1.appendRow([item1, item2])
sti.appendRow([rootitem1, rootitem2])

sti.setHorizontalHeaderLabels(['Класс', 'Описание'])
tv.setModel(sti)
tv.setColumnWidth(0, 170)
tv.resize(400, 100)
window.show()
sys.exit(app.exec_())
# -*- coding: utf-8 -*-
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("QStandardItemModel")
tv = QtWidgets.QTreeView(parent=window)
sti = QtGui.QStandardItemModel(parent=window)
rootitem1 = QtGui.QStandardItem('QAbstractItemView')
rootitem2 = QtGui.QStandardItem('Базовый класс')
item1 = QtGui.QStandardItem('QListView')
item2 = QtGui.QStandardItem('Список')
rootitem1.appendRow([item1, item2])
item1 = QtGui.QStandardItem('QTableView')
item2 = QtGui.QStandardItem('Таблица')
rootitem1.appendRow([item1, item2])
item1 = QtGui.QStandardItem('QTreeView')
item2 = QtGui.QStandardItem('Иерархический список')
rootitem1.appendRow([item1, item2])
sti.appendRow([rootitem1, rootitem2])
sti.setHorizontalHeaderLabels(['Класс', 'Описание'])
tv.setModel(sti)
tv.setColumnWidth(0, 170)
tv.resize(400, 100)
window.show()
sys.exit(app.exec_())
