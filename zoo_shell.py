from PyQt5 import QtGui, QtWidgets, QtCore
import zoo_model


class ZooShellEdit(QtWidgets.QPlainTextEdit):
    def __init__(self, parent=None):
        QtWidgets.QPlainTextEdit.__init__(self, parent)
        self.setFont(QtGui.QFont('Arial', 9))

        self.prompt_ = ">"
        self.insertPlainText(self.prompt_)
        self.mainWindow = None

    def keyPressEvent(self, keyEvent: QtGui.QKeyEvent):
        if(keyEvent.key() == QtCore.Qt.Key_Return):
            lines = self.toPlainText().split('\n')
            self.mainWindow.shellCommand(lines[len(lines)-1])
        else:
            super().keyPressEvent(keyEvent)

    def connect(self, prompt):
        self.prompt_ = prompt
        self.appendPlainText(self.prompt_ + ">")

    def printError(self, error):
        self.appendPlainText(error)
        self.appendPlainText(self.prompt_ + ">")

    def printResult(self):
        self.appendPlainText('success')
        self.appendPlainText(self.prompt_ + ">")
