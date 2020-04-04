import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog,QLineEdit,QFileDialog
from PyQt5.QtGui import QIcon


class VishApp(QWidget):

	def __init__(self):
		super().__init__()
		print("inside App class's init method")
		self.title = 'PyQt5 file dialog - pythonspot.com'
		self.left = 10
		self.top = 10
		self.width = 400
		self.height = 400
		self.initUI()

	def initUI(self):
		print("inside App:initUI() method")
		self.setWindowTitle(self.title)
		self.setGeometry(self.left,self.top,self.width,self.height)
		self.openFileNameDialog()
		self.show()


	def openFileNameDialog(self):
		print("inside App:openFileNameDialog() method")
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files(*);; Python Files (*.py)", options=options)
		if fileName:
			print("file selected:"+fileName)


if __name__ == '__main__':
	print("inside main method of python file")
	app = QApplication(sys.argv)
	ex = VishApp()
	sys.exit(app.exec_())
