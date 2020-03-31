from PyQt5.QtWidgets import QApplication
import sys

from VishFileDialog import VishApp



if __name__ == '__main__':
	print("inside main method of python file")
	app = QApplication(sys.argv)
	ex = VishApp()
	sys.exit(app.exec_())