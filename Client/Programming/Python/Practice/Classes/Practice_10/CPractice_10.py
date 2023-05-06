import os
import sys

from PyQt5 import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


# Practice 10
class CPractice_10(QMainWindow, uic.loadUiType("Resources/Practice_10/P10MainWindow.ui")[0]):
	# 생성자
	def __init__(self):
		super().__init__()
		self.__init__practice_10__()
	
	# 초기화
	def __init__practice_10__(self):
		self.show()
		self.setupUi(self)
		self.setWindowTitle("Practice 10")
		
		# 영역을 설정한다
		nHeight = self.frameGeometry().height() - self.geometry().height()
		self.setGeometry(10, 10 + nHeight, self.geometry().width(), self.geometry().height())
	
	# 초기화
	@classmethod
	def Start(cls, args):
		oApp = QApplication(args)
		
		try:
			oPractice = CPractice_10()
			
		finally:
			sys.exit(oApp.exec())
