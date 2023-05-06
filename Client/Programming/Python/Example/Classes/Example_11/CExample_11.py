import os
import sys

from PyQt5 import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Example.Classes.Global.Base.CMainWnd import *


# Example 11
class CExample_11(CMainWnd, uic.loadUiType("Resources/Example_11/E11MainWindow.ui")[0]):
	# 생성자
	def __init__(self):
		super().__init__()
		self.__init__example_11__()
	
	# 초기화
	def __init__example_11__(self):
		self.setWindowTitle("Example 11")
		
	# 초기화
	@classmethod
	def Start(cls, args):
		oApp = QApplication(args)
		
		try:
			oExample = CExample_11()
		
		finally:
			sys.exit(oApp.exec())
