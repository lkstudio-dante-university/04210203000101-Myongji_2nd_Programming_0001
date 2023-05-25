import os
import sys

from PyQt5 import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

"""
과제 12 - 1
-
"""


# Practice 12
class CPractice_12(QMainWindow, uic.loadUiType("Resources/Practice_12/P12MainWindow.ui")[0]):
	# 생성자
	def __init__(self):
		super().__init__()
		self.__init__practice_12__()
	
	# 초기화
	def __init__practice_12__(self):
		self.show()
		self.setupUi(self)
		self.setWindowTitle("Practice 12")
		
		# 영역을 설정한다
		nHeight = self.frameGeometry().height() - self.geometry().height()
		self.setGeometry(10, 10 + nHeight, self.geometry().width(), self.geometry().height())
		
		# 타이머를 설정한다
		self.m_oTimer = QTimer(self)
		self.m_oTimer.timeout.connect(self.OnUpdate)
		
		self.m_oTimer.start(1)
		
		# 메뉴 바를 설정한다
		self.menuBar().setNativeMenuBar(False)
		self.actionAbout.triggered.connect(self.OnClickAboutMenu)
	
	# 상태를 갱신한다
	def OnUpdate(self):
		self.update()
	
	# 그리기 이벤트를 수신했을 경우
	def paintEvent(self, a_oEvent: QPaintEvent):
		oPainter = QPainter(self)
		
		try:
			pass
		
		finally:
			oPainter.end()
	
	# 닫기 이벤트를 수신했을 경우
	def closeEvent(self, a_oEvent: QCloseEvent):
		nResult = QMessageBox.question(self, "알림", "앱을 종료하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		a_oEvent.accept() if nResult == QMessageBox.Yes else a_oEvent.ignore()
	
	# 키 눌림 이벤트를 수신했을 경우
	def keyPressEvent(self, a_oEvent: QKeyEvent):
		# Esc 키를 눌렀을 경우
		if a_oEvent.key() == Qt.Key_Escape:
			self.close()
			
	# 정보 메뉴를 눌렀을 경우
	def OnClickAboutMenu(self):
		QMessageBox.aboutQt(self, "알림")
	
	# 초기화
	@classmethod
	def Start(cls, args):
		oApp = QApplication(args)
		oPractice = CPractice_12()
		
		sys.exit(oApp.exec())
