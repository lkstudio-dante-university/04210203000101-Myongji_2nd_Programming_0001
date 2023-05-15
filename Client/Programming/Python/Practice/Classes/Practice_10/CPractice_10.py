import os
import sys

from PyQt5 import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


# Practice 10
class CPractice_10(QMainWindow, uic.loadUiType("Resources/Practice_10/P10MainWindow.ui")[0]):
	# 도구
	class EP10Tool:
		NONE = -1
		PEN = 0
		LINE = 1
		ELLIPSE = 2
		RECTANGLE = 3
		MAX_VAL = RECTANGLE + 1
	
	# 생성자
	def __init__(self):
		# 맴버 변수를 설정한다
		self.m_eSelTool = CPractice_10.EP10Tool.PEN
		self.m_oPosList = []
		
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
		
		# 타이머를 설정한다
		self.m_oTimer = QTimer(self)
		self.m_oTimer.timeout.connect(self.OnUpdate)
		
		self.m_oTimer.start()
		
		# 메뉴 바를 설정한다
		self.menuBar().setNativeMenuBar(False)
		self.actionAbout.triggered.connect(self.OnClickAboutMenu)
		
		# 버튼을 설정한다
		self.m_oPenBtn = QPushButton("펜", self.centralWidget())
		self.m_oPenBtn.setGeometry(10, 10, 150, 35)
		self.m_oPenBtn.clicked.connect(lambda: self.OnClickToolBtn(CPractice_10.EP10Tool.PEN))
		
		self.m_oLineBtn = QPushButton("직선", self.centralWidget())
		self.m_oLineBtn.setGeometry(170, 10, 150, 35)
		self.m_oLineBtn.clicked.connect(lambda: self.OnClickToolBtn(CPractice_10.EP10Tool.LINE))
		
		self.m_oEllipseBtn = QPushButton("타원", self.centralWidget())
		self.m_oEllipseBtn.setGeometry(330, 10, 150, 35)
		self.m_oEllipseBtn.clicked.connect(lambda: self.OnClickToolBtn(CPractice_10.EP10Tool.ELLIPSE))
		
		self.m_oRectangleBtn = QPushButton("사각형", self.centralWidget())
		self.m_oRectangleBtn.setGeometry(490, 10, 150, 35)
		self.m_oRectangleBtn.clicked.connect(lambda: self.OnClickToolBtn(CPractice_10.EP10Tool.RECTANGLE))
	
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
			
	# 마우스 이동 이벤트를 수신했을 경우
	def mouseMoveEvent(self, a_oEvent: QMouseEvent):
		pass
	
	# 마우스 버튼 눌림 이벤트를 수신했을 경우
	def mousePressEvent(self, a_oEvent: QMouseEvent):
		pass
	
	# 마우스 버튼 눌림 종료 이벤트를 수신했을 경우
	def mouseReleaseEvent(self, a_oEvent: QMouseEvent):
		pass
	
	# 정보 메뉴를 눌렀을 경우
	def OnClickAboutMenu(self):
		QMessageBox.aboutQt(self, "알림")
	
	# 툴 버튼을 눌렀을 경우
	def OnClickToolBtn(self, a_eTool: EP10Tool):
		self.m_eSelTool = a_eTool
	
	# 초기화
	@classmethod
	def Start(cls, args):
		oApp = QApplication(args)
		oPractice = CPractice_10()
		
		sys.exit(oApp.exec())
