import os
import sys

from PyQt5 import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


# Example 10
class CExample_10(QMainWindow, uic.loadUiType("Resources/Example_10/E10MainWindow.ui")[0]):
	# 생성자
	def __init__(self):
		super().__init__()
		self.__init__example_10__()
	
	# 초기화
	def __init__example_10__(self):
		self.show()
		self.setupUi(self)
		self.setWindowTitle("Example 10")
		
		# 영역을 설정한다
		nHeight = self.frameGeometry().height() - self.geometry().height()
		self.setGeometry(10, 10 + nHeight, self.geometry().width(), self.geometry().height())
		
		# 변수를 설정한다
		self.m_oSrcPos = QPoint(0, 0)
		self.m_oDestPos = QPoint(0, 0)
		
		self.m_nColor = E10Color.RED
		self.m_nShape = E10Shape.LINE
		
		# 메뉴 바를 설정한다
		self.menuBar().setNativeMenuBar(False)
		self.actionAbout.triggered.connect(self.OnClickAboutMenu)
		
		# 버튼을 설정한다
		self.btnRed.clicked.connect(lambda: self.OnClickColorRadioBtn(E10Color.RED))
		self.btnGreen.clicked.connect(lambda: self.OnClickColorRadioBtn(E10Color.GREEN))
		self.btnBlue.clicked.connect(lambda: self.OnClickColorRadioBtn(E10Color.BLUE))
		
		self.btnLine.clicked.connect(lambda: self.OnClickShapeRadioBtn(E10Shape.LINE))
		self.btnEllipse.clicked.connect(lambda: self.OnClickShapeRadioBtn(E10Shape.ELLIPSE))
		self.btnRectangle.clicked.connect(lambda: self.OnClickShapeRadioBtn(E10Shape.RECTANGLE))
	
	# 닫기 이벤트를 수신했을 경우
	def closeEvent(self, a_oEvent: QCloseEvent):
		nResult = QMessageBox.question(self, "알림", "앱을 종료하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		a_oEvent.accept() if nResult == QMessageBox.Yes else a_oEvent.ignore()
	
	# 그리기 이벤트를 수신했을 경우
	def paintEvent(self, a_oEvent: QPaintEvent):
		oPainter = QPainter(self)
		
		try:
			oColorList = [
				QColor(255, 0, 0), QColor(0, 255, 0), QColor(0, 0, 255)
			]
			
			oPainter.setPen(QPen(oColorList[self.m_nColor], 1))
			
			# 라인 일 경우
			if self.m_nShape == E10Shape.LINE:
				oPainter.drawLine(self.m_oSrcPos, self.m_oDestPos)
			
			# 타원 일 경우
			elif self.m_nShape == E10Shape.ELLIPSE:
				oPainter.drawEllipse(self.m_oSrcPos.x(), self.m_oSrcPos.y(), self.m_oDestPos.x() - self.m_oSrcPos.x(), self.m_oDestPos.y() - self.m_oSrcPos.y())
			
			# 사각형 일 경우
			elif self.m_nShape == E10Shape.RECTANGLE:
				oPainter.drawRect(self.m_oSrcPos.x(), self.m_oSrcPos.y(), self.m_oDestPos.x() - self.m_oSrcPos.x(), self.m_oDestPos.y() - self.m_oSrcPos.y())
		
		finally:
			oPainter.end()
	
	# 키 눌림 이벤트를 수신했을 경우
	def keyPressEvent(self, a_oEvent: QKeyEvent):
		# 백 키를 눌렀을 경우
		if a_oEvent.key() == Qt.Key_Escape:
			self.close()
	
	# 마우스 이동 이벤트를 수신했을 경우
	def mouseMoveEvent(self, a_oEvent: QMouseEvent):
		self.m_oDestPos = QPoint(a_oEvent.x(), a_oEvent.y())
		self.update()
	
	# 마우스 버튼 눌림 이벤트를 수신했을 경우
	def mousePressEvent(self, a_oEvent: QMouseEvent):
		self.m_oSrcPos = QPoint(a_oEvent.x(), a_oEvent.y())
	
	# 마우스 버튼 눌림 종료 이벤트를 수신했을 경우
	def mouseReleaseEvent(self, a_oEvent: QMouseEvent):
		self.m_oDestPos = QPoint(a_oEvent.x(), a_oEvent.y())
	
	# 정보 메뉴를 눌렀을 경우
	def OnClickAboutMenu(self):
		QMessageBox.aboutQt(self, "알림")
	
	# 색상 라디오 버튼을 눌렀을 경우
	def OnClickColorRadioBtn(self, a_nColor: int):
		self.m_nColor = a_nColor
	
	# 모양 라디오 버튼을 눌렀을 경우
	def OnClickShapeRadioBtn(self, a_nShape: int):
		self.m_nShape = a_nShape
	
	# 초기화
	@classmethod
	def Start(cls, args):
		oApp = QApplication(args)
		
		try:
			oExample = CExample_10()
		
		finally:
			sys.exit(oApp.exec())


# 색상
class E10Color:
	NONE = -1
	RED = 0
	GREEN = 1
	BLUE = 2
	MAX_VAL = BLUE + 1


# 모양
class E10Shape:
	NONE = -1
	LINE = 0
	ELLIPSE = 1
	RECTANGLE = 2
	MAX_VAL = RECTANGLE + 1
