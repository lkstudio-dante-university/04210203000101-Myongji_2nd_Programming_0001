import os
import sys

from PyQt5 import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

"""
uic.loadUiType 메서드는 Designer 프로그램으로 작성 된 UI 파일을 불러오는 역할을 수행한다. 따라서, 해당 메서드를 이용하면
Designer 프로그램을 통해 미리 배치 된 UI 위젯을 손쉽게 설정하는 것이 가능하다.
"""


# Example 11
class CExample_11(QMainWindow, uic.loadUiType("Resources/Example_11/E11MainWindow.ui")[0]):
	# 생성자
	def __init__(self):
		# 멤버 변수를 설정한다
		self.m_oCurShape = None
		self.m_oShapeList = []
		
		self.m_nSelTool = CE11Tool.PEN
		self.m_nSelPenColor = CE11Color.DEF
		self.m_nSelBrushColor = CE11Color.DEF
		
		super().__init__()
		self.__init__example_11__()
	
	# 초기화
	def __init__example_11__(self):
		"""
		setupUi 메서드는 Designer 프로그램을 통해 배치 된 UI 위젯을 실제 QMainWindow 상에 설정하는 역할을 수행한다. (즉,
		uic.loadUiType 메서드는 Designer 로 작업 된 파일을 불러오는 역할을 수행 할 뿐 실제 해당 파일에 존재하는 UI 위젯을 설정해주는
		메서드는 self.setupUi 메서드라는 것을 알 수 있다.)
		"""
		self.show()
		self.setupUi(self)
		self.setWindowTitle("Example_11")
		
		# 영역을 설정한다
		nHeight = self.frameGeometry().height() - self.geometry().height()
		self.setGeometry(10, 10 + nHeight, self.geometry().width(), self.geometry().height())
		
		# 타이머를 설정한다
		self.m_oTimer = QTimer(self)
		self.m_oTimer.timeout.connect(self.OnUpdate)
		
		self.m_oTimer.start()
		
		"""
		Designer 프로그램에서 배치 된 각 위젯은 중복되지 않는 고유한 이름을 지니고 있으며 해당 이름을 활용하면 특정 위젯을 제어하는 것이
		가능하다. (즉, setupUi 메서드를 통해 배치 된 위젯의 이름을 기반으로 맴버 변수가 자동으로 선언 된다는 것을 알 수 있다.)
		"""
		# 메뉴 바를 설정한다
		self.menuBar().setNativeMenuBar(False)
		self.actionAbout.triggered.connect(self.OnClickAboutMenu)
		
		# 버튼을 설정한다
		self.btnPen.clicked.connect(lambda: self.OnClickToolBtn(CE11Tool.PEN))
		self.btnLine.clicked.connect(lambda: self.OnClickToolBtn(CE11Tool.LINE))
		self.btnEllipse.clicked.connect(lambda: self.OnClickToolBtn(CE11Tool.ELLIPSE))
		self.btnRectangle.clicked.connect(lambda: self.OnClickToolBtn(CE11Tool.RECTANGLE))
		
		self.btnPenDefColor.clicked.connect(lambda: self.OnClickPenColorBtn(CE11Color.DEF))
		self.btnPenRedColor.clicked.connect(lambda: self.OnClickPenColorBtn(CE11Color.RED))
		self.btnPenGreenColor.clicked.connect(lambda: self.OnClickPenColorBtn(CE11Color.GREEN))
		self.btnPenBlueColor.clicked.connect(lambda: self.OnClickPenColorBtn(CE11Color.BLUE))
		
		self.btnBrushDefColor.clicked.connect(lambda: self.OnClickBrushColorBtn(CE11Color.DEF))
		self.btnBrushRedColor.clicked.connect(lambda: self.OnClickBrushColorBtn(CE11Color.RED))
		self.btnBrushGreenColor.clicked.connect(lambda: self.OnClickBrushColorBtn(CE11Color.GREEN))
		self.btnBrushBlueColor.clicked.connect(lambda: self.OnClickBrushColorBtn(CE11Color.BLUE))
		
		self.btnClearAllShapes.clicked.connect(self.OnClickClearAllShapesBtn)
	
	# 상태를 갱신한다
	def OnUpdate(self):
		self.update()
	
	# 그리기 이벤트를 수신했을 경우
	def paintEvent(self, a_oEvent: QPaintEvent):
		oPainter = QPainter(self)
		
		try:
			for oShape in self.m_oShapeList:
				oShape.Draw(oPainter)
		
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
		# 현재 도형이 존재 할 경우
		if self.m_oCurShape != None:
			self.m_oCurShape.AddPos(QPoint(a_oEvent.x(), a_oEvent.y()))
	
	# 마우스 눌림 이벤트를 수신했을 경우
	def mousePressEvent(self, a_oEvent: QMouseEvent):
		self.m_oCurShape = self.CreateShape()
		self.m_oCurShape.AddPos(QPoint(a_oEvent.x(), a_oEvent.y()))
		
		self.m_oShapeList.append(self.m_oCurShape)
	
	# 마우스 눌림 종료 이벤트를 수신했을 경우
	def mouseReleaseEvent(self, a_oEvent: QMouseEvent):
		self.mouseMoveEvent(a_oEvent)
		self.m_oCurShape = None
	
	# 정보 메뉴를 눌렀을 경우
	def OnClickAboutMenu(self):
		QMessageBox.aboutQt(self, "알림")
	
	# 도구 버튼을 눌렀을 경우
	def OnClickToolBtn(self, a_nTool: int):
		self.m_nSelTool = a_nTool
		self.m_oCurShape = self.CreateShape()
	
	# 펜 색상 버튼을 눌렀을 경우
	def OnClickPenColorBtn(self, a_nColor: int):
		self.m_nSelPenColor = a_nColor
		self.m_oCurShape = self.CreateShape()
	
	# 펜 색상 버튼을 눌렀을 경우
	def OnClickBrushColorBtn(self, a_nColor: int):
		self.m_nSelBrushColor = a_nColor
		self.m_oCurShape = self.CreateShape()
	
	# 모든 도형 지우기 버튼을 눌렀을 경우
	def OnClickClearAllShapesBtn(self):
		self.m_oShapeList.clear()
	
	# 도형을 생성한다
	def CreateShape(self):
		oShapeList = [
			CE11Pen(self.m_nSelPenColor, self.m_nSelBrushColor),
			CE11Line(self.m_nSelPenColor, self.m_nSelBrushColor),
			CE11Ellipse(self.m_nSelPenColor, self.m_nSelBrushColor),
			CE11Rectangle(self.m_nSelPenColor, self.m_nSelBrushColor)
		]
		
		return oShapeList[self.m_nSelTool]
	
	# 초기화
	@classmethod
	def Start(cls, args):
		oApp = QApplication(args)
		oExample = CExample_11()
		
		sys.exit(oApp.exec())


# 도구
class CE11Tool:
	NONE = -1
	PEN = 0
	LINE = 1
	ELLIPSE = 2
	RECTANGLE = 3
	MAX_VAL = RECTANGLE + 1


# 색상
class CE11Color:
	NONE = -1
	DEF = 0
	RED = 1
	GREEN = 2
	BLUE = 3
	MAX_VAL = BLUE + 1


# 도형
class CE11Shape:
	PEN_COLOR_LIST = [
		QColor(0, 0, 0, 255), QColor(255, 0, 0, 255), QColor(0, 255, 0, 255), QColor(0, 0, 255, 255)
	]
	
	BRUSH_COLOR_LIST = [
		QColor(0, 0, 0, 0), QColor(255, 0, 0, 255), QColor(0, 255, 0, 255), QColor(0, 0, 255, 255)
	]
	
	# 생성자
	def __init__(self, a_nPenColor: int, a_nBrushColor: int):
		self.m_oPosList = []
		self.m_nPenColor = a_nPenColor
		self.m_nBrushColor = a_nBrushColor
	
	# 위치를 추가한다
	def AddPos(self, a_oPos: QPoint):
		self.m_oPosList.append(a_oPos)
	
	# 도형을 그린다
	def Draw(self, a_oPainter: QPainter):
		a_oPainter.setPen(QPen(CE11Shape.PEN_COLOR_LIST[self.m_nPenColor]))
		a_oPainter.setBrush(QBrush(CE11Shape.BRUSH_COLOR_LIST[self.m_nBrushColor]))


# 펜
class CE11Pen(CE11Shape):
	# 도형을 그린다
	def Draw(self, a_oPainter: QPainter):
		super().Draw(a_oPainter)
		
		# 위치 정보가 존재 할 경우
		if len(self.m_oPosList) >= 2:
			for i in range(0, len(self.m_oPosList) - 1):
				a_oPainter.drawLine(self.m_oPosList[i], self.m_oPosList[i + 1])


# 직선
class CE11Line(CE11Shape):
	# 도형을 그린다
	def Draw(self, a_oPainter: QPainter):
		super().Draw(a_oPainter)
		
		# 위치 정보가 존재 할 경우
		if len(self.m_oPosList) >= 2:
			a_oPainter.drawLine(self.m_oPosList[0], self.m_oPosList[len(self.m_oPosList) - 1])


# 타원
class CE11Ellipse(CE11Shape):
	# 도형을 그린다
	def Draw(self, a_oPainter: QPainter):
		super().Draw(a_oPainter)
		
		# 위치 정보가 존재 할 경우
		if len(self.m_oPosList) >= 2:
			a_oPainter.drawEllipse(QRect(self.m_oPosList[0], self.m_oPosList[len(self.m_oPosList) - 1]))


# 사각형
class CE11Rectangle(CE11Shape):
	# 도형을 그린다
	def Draw(self, a_oPainter: QPainter):
		super().Draw(a_oPainter)
		
		# 위치 정보가 존재 할 경우
		if len(self.m_oPosList) >= 2:
			a_oPainter.drawRect(QRect(self.m_oPosList[0], self.m_oPosList[len(self.m_oPosList) - 1]))
