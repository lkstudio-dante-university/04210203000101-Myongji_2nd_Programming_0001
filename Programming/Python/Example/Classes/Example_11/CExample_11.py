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
		super().__init__()
		self.__init__example_11__()
	
	# 초기화
	def __init__example_11__(self):
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
		가능하다. (즉, setupUi 메서드를 통해 배치 된 위젯의 이름을 기반으로 맴버 변수가 설정된다는 것을 알 수 있다.)
		"""
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
		oExample = CExample_11()
		
		sys.exit(oApp.exec())
