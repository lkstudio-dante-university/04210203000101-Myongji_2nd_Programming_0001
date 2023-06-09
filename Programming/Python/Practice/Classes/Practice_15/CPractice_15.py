import os
import sys

from PyQt5 import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Example.Classes.Global.Manager.CTimeManager import *
from Example.Classes.Global.Manager.CInputManager import *

"""
기말 평가
- 볼 반사 시뮬레이션 제작하기
- 좌하단에 터렛을 배치 후 위/아래 방향키로 포신 각도 조절
- 스페이스 키를 눌렀다가 때면 포신 각도로 볼 발사 (단, 스페이스 키를 오래 누를수록 볼 속도 증가)
- 발사 된 볼이 벽에 부딛쳤을 경우 반사 (즉, 충돌한 벽에 따라 상/하 또는 좌/우로 반사)
- 일정 횟수 이상 반사되면 볼 제거 (즉, 최대 반사 가능한 횟수 제한)
"""


# Practice 15
class CPractice_15(QMainWindow, uic.loadUiType("Resources/Practice_15/P15MainWindow.ui")[0]):
	# 생성자
	def __init__(self):
		super().__init__()
		self.__init__practice_15__()
	
	# 초기화
	def __init__practice_15__(self):
		self.show()
		self.setupUi(self)
		self.setWindowTitle("Practice 15")
		
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
		
		# 관리자를 갱신한다
		CTimeManager.GetInst().Update()
		CInputManager.GetInst().Update()
		
		# 라벨을 갱신한다
		self.labelDeltaTime.setText("Delta Time: {0:0.5f} sec".format(CTimeManager.GetInst().GetDeltaTime()))
		self.labelRunningTime.setText("Running Time: {0:0.5f} sec".format(CTimeManager.GetInst().GetRunningTime()))
	
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
			
		CInputManager.GetInst().AddKey(a_oEvent.key())
		
	# 키 눌림 종료 이벤트를 수신했을 경우
	def keyReleaseEvent(self, a_oEvent: QKeyEvent):
		CInputManager.GetInst().RemoveKey(a_oEvent.key())
	
	# 정보 메뉴를 눌렀을 경우
	def OnClickAboutMenu(self):
		QMessageBox.aboutQt(self, "알림")
	
	# 초기화
	@classmethod
	def Start(cls, args):
		oApp = QApplication(args)
		oPractice = CPractice_15()
		
		sys.exit(oApp.exec())
