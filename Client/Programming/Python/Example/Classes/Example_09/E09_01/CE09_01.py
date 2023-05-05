import os
import sys

from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

"""
QMainWindow 클래스는 윈도우를 제어하는 역할을 수행한다. (즉, 일반적인 GUI 프로그램은 대부분 윈도우 형태로 제작되기 때문에 QMainWindow
클래스를 상속함으로서 다양한 GUI 프로그램을 제작하는 것이 가능하다.)
"""
# Example 9 - 1
class CE09_01(QMainWindow):
	# 생성자
	def __init__(self):
		super().__init__()
		self.__init__E09_01()
	
	# 초기화
	def __init__E09_01(self):
		self.show()
		self.setWindowTitle("Example 9 - 1")
		
		"""
		Geometry vs Frame Geometry
		- Geometry 는 윈도우의 타이틀 바를 제외한 영역을 의미하며 이를 클라이언트 영역이라고 한다. 반면, Frame Geometry 는 윈도우의
		타이틀 바를 포함한 영역을 의미하기 때문에 이를 윈도우 영역이라고 부른다. (즉, 일반적인 GUI 위젯은 클라이언트 영역에 배치 된다는 것을
		알 수 있다.)
		
		QDesktopWidget 이란?
		- 윈도우즈 플랫폼의 바탕화면 (Mac 플랫폼에서는 Finder) 을 제어 할 수 있는 클래스를 의미한다. (즉, 해당 클래스를 활용하면 현재
		디스플레이의 해상도 등을 가져오는 것이 가능하다.)
		"""
		# 영역을 설정한다
		nHeight = self.frameGeometry().height() - self.geometry().height()
		oDesktopGeometry = QDesktopWidget().availableGeometry()
		
		self.setGeometry(10, 10 + nHeight, oDesktopGeometry.width() // 2, oDesktopGeometry.height() // 2)
		
		"""
		메뉴란?
		- 윈도우 바 하단에 위치하는 버튼 위젯을 의미한다. (즉, 메뉴를 활용하면 윈도우에서 공통적으로 사용 되는 기능들을 버튼 형태로 표현하는
		것이 가능하다.)
		
		PyQt 에서는 특정 메뉴가 선택 되었을 경우 해당 메뉴를 처리하기 위해서 액션 객체가 필요하다. (즉, 액션 객체는 메뉴 버튼과 이를 처리하기
		위한 메서드를 연결해주는 객체라는 것을 알 수 있다.)
		"""
		# 메뉴를 설정한다
		oAction = QAction("About", self)
		oAction.triggered.connect(self.OnClickAboutMenu)
		
		oMenuBar = self.menuBar()
		oMenuBar.setNativeMenuBar(False)
		
		oFileMenu = oMenuBar.addMenu("File")
		oFileMenu.addAction(oAction)
	
	# 정보 메뉴를 눌렀을 경우
	def OnClickAboutMenu(self):
		"""
		QMessageBox 클래스는 알림 창을 제어하는 역할을 수행한다. (즉, 해당 클래스를 활용하면 특정 동작의 진행 여부를 사용자로부터 입력받거나
		반대로 사용자에게 특정 연산 결과를 알리는 것이 가능하다.)
		"""
		QMessageBox.aboutQt(self, "알림")
