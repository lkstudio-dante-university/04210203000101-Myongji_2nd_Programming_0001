import os
import sys

from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Example.Classes.Example_09.E09_01.CE09_01 import *


# Example 9
class CExample_09:
	# 초기화
	@classmethod
	def Start(cls, args):
		"""
		QApplication 클래스는 PyQt 를 사용해서 제작 된 앱을 관리하는 역할을 수행한다. (즉, 해당 클래스는 단순히 앱을 생성하고 실행하는
		용도 이외에는 거의 사용되지 않는다는 것을 알 수 있다.)
		"""
		oApp = QApplication(args)
		
		"""
		try ~ except ~ finally 구문은 Python 으로 제작 된 프로그램이 실행 중에 발생하는 예외 (의도치 않은 동작) 를 처리하는 것이
		가능하다.
		
		try 구문은 예외를 감지하기 위한 구문을 의미하며 해당 구문 내부에서 발생한 예외는 except 구문에서 처리하는 것이 가능하다. 또한,
		예외는 raise 키워드를 통해서 명시적으로 발생시키는 것이 가능하다. (즉, 예외를 명시적으로 발생시킴으로서 프로그램을 제작하는 과정
		중에 발생하는 의도칙 않은 동작을 사전에 방지 할 수 있다는 것을 알 수 있다.)
		
		finally 구문은 try 구문 내부에서 예외가 발생하더라도 반드시 실행되는 구문을 의미한다. (즉, 해당 구문을 활용하면 스트림 해제와 같은
		컴퓨터 자원 처리 구문을 좀 더 안전하게 작성하는 것이 가능하다.)
		"""
		try:
			oExample = CE09_01()
		finally:
			"""
			sys.exit 메서드는 프로그램을 종료시키는 역할을 수행한다. (즉, 해당 메서드를 호출하면 프로그램은 처리 중인 작업을 모두 종료한
			후 즉시 프로그램이 종료시킨다는 것을 알 수 있다.)
			
			QApplication 클래스를 통해 생성 된 객체는 exec 메서드를 통해서 구동시키는 것이 가능하다. (즉, 해당 메서드를 호출하지 않으면
			PyQt 를 통해 제작 된 프로그램이 동작하지 않는다는 것을 알 수 있다.)
			"""
			sys.exit(oApp.exec())
