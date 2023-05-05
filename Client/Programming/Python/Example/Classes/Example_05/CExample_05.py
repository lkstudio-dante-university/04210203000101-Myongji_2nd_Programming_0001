import os
import sys

from Example.Classes.Example_05.E05_01.CE05_01 import *


# Example 5
class CExample_05:
	# 초기화
	@classmethod
	def Start(cls, argv):
		# cls.E05_01(argv)
		cls.E05_02(argv)
	
	# 5 - 1
	@classmethod
	def E05_01(cls, argv):
		"""
		Python 의 자료형은 값 형식 자로형과 참조 형식 자료형으로 나뉜다. (즉, 클래스는 참조 형식 자료형에 해당하기 때문에 해당 변수에는 생성 된 
		객체가 아닌 해당 객체를 가리키는 참조 값이 할당 된다는 것을 알 수 있다.)

		값 형식 vs 참조 형식
		- 값 형식은 실제 데이터를 다루기 때문에 해당 형식 변수를 다른 변수에 할당했을 경우 사본 변수가 만들어지는 특징이 존재한다. (즉, 사본
		변수를 변경해도 원본 변수는 전혀 영향을 받지 않는다.)

		반면, 참조 형식은 실제 데이터가 아닌 해당 데이터를 가리키는 참조 값 (메모리 주소) 를 다루기 때문에 해당 형식 변수를 다른 변수에
		할당했을 경우 얕은 복사가 이루어지기 때문에 사본 변수를 변경하면 원본 변수도 영향을 받는다는 차이점이 존재한다.

		Python 값 형식 자료형
		- int
		- float

		Python 참조 형식 자료형
		- str
		- list
		- dict
		- 등등...

		즉, int 및 float 자료형을 제외하면 모두 참조 형식 자료형에 속한다는 것을 알 수 있다.
		"""
		oSuperA = CE05Super()
		oSuperB = CE05Super()
		
		"""
		객체 하위에 존재하는 맴버에 접근하기 위해서는 . (맴버 접근 연산자) 를 사용하면 된다. (즉, 해당 연산자를 활용하면 특정 객체 하위에
		존재하는 변수 및 메서드를 사용하는 것이 가능하다.
		"""
		oSuperA.m_nVal = 10
		oSuperB.m_nVal = 20
		
		print("=====> 클래스 정보 <=====")
		oSuperA.ShowInfo()
		oSuperB.ShowInfo()
	
	# 5 - 2
	@classmethod
	def E05_02(cls, argv):
		oSuper = CE05Super()
		oSub = CE05Sub()
		
		oSuper.m_nVal = 10
		
		"""
		Sub 클래스 객체는 Super 클래스를 상속했기 때문에 Sub 클래스에 있는 맴버 뿐만 아니라 Super 클래스에 존재하는 맴버도 사용 가능하다는
		것을 알 수 있다.
		"""
		oSub.m_nVal = 20
		oSub.m_oStr = "Hello, World!"
		
		print("=====> 부모 클래스 정보 <=====")
		oSuper.ShowInfo()
		
		print("\n=====> 자식 클래스 정보 <=====")
		oSub.ShowInfo()
