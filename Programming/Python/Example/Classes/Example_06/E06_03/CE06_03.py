import os
import sys

# 회원 관리자
class CE06MemberManager:
	m_oInst = None

	# 초기화
	def __init__(self):
		# 객체가 존재 할 경우
		if CE06MemberManager.m_oInst != None:
			"""
			rase 키워드는 예외를 발생시키는 역할을 수행한다. (즉, 프로그램이 동작 중에 의도하지 않는 데이터가 전달 되었을 때
			해당 키워드를 사용해서 프로그램을 중지하는 것이 가능하다.)

			따라서, 해당 키워드는 프로그램을 제작하는 도중에 예상하지 못한 경우를 처리하는데 활용되며 발생 된 예외는 try ~ except
			키워드를 통해 처리하는 것이 가능하다.
			"""
			raise Exception("CE06MemberManager.GetInst 메서드를 사용해서 객체를 생성해야합니다.")
		
	"""
	@classmethod 키워드는 해당 메서드가 객체에 종속되는 맴버 메서드가 아니라 클래스에 종속되는 클래스 메서드라는 것을 Python
	인터프리터에게 알리는 역할을 수행한다.

	따라서, 해당 키워드로 명시된 메서드는 클래스를 이름을 통해서 호출하는 것이 가능하며 항상 첫번째 매개 변수로 클래스 자체를
	나타내는 참조가 전달된다. (즉, 해당 매개 변수 이름은 cls 를 사용하는 것이 관례이며 맴버 메서드 일 경우에는 self 를 사용한다.)
	"""
	# 인스턴스를 반환한다
	@classmethod
	def GetInst(cls):
		# 객체 생성이 가능 할 경우
		if CE06MemberManager.m_oInst == None:
			CE06MemberManager.m_oInst = CE06MemberManager()

		return CE06MemberManager.m_oInst

# Example 6 - 3
class CE06_03:
    # 실행한다
	def Run(self):
		pass
