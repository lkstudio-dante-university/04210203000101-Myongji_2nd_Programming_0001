import os
import sys

"""
=====> 메뉴 <=====
1. 회원 추가
2. 회원 삭제
3. 회원 검색
4. 모든 회원 출력
5. 종료

메뉴 선택 : 1
이름 : 회원A
전화번호 : 1234

Case 1. 동일한 이름을 지닌 회원이 존재 할 경우
회원A 는 이미 가입 된 회원입니다.

Case 2. 처음 가입했을 경우
회원A 정보를 입력했습니다.

메뉴 선택 : 2
이름 : 회원A

Case 1. 회원이 존재 할 경우
회원A 를 삭제했습니다.

Case 2. 회원이 없을 경우
회원A 에 대한 정보를 찾을 수 없습니다.

메뉴 선택 : 3
이름 : 회원A

Case 1. 회원 존재 할 경우
=====> 회원 정보 <=====
이름 : 회원 A
전화번호 : 1234

Case 2. 회원이 없을 경우
회원A 에 대한 정보를 찾을 수 없습니다.

메뉴 선택 : 4
=====> 모든 회원 정보 <=====
이름 : 회원A
전화번호 : 1234

이름 : 회원B
전화번호 : 1234

메뉴 선택 : 5
프로그램을 종료합니다.
"""
# Example 6 - 3
class CE06_03:
    # 실행한다
	@classmethod
	def Run(cls):
		pass


# 회원
class CE06Member:
	# 생성자
	def __init__(self, a_oName:str, a_oPhoneNumber:str):
		self.m_oName = a_oName
		self.m_oPhoneNumber = a_oPhoneNumber

	# 정보를 출력한다
	def ShowInfo(self):
		print("이름 : {0}".format(self.m_oName))
		print("전화번호 : {0}".format(self.m_oPhoneNumber))
	

# 회원 관리자
class CE06MemberManager:
	m_oInst = None

	# 초기화
	def __init__(self):
		self.m_oMemberList = list()

		# 객체가 존재 할 경우
		if CE06MemberManager.m_oInst != None:
			"""
			raise 키워드는 예외를 발생시키는 역할을 수행한다. (즉, 프로그램이 동작 중에 의도하지 않는 데이터가 전달 되었을 때
			해당 키워드를 사용해서 프로그램을 중지하는 것이 가능하다.)

			따라서, 해당 키워드는 프로그램을 제작하는 도중에 예상하지 못한 경우를 처리하는데 활용되며 발생 된 예외는 try ~ except
			키워드를 통해 처리하는 것이 가능하다.
			"""
			raise Exception("CE06MemberManager.GetInst 메서드를 사용해주세요.")
		
		CE06MemberManager.m_oInst = self
		
	# 회원을 추가한다
	def AddMember(self, a_oMember:CE06Member):
		oMember = self.SearchMember(a_oMember.m_oName)

		# 회원이 없을 경우
		if oMember == None:
			self.m_oMemberList.append(oMember)
			return a_oMember
		
		return None

	# 회원을 제거한다
	def RemoveMember(self, a_oName:str):
		oMember = self.SearchMember(a_oName)

		# 회원이 존재 할 경우
		if oMember != None:
			self.m_oMemberList.remove(oMember)
			return oMember
		
		return None

	# 회원을 검색한다
	def SearchMember(self, a_oName:str):
		for oMember in self.m_oMemberList:
			# 이름이 동일 할 경우
			if oMember.m_oName == a_oName:
				return oMember
			
		return None

	# 모든 회원을 출력한다
	def ShowAllMembers(self):
		for oMember in self.m_oMemberList:
			oMember.ShowInfo()
			print()

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
		if cls.m_oInst == None:
			cls.m_oInst = CE06MemberManager()

		return cls.m_oInst
	