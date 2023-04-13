import os
import sys

from P06_01.CP06_01 import *

# Practice 6
class CPractice_06:
	MENU_NONE = -1
	MENU_ADD_MEMBER = 1
	MENU_REMOVE_MEMBER = 2
	MENU_SEARCH_MEMBER = 3
	MENU_PRINT_ALL_MEMBERS = 4
	MENU_EXIT = 5

    # 초기화
	@classmethod
	def Start(cls, args):
		nMenu = cls.MENU_NONE

		while nMenu != cls.MENU_EXIT:
			cls.PrintMenu()
			nMenu = int(input("\n메뉴 선택 : "))

			# 회원 추가 일 경우
			if nMenu == cls.MENU_ADD_MEMBER:
				cls.AddMember()

			# 회원 삭제 일 경우
			elif nMenu == cls.MENU_REMOVE_MEMBER:
				cls.RemoveMember()

			# 회원 검색 일 경우
			elif nMenu == cls.MENU_SEARCH_MEMBER:
				cls.SearchMember()

			# 모든 회원 출력 일 경우
			elif nMenu == cls.MENU_PRINT_ALL_MEMBERS:
				cls.PrintAllMembers()

			print()

	# 메뉴를 출력한다
	@classmethod
	def PrintMenu(cls):
		print("=====> 메뉴 <=====")
		print("1. 회원 추가")
		print("2. 회원 삭제")
		print("3. 회원 검색")
		print("4. 모든 회원 출력")
		print("5. 종료")

	# 회원을 추가한다
	@classmethod
	def AddMember(cls):
		oName = input("이름 : ")
		oPhoneNumber = input("전화번호 : ")

		# 회원을 추가했을 경우
		if CP06MemberManager.GetInst().AddMember(CP06Member(oName, oPhoneNumber)) != None:
			print("\n{0} 을(를) 추가했습니다.".format(oName))
		else:
			print("\n{0} 은(는) 추가 된 회원입니다.".format(oName))

	# 회원을 삭제한다
	@classmethod
	def RemoveMember(cls):
		oName = input("이름 : ")

		# 회원을 삭제했을 경우
		if CP06MemberManager.GetInst().RemoveMember(oName) != None:
			print("\n{0} 을(를) 삭제했습니다.".format(oName))
		else:
			print("\n{0} 은(는) 없는 회원입니다.".format(oName))

	# 회원을 검색한다
	@classmethod
	def SearchMember(cls):
		oName = input("이름 : ")
		oMember = CP06MemberManager.GetInst().SearchMember(oName)

		# 회원이 존재 할 경우
		if oMember != None:
			print("\n=====> 회원 정보 <=====")
			oMember.ShowInfo()
		else:
			print("\n{0} 은(는) 없는 회원입니다.".format(oName))

	# 모든 회원을 출력한다
	@classmethod
	def PrintAllMembers(cls):
		print("=====> 모든 회원 정보 <=====")
		CP06MemberManager.GetInst().PrintAllMembers()


# 메인 모듈 일 경우
if __name__ == "__main__":
	CPractice_06.Start(sys.argv)
	