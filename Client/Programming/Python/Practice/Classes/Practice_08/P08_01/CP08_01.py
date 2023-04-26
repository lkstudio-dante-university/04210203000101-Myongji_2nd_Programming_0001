import os
import sys
import random

from P08_01.CP08Utility import *
from P08_01.CP08UserInfoStorage import *
from P08_01.CP08StoreInfoStorage import *

# 상점
class CP08Store:
	MENU_NONE = -1
	MENU_BUY_EQUIP = 0
	MENU_SELL_EQUIP = 1
	MENU_EXIT = 2
	
	# 방문한다
	@classmethod
	def Visit(cls):
		nSelMenu = cls.MENU_NONE

		while nSelMenu != cls.MENU_EXIT:
			cls.PrintMenu()
			nSelMenu = int(input("\n상점 메뉴 선택 : ")) - 1

			# 장비 구입 일 경우
			if nSelMenu == cls.MENU_BUY_EQUIP:
				cls.BuyEquip()

			# 장비 판매 일 경우
			elif nSelMenu == cls.MENU_SELL_EQUIP:
				cls.SellEquip()

			print("")

	# 메뉴를 출력한다
	@classmethod
	def PrintMenu(cls):
		print("=====> 상점 메뉴 <=====")
		print("1. 장비 구입")
		print("2. 장비 판매")
		print("3. 나가기")

	# 장비 구입 메뉴를 출력한다
	@classmethod
	def PrintBuyEquipMenu(cls, a_oMenuEquipInfoList:list):
		print("=====> 구입 가능 장비 <=====")

		for i, oMenuEquipInfo in enumerate(a_oMenuEquipInfoList):
			print("{0}. {1} (비용 : {2}, 재고 : {3})".format(i + 1, oMenuEquipInfo.GetKinds(), CP08Utility.GetPrice(oMenuEquipInfo, True), oMenuEquipInfo.m_nNumEquips))

		print("{0}. 그만두기".format(len(a_oMenuEquipInfoList) + 1))

	# 장비 판매 메뉴를 출력한다
	@classmethod
	def PrintSellEquipMenu(cls, a_oMenuEquipInfoList:list):
		print("=====> 판매 가능 장비 <=====")

		for i, oMenuEquipInfo in enumerate(a_oMenuEquipInfoList):
			print("{0}. {1} (등급 : {2}, 비용 : {3}, 재고 : {4})".format(i + 1, oMenuEquipInfo.GetKinds(), oMenuEquipInfo.GetGrade(), CP08Utility.GetPrice(oMenuEquipInfo, False), oMenuEquipInfo.m_nNumEquips))

		print("{0}. 그만두기".format(len(a_oMenuEquipInfoList) + 1))

	# 장비를 구입한다
	@classmethod
	def BuyEquip(cls):
		nSelEquip = -1
		oMenuEquipInfoList = CP08Utility.ConvertToMenuEquipInfos(CP08StoreInfoStorage.GetInst().GetStoreInfo(0).m_oEquipList)

		while nSelEquip < len(oMenuEquipInfoList):
			cls.PrintBuyEquipMenu(oMenuEquipInfoList)
			nSelEquip = int(input("\n구입 장비 선택 (소지 금액 : {0}) : ".format(CP08UserInfoStorage.GetInst().GetUserInfo(0).m_nNumGolds))) - 1

			# 장비를 선택했을 경우
			if nSelEquip < len(oMenuEquipInfoList):
				nNumEquips = int(input("구입 수량 입력 : "))

				# 재고가 부족 할 경우
				if oMenuEquipInfoList[nSelEquip].m_nNumEquips < nNumEquips:
					print("재고가 부족합니다.")

				# 비용이 부족 할 경우
				elif CP08UserInfoStorage.GetInst().GetUserInfo(0).m_nNumGolds * nNumEquips < CP08Utility.GetPrice(oMenuEquipInfoList[nSelEquip], True):
					print("비용이 부족합니다.")

				else:
					for _ in range(0, nNumEquips):
						oEquipInfo = CP08EquipInfo(oMenuEquipInfoList[nSelEquip].m_nKinds, random.randint(CP08EquipInfo.GRADE_COMMON, CP08EquipInfo.GRADE_HERO))
						print("{0} {1} 을(를) 구입했습니다.".format(oEquipInfo.GetGrade(), oEquipInfo.GetKinds()))

						CP08UserInfoStorage.GetInst().GetUserInfo(0).m_nNumGolds -= CP08Utility.GetPrice(oMenuEquipInfoList[nSelEquip], True)

						CP08UserInfoStorage.GetInst().GetUserInfo(0).AddEquipInfo(oEquipInfo)
						CP08StoreInfoStorage.GetInst().GetStoreInfo(0).RemoveEquipInfo(oEquipInfo)

				nSelEquip = -1

			print("")
			oMenuEquipInfoList = CP08Utility.ConvertToMenuEquipInfos(CP08StoreInfoStorage.GetInst().GetStoreInfo(0).m_oEquipList)

	# 장비를 판매한다
	@classmethod
	def SellEquip(cls):
		nSelEquip = -1
		oMenuEquipInfoList = CP08Utility.ConvertToMenuEquipInfos(CP08UserInfoStorage.GetInst().GetUserInfo(0).m_oEquipList)

		while nSelEquip < len(oMenuEquipInfoList):
			cls.PrintSellEquipMenu(oMenuEquipInfoList)
			nSelEquip = int(input("\n판매 장비 선택 (소지 금액 : {0}) : ".format(CP08UserInfoStorage.GetInst().GetUserInfo(0).m_nNumGolds))) - 1

			# 장비를 선택했을 경우
			if nSelEquip < len(oMenuEquipInfoList):
				nNumEquips = int(input("판매 수량 입력 : "))

				# 재고가 부족 할 경우
				if oMenuEquipInfoList[nSelEquip].m_nNumEquips < nNumEquips:
					print("재고가 부족합니다.")

				else:
					print("{0} {1} 을(를) 판매했습니다.".format(oMenuEquipInfoList[nSelEquip].GetGrade(), oMenuEquipInfoList[nSelEquip].GetKinds()))

					for _ in range(0, nNumEquips):
						CP08UserInfoStorage.GetInst().GetUserInfo(0).m_nNumGolds += CP08Utility.GetPrice(oMenuEquipInfoList[nSelEquip], False)

						CP08UserInfoStorage.GetInst().GetUserInfo(0).RemoveEquipInfo(CP08EquipInfo(oMenuEquipInfoList[nSelEquip].m_nKinds, oMenuEquipInfoList[nSelEquip].m_nGrade))
						CP08StoreInfoStorage.GetInst().GetStoreInfo(0).AddEquipInfo(CP08EquipInfo(oMenuEquipInfoList[nSelEquip].m_nKinds, CP08EquipInfo.GRADE_NONE))

				nSelEquip = -1

			print("")
			oMenuEquipInfoList = CP08Utility.ConvertToMenuEquipInfos(CP08UserInfoStorage.GetInst().GetUserInfo(0).m_oEquipList)


# Practice 8 - 1
class CP08_01:
	MENU_NONE = -1
	MENU_VISIT_STORE = 0
	MENU_EXIT = 1

    # 실행한다
	@classmethod
	def Run(cls):
		cls.LoadInfos()
		nSelMenu = cls.MENU_NONE

		# 유저 정보가 없을 경우
		if not CP08UserInfoStorage.GetInst().GetUserInfo(0):
			oUserInfo = CP08UserInfo()
			oUserInfo.m_nNumGolds = int(input("초기 비용 입력 : "))

			CP08UserInfoStorage.GetInst().AddUserInfo(oUserInfo)

		while nSelMenu != cls.MENU_EXIT:
			cls.PrintMenu()
			nSelMenu = int(input("\n메인 메뉴 선택 : ")) - 1

			# 상점 방문 일 경우
			if nSelMenu == cls.MENU_VISIT_STORE:
				CP08Store.Visit()

			print("")

		cls.SaveInfos()

	# 메누를 출력한다
	@classmethod
	def PrintMenu(cls):
		print("=====> 메인 메뉴 <=====")
		print("1. 상점 방문")
		print("2. 종료")

	# 정보를 로드한다
	@classmethod
	def LoadInfos(cls):
		CP08UserInfoStorage.GetInst().LoadUserInfos()
		CP08StoreInfoStorage.GetInst().LoadStoreInfos()

	# 정보를 저장한다
	@classmethod
	def SaveInfos(cls):
		CP08UserInfoStorage.GetInst().SaveUserInfos()
		CP08StoreInfoStorage.GetInst().SaveStoreInfos()