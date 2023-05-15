import os
import sys

from Practice.Classes.Practice_08.CP08EquipInfo import *


# 유저 정보
class CP08UserInfo:
	# 초기화
	def __init__(self, a_oUserInfo: str = None):
		self.__init__user_info__()
		
		# 유저 정보가 유효 할 경우
		if a_oUserInfo:
			oTokenList = a_oUserInfo.split(",")
			self.m_nNumGolds = int(oTokenList[0])
			
			for i in range(2, len(oTokenList), 2):
				self.m_oEquipList.append(CP08EquipInfo(int(oTokenList[i]), int(oTokenList[i + 1])))
	
	# 초기화
	def __init__user_info__(self):
		self.m_nNumGolds = 0
		self.m_oEquipList = []
	
	# 장비 정보를 추가한다
	def AddEquipInfo(self, a_oEquipInfo: CP08EquipInfo):
		self.m_oEquipList.append(a_oEquipInfo)
	
	# 장비 정보를 제거한다
	def RemoveEquipInfo(self, a_oEquipInfo: CP08EquipInfo):
		for i in range(0, len(self.m_oEquipList)):
			# 종류와 등급이 동일 할 경우
			if a_oEquipInfo.m_nKinds == self.m_oEquipList[i].m_nKinds and a_oEquipInfo.m_nGrade == self.m_oEquipList[i].m_nGrade:
				del self.m_oEquipList[i]
				break
	
	# 유저 정보를 저장한다
	def SaveUserInfo(self, a_oOutUserInfoList: list):
		oStoreInfo = "{0},{1}".format(self.m_nNumGolds, len(self.m_oEquipList))
		
		for oEquipInfo in self.m_oEquipList:
			oStoreInfo += ",{0}".format(oEquipInfo.GetEquipInfo())
		
		a_oOutUserInfoList.append(oStoreInfo)


# 유저 정보 저장소
class CP08UserInfoStorage:
	m_oInst = None
	FILE_PATH_USER_INFOS = "Resources/Practice_08/P08UserInfos.txt"
	
	# 초기화
	def __init__(self):
		self.__init__user_info_storage__()
	
	# 초기화
	def __init__user_info_storage__(self):
		self.m_oUserInfoList = []
	
	# 유저 정보를 반환한다
	def GetUserInfo(self, a_nIdx: int):
		return self.m_oUserInfoList[a_nIdx] if a_nIdx >= 0 and a_nIdx < len(self.m_oUserInfoList) else None
	
	# 유저 정보를 추가한다
	def AddUserInfo(self, a_oUserInfo: CP08UserInfo):
		self.m_oUserInfoList.append(a_oUserInfo)
	
	# 유저 정보를 로드한다
	def LoadUserInfos(self):
		# 유저 정보가 존재 할 경우
		if os.path.isfile(CP08UserInfoStorage.FILE_PATH_USER_INFOS):
			with open(CP08UserInfoStorage.FILE_PATH_USER_INFOS, "r") as oRStream:
				for oUserInfo in oRStream.readlines():
					self.m_oUserInfoList.append(CP08UserInfo(oUserInfo))
	
	# 유저 정보를 저장한다
	def SaveUserInfos(self):
		# 디렉토리가 없을 경우
		if not os.path.isdir(os.path.dirname(CP08UserInfoStorage.FILE_PATH_USER_INFOS)):
			os.makedirs(os.path.dirname(CP08UserInfoStorage.FILE_PATH_USER_INFOS))
		
		with open(CP08UserInfoStorage.FILE_PATH_USER_INFOS, "w") as oWStream:
			oUserInfoList = []
			
			for oUserInfo in self.m_oUserInfoList:
				oUserInfo.SaveUserInfo(oUserInfoList)
			
			oWStream.writelines(oUserInfoList)
	
	# 인스턴스를 반환한다
	@classmethod
	def GetInst(cls):
		# 인스턴스가 없을 경우
		if cls.m_oInst == None:
			cls.m_oInst = CP08UserInfoStorage()
		
		return cls.m_oInst
