import os
import sys

# Example 7 - 1
class CE07_01:
    # 실행한다
	@classmethod
	def Run(cls):
		CE07UserInfoStorage.GetInst()
	

# 유저 정보 저장소
class CE07UserInfoStorage:
	m_oInst = None

	# 초기화
	def __init__(self):
		self.m_nNumGolds = 0

	# 인스턴스를 반환한다
	@classmethod
	def GetInst(cls):
		# 인스턴스가 없을 경우
		if cls.m_oInst == None:
			cls.m_oInst = CE07UserInfoStorage()
			
		return cls.m_oInst
	