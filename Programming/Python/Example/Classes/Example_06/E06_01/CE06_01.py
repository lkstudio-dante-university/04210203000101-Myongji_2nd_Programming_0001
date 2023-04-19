import os
import sys
import time

# Example 6 - 1
class CE06_01:
    # 실행한다
	@classmethod
	def Run(cls):
		oTokenList01 = input("플레이어 스탯 입력 (체력, 공격력, 방어력) : ").split()
		oTokenList02 = input("적 스탯 입력 (체력, 공격력, 방어력) : ").split()

		oPlayer = CE06Unit("플레이어", int(oTokenList01[0]), int(oTokenList01[1]), int(oTokenList01[2]))
		oEnemy = CE06Unit("적", int(oTokenList02[0]), int(oTokenList02[1]), int(oTokenList02[2]))

		while True:
			print("\n=====> 플레이어 공격 <=====")
			oPlayer.Attack(oEnemy)

			# 적 체력이 없을 경우
			if oEnemy.m_nHP <= 0:
				break

			print("\n=====> 적 공격 <=====")
			oEnemy.Attack(oPlayer)

			# 플레이어 체력이 없을 경우
			if oPlayer.m_nHP <= 0:
				break

			time.sleep(1)

		print("\n{0} 이(가) 이겼습니다.".format(oPlayer.m_oName if oPlayer.m_nHP > 0 else oEnemy.m_oName))
		
		
# 유닛
class CE06Unit:
	# 초기화
	def __init__(self, a_oName:str, a_nHP:int, a_nATK:int, a_nDEF:int):
		self.m_nHP = a_nHP
		self.m_nATK = a_nATK
		self.m_nDEF = a_nDEF
		self.m_oName = a_oName

	# 공격한다
	def Attack(self, a_oTarget):
		nDamage = max(0, self.m_nATK - a_oTarget.m_nDEF)
		a_oTarget.m_nHP -= nDamage

		print("{0} 에게 {1} 피해를 입혔습니다.".format(a_oTarget.m_oName, nDamage))
