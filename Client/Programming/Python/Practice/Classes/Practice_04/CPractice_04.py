import os
import sys
import random

# Practice 4
class CPractice_04:
	# 초기화
	@classmethod
	def Start(cls, args):
		oAnswer = []
		cls.SetupAnswer(oAnswer)

		nTryTimes = 0
		print("정답 : {0}\n".format(oAnswer))

		print(random.sample(range(1, 10), 4))

		while True:
			oTokenList = input("숫자 (4 개) 입력 : ").split()
			nTryTimes += 1
			
			nNumBalls = 0
			nNumStrikes = 0

			for i in range(0, len(oAnswer)):
				oDigit = str(oAnswer[i])

				nNumBalls += 1 if oDigit in oTokenList and i != oTokenList.index(oDigit) else 0
				nNumStrikes += 1 if oDigit in oTokenList and i == oTokenList.index(oDigit) else 0
					

			print("결과 : {0} Strike, {1} Ball\n".format(nNumStrikes, nNumBalls))

			# 게임이 종료 되었을 경우
			if nNumStrikes >= len(oAnswer):
				break

		print("{0} 번 시도 끝에 성공했습니다.".format(nTryTimes))


	# 정답을 설정한다
	@classmethod
	def SetupAnswer(cls, a_oAnswer:list):
		while len(a_oAnswer) < 4:
			nVal = random.randint(1, 9)

			# 중복 값이 없을 경우
			if nVal not in a_oAnswer:
				a_oAnswer.append(nVal)


# 메인 모듈 일 경우
if __name__ == "__main__":
	CPractice_04.Start(sys.argv)
	