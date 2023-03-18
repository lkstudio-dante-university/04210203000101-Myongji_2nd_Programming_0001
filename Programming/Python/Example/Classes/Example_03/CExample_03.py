import os
import sys

# Example 3
class CExample_03:
    # 초기화
	@classmethod
	def Start(cls, args):
		print("수식 입력 : ", end = "")
		oTokenList = input().split()

		nLhs = int(oTokenList[0])
		nRhs = int(oTokenList[2])

		# + 일 경우
		if oTokenList[1] == "+":
			print(f"{nLhs} + {nRhs} = {nLhs + nRhs}")
		# - 일 경우
		elif oTokenList[1] == "-":
			print(f"{nLhs} - {nRhs} = {nLhs - nRhs}")
		# * 일 경우
		elif oTokenList[1] == "*":
			print(f"{nLhs} * {nRhs} = {nLhs * nRhs}")
		# / 일 경우
		elif oTokenList[1] == "/":
			print(f"{nLhs} / {nRhs} = {nLhs / nRhs}")
		
# 메인 모듈 일 경우
if __name__ == "__main__":
	CExample_03.Start(sys.argv)
	