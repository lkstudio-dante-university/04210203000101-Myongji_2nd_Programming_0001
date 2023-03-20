import os
import sys

# Example 4
class CExample_04:
    # 초기화
	@classmethod
	def Start(cls, args):
		cls.E04_01(args)
		cls.E04_02(args)
		cls.E04_03(args)

	# 4 - 1
	@classmethod
	def E04_01(cls, args):
		pass

	# 4 - 2
	@classmethod
	def E04_02(cls, args):
		oTokenList = input("정수 (2 개) 입력 : ").split()

		nLhs = int(oTokenList[0])
		nRhs = int(oTokenList[1])

		print("=====> 산술 연산자 <=====")
		print(f"{nLhs} + {nRhs} = {nLhs + nRhs}")
		print(f"{nLhs} - {nRhs} = {nLhs - nRhs}")
		print(f"{nLhs} * {nRhs} = {nLhs * nRhs}")
		print(f"{nLhs} / {nRhs} = {nLhs / nRhs}")
		print(f"{nLhs} % {nRhs} = {nLhs % nRhs}")
		print(f"{nLhs} ** {nRhs} = {nLhs ** nRhs}")
		print(f"{nLhs} // {nRhs} = {nLhs // nRhs}")

		print("\n=====> 관계 연산자 <=====")
		print(f"{nLhs} < {nRhs} = {nLhs < nRhs}")
		print(f"{nLhs} > {nRhs} = {nLhs > nRhs}")
		print(f"{nLhs} <= {nRhs} = {nLhs <= nRhs}")
		print(f"{nLhs} >= {nRhs} = {nLhs >= nRhs}")
		print(f"{nLhs} == {nRhs} = {nLhs == nRhs}")
		print(f"{nLhs} != {nRhs} = {nLhs != nRhs}")

		print("\n=====> 논리 연산자 <=====")
		print(f"{nLhs} and {nRhs} = {nLhs and nRhs}")
		print(f"{nLhs} or {nRhs} = {nLhs or nRhs}")
		print(f"not {nLhs} = {not nLhs}")

		print("\n=====> 비트 연산자 <=====")
		print(f"{nLhs:08b} & {nRhs:08b} = {nLhs & nRhs:08b}")
		print(f"{nLhs:08b} | {nRhs:08b} = {nLhs | nRhs:08b}")
		print(f"{nLhs:08b} ^ {nRhs:08b} = {nLhs ^ nRhs:08b}")
		print(f"~{nLhs:08b} = {~nLhs:08b}")
		print(f"{nLhs:08b} << 1 = {nLhs << 1:08b}")
		print(f"{nLhs:08b} >> 1 = {nLhs >> 1:08b}")

	# 4 - 3
	@classmethod
	def E04_03(cls, args):
		pass
	

# 메인 모듈 일 경우
if __name__ == "__main__":
	CExample_04.Start(sys.argv)
	