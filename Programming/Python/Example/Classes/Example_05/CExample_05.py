import os
import sys

# Example 5
class CExample_05:
	# 초기화
	@classmethod
	def Start(cls, args):
		cls.E05_01(args)

	# 5 - 1
	@classmethod
	def E05_01(cls, args):
		pass


# 메인 모듈 일 경우
if __name__ == "__main__":
	CExample_05.Start(sys.argv)
	