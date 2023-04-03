import os
import sys

from E06_01.CE06_01 import *

# Example 6
class CExample_06:
    # 초기화
	@classmethod
	def Start(cls, args):
		cls.E06_01(args)

	# 6 - 1
	@classmethod
	def E06_01(cls, args):
		pass


# 메인 모듈 일 경우
if __name__ == "__main__":
	CExample_06.Start(sys.argv)
	