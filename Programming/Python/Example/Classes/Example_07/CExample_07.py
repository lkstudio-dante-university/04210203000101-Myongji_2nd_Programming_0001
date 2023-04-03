import os
import sys

from E07_01.CE07_01 import *

# Example 7
class CExample_07:
    # 초기화
	@classmethod
	def Start(cls, args):
		cls.E07_01(args)

	# 7 - 1
	@classmethod
	def E07_01(cls, args):
		pass


# 메인 모듈 일 경우
if __name__ == "__main__":
	CExample_07.Start(sys.argv)
	