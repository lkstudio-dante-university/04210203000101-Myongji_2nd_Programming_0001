import os
import sys

from E06_01.CE06_01 import *
from E06_02.CE06_02 import *
from E06_03.CE06_03 import *

# Example 6
class CExample_06:
    # 초기화
	@classmethod
	def Start(cls, args):
		# cls.E06_01(args)
		# cls.E06_02(args)
		cls.E06_03(args)

	# 6 - 1
	@classmethod
	def E06_01(cls, args):
		oExample = CE06_01()
		oExample.Run()

	# 6 - 2
	@classmethod
	def E06_02(cls, args):
		oExample = CE06_02()
		oExample.Run()

	# 6 - 3
	@classmethod
	def E06_03(cls, args):
		oExample = CE06_03()
		oExample.Run()


# 메인 모듈 일 경우
if __name__ == "__main__":
	CExample_06.Start(sys.argv)
	