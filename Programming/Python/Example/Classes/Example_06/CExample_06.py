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
		# CE06_01.Run()
		# CE06_02.Run()
		CE06_03.Run()


# 메인 모듈 일 경우
if __name__ == "__main__":
	CExample_06.Start(sys.argv)
	