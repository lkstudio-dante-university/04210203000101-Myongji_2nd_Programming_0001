import os
import sys

from P08_01.CP08_01 import *

# Practice 8
class CPractice_08:
    # 초기화
	@classmethod
	def Start(cls, args):
		CP08_01.Run()


# 메인 모듈 일 경우
if __name__ == "__main__":
	CPractice_08.Start(sys.argv)
	