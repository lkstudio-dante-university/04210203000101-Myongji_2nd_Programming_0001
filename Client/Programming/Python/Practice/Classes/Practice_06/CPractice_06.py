import os
import sys

from P06_01.CP06_01 import *

# Practice 6
class CPractice_06:
    # 초기화
	@classmethod
	def Start(cls, args):
		CP06_01.Run()


# 메인 모듈 일 경우
if __name__ == "__main__":
	CPractice_06.Start(sys.argv)
	