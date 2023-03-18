import os
import sys

# Example 4
class CExample_04:
    # 초기화
	@classmethod
	def Start(cls, args):
		print("Hello, World!")

# 메인 모듈 일 경우
if __name__ == "__main__":
	CExample_04.Start(sys.argv)
	