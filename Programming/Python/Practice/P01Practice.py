import os
import sys

sys.path.append(os.getcwd().replace("\\", "/"))

from Practice.Classes.Practice_04.CPractice_04 import *
from Practice.Classes.Practice_06.CPractice_06 import *
from Practice.Classes.Practice_08.CPractice_08 import *
from Practice.Classes.Practice_10.CPractice_10 import *
from Practice.Classes.Practice_12.CPractice_12 import *
from Practice.Classes.Practice_15.CPractice_15 import *

# 메인 모듈 일 경우
if __name__ == "__main__":
	# CPractice_04.Start(sys.argv)
	# CPractice_06.Start(sys.argv)
	# CPractice_08.Start(sys.argv)
	# CPractice_10.Start(sys.argv)
	CPractice_12.Start(sys.argv)
	# CPractice_15.Start(sys.argv)
