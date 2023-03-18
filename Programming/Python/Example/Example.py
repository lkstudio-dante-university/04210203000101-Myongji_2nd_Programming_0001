"""
import 키워드는 특정 Python 모듈을 포함 시키는 역할을 수행한다.
"""
import os
import sys

from Classes.Example_03.CExample_03 import *
from Classes.Example_04.CExample_04 import *

"""
메인 모듈이란?
- Python 은 프로그램이 실행 될 때 가장 처음 실행 할 진입 함수 (메서드) 가 따로 존재하지 않는다.
따라서, 어떤 파일이 먼저 실행되느냐에 따라 결과가 달라지기 때문에 사용자 (프로그래머) 가 임의적으로 진입 함수를 만들어 줄 필요가 있다.

Python 인터프리터는 가장 먼저 실행되는 파일의 모듈 이름을 __main__ 으로 지정하기 때문에 해당 특징을 활용하면 진입 함수 역할을 하는
파일을 제작하는 것이 가능하다.
"""
# 메인 모듈 일 경우
if __name__ == "__main__":
    CExample_03.Start(sys.argv)
    # CExample_04.Start(sys.argv)
    