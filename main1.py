# 세번 반복해서 출력
import sys
if len(sys.argv) > 1:
    for c in range(3):
        print(sys.argv[1])
else:
    print('There is no args. ex) python main2.py hello')