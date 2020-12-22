# 입력받은 모든 args출력
import sys
if len(sys.argv) > 1:
    for c in sys.argv[1:]:
        print(c)
else:
    print('There is no args. ex) python main2.py hello bye')