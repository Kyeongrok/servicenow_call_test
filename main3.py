# 입력받은 모든 args를 파일로 출력
import sys
if len(sys.argv) > 1:
    with open('print.log', 'w+') as f:
        for c in sys.argv[1:]:
            f.write(c)
else:
    print('There is no args. ex) python main2.py hello bye')