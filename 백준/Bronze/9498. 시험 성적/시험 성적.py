import sys

score = int(sys.stdin.readline())

score_std = score // 10

if score_std == 9 or score_std == 10:
    print('A')
elif score_std == 8:
    print('B')
elif score_std == 7:
    print('C')
elif score_std == 6:
    print('D')
else:
    print('F')
