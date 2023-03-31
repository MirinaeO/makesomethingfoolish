#가위바위보는 정말 real 트루 공정한 게임인가?

import random

RSP = ['rock', 'scissor', 'paper'] #바위 : 0 가위 : 1 보 : 2
rcplist = []
n = 0
for i in range(1000000000):
    v = random.randrange(0, 3)
    s = random.randrange(0, 3)

    if v == s:
        a = ("무승부")
    elif v==0 and s==1:
        a = ("v 승")
    elif v==0 and s==2:
        a = ("s 승")
    elif v==1 and s==0:
        a = ("s 승")
    elif v==1 and s==2:
        a = ("v 승")
    elif v==2 and s==0:
        a = ("v 승")
    elif v==2 and s==1:
        a = ("s 승")
    rcplist.append(a)
    n = n + 1
print("v 승 수 : " + str(rcplist.count("v 승")))
print("s 승 수 : " + str(rcplist.count("s 승")))
print("무승부 수 : " + str(rcplist.count("무승부")))