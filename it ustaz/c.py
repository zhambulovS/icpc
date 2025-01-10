#template by Sulia
# import sys
import math
# import bisect
# from collections import defaultdict, deque
# from heapq import heappop, heappush
from itertools import permutations, combinations
# from numba import njit
from functools import lru_cache
sint=lambda: int(input())
mint=lambda: map(int, input().split())
lst=lambda: list(map(int, input().split()))
# MOD = int(1e7)
# PI = 3.141592653589793
# INF = float('inf')
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
# @njit
@lru_cache(maxsize=128, typed=False)
def solve():
    cord=[]
    t=sint()
    res=0
    n=list(range(1, t+1))
    for _ in range(t):
        l,r=mint()
        cord.append([l,r])
    for i in permutations(n):
        for k in range(len(i)):
            res+=  math.sqrt((cord[k-1][0] - cord[k][0])**2 + (cord[k-1][1] - cord[k][1])**2)

    print(res, res/t)
    

if __name__ == "__main__":
    solve()
# 3
# 0 0
# 1 0
# 0 1
#  math.sqrt((cord[i][0] - cord[i + 1][0])**2 + (cord[i][1] - cord[i + 1][1])**2)