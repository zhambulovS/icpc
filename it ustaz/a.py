#template by Sulia
# import sys
import math
# import bisect
# from collections import defaultdict, deque
# from heapq import heappop, heappush
# from itertools import permutations, combinations\
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
    t=sint()
    s=lst()
    mx=max(s)
    c=0
    res=0
    for i in range(2, int(mx**0.5)+1):
        x=0
        for j in s:
            if j%i==0:
                x+=1 
        if c<x:
            res=i 
            c=x
    print(res)

if __name__ == "__main__":
    solve()
# 4
# 1 2 3 4