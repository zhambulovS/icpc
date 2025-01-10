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
    last=''
    q=True
    c=True
    cities=[]
    for _ in range(sint()):
        if q:
            s=input().lower()
            cities.append(s)
            last=s[-1]
            q=False 
            continue
        s=input().lower()
        if last==s[0] and s not in cities:
            last=s[-1]
            cities.append(s)
        else:
            c=False
            break
    print('Yes' if c else 'No') 

if __name__ == "__main__":
    solve()
# 4
# 1 2 3 4