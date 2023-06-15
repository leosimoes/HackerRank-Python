"""
    Author: Leonardo Simoes
    Date: 06/15/2023
    HackerRank - Python - Basic Data Types - Tuples
    Language: Pypy 3
"""

if __name__ == '__main__':
    n = int(input())
    t = tuple(map(int, input().split()))
    print(hash(t))