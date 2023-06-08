"""
    Author: Leonardo Simoes
    Date: 06/02/2023
    HackerRank - Python - Introductions - Python If-Else
"""

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0 or n in range(6,21,2):
        print('Weird')
    else:
        print('Not Weird')