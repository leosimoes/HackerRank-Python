"""
    Author: Leonardo Simoes
    Date: 07/13/2023
    HackerRank - Python - Basic Data Types - Finding the percentage
    Language: Python 3
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    mean = sum(student_marks[query_name])/len(student_marks[query_name])

    print(f'{mean:,.2f}')