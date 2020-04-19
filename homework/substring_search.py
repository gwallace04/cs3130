"""
A small program to find a substring in a given string and return the number of
successful and unsuccessful matches
Author: Gabriel Wallace
"""

def string_match(text: str, sub: str) -> dict:
    matches = {'index': 0, 'successful': 0, 'unsuccessful': 0}
    n = len(text)
    m = len(sub)
    for i in range (n - m):
        j = 0
        while j < m and sub[j] == text[i + j]:
            j += 1
            matches['successful'] += 1
        if j == m:
            matches['index'] = i
            return matches
        else:
            matches['unsuccessful'] += 1
    matches['index'] = -1
    return matches

def count_substrings(text: str, start = 'A', end = 'B') -> int:
    count = 0
    n = len(text)
    for i in range(n):
        if text[i] == start:
            for j in range(i, n):
                if text[j] == end:
                    count += 1
    return count

if __name__ == "__main__":
    a = "ABCDABCDABCDABXD"
    b = "ABX"
    print(string_match(a, b))
    print(count_substrings("CABAAXBYB"))
    print(count_substrings("ABBB"))
    
