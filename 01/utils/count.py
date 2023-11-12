from .function import add

def count_word(s, a):
    n = 0
    for i in range(len(s)):
        if s[i] == a:
            n = add(n, 1)
    
    return n