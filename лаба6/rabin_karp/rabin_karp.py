def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)
    d = 256  
    q = 101  
    h = pow(d, m-1) % q
    p = 0 
    t = 0  
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(text[i])) % q
    indexes = []
    for i in range(n-m+1):
        if p == t:
            if pattern == text[i:i+m]:
                indexes.append(i)
        if i < n-m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q
    return indexes