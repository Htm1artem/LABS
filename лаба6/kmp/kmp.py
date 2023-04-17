def kmp(text, pattern):
    n = len(text)
    m = len(pattern)
    j = 0
    k = -1
    next = [-1] * m
    while j < m - 1:
        if k == -1 or pattern[j] == pattern[k]:
            j += 1
            k += 1
            if pattern[j] != pattern[k]:
                next[j] = k
            else:
                next[j] = next[k]
        else:
            k = next[k]
    j = 0
    k = 0
    indexes = []
    while j < n:
        if k == -1 or text[j] == pattern[k]:
            j += 1
            k += 1
        else:
            k = next[k]
        if k == m:
            indexes.append(j - m)
            k = next[k - 1]
    return indexes