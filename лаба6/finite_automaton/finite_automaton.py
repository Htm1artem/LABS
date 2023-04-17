def finite_automaton(text, pattern):
    m = len(pattern)
    n = len(text)
    automaton = [[0] * 256 for _ in range(m + 1)]
    j = 0
    for i in range(m):
        for k in range(256):
            automaton[i][k] = automaton[j][k]
        automaton[i][ord(pattern[i])] = i + 1
        if i < m - 1:
            j = automaton[j][ord(pattern[i])]
    indexes = []
    j = 0
    for i in range(n):
        j = automaton[j][ord(text[i])]
        if j == m:
            indexes.append(i - m + 1)
    return indexes