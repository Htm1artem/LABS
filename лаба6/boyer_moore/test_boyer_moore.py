from boyer_moore import boyer_moore

text = "abcabcabcabc"
print("Текст:", text)
pattern = "abc"
indexes = boyer_moore(text, pattern)
print("Идексы", pattern, ":", indexes)
print()

text = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15"
print("Текст:", text)
pattern = "1"
indexes = boyer_moore(text, pattern)
print("Идексы", pattern, ":", indexes)
print()

text = "The quick brown fox jumps over the lazy dog"
print("Текст:", text)
pattern = "fox"
indexes = boyer_moore(text, pattern)
print("Идексы", pattern, ":", indexes)