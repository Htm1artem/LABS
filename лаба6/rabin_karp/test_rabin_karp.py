from rabin_karp import rabin_karp

text = "The quick brown fox jumps over the lazy dog"
print("Текст:", text)
pattern = "fox"
indexes = rabin_karp(text, pattern)
print("Индексы", pattern, ":", indexes)
print()

text = "123 45646 12366 512363 324123"
print("Текст:", text)
pattern = "123"
indexes = rabin_karp(text, pattern)
print("Индексы", pattern, ":", indexes)
print()

text = "Всем привет, всем хорошего дня, всем счастья, здоровья и любви!"
print("Текст:", text)
pattern = "всем"
indexes = rabin_karp(text, pattern)
print("Индексы", pattern, ":", indexes)
print()

text = "Яблоко, банан, груша, банан. слива, виноград, 123, банан, Банан"
print("Текст:", text)
pattern = "банан"
indexes = rabin_karp(text, pattern)
print("Индексы", pattern, ":", indexes)