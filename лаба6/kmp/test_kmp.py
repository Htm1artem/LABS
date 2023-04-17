from kmp import kmp
text = "AABAACAADAABAABA"
print("Текст:", text)
pattern = "AABA"
indexes = kmp(text, pattern)
print("Индексы", pattern, ":", indexes)
print()

text = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
print("Текст:", text)
pattern = "ж"
indexes = kmp(text, pattern)
print("Индексы", pattern, ":", indexes)
print()

text = "Триста тысяч часов за спиною Триста тысяч планет надо мною Не устал ли Создатель их в небе кружить? Каждый раз просыпаясь с рассветом Неспроста вспоминаешь об этом Очень здорово всё-таки жить!"
print("Текст:", text)
pattern = "та"
indexes = kmp(text, pattern)
print("Индексы", pattern, ":", indexes)
print()