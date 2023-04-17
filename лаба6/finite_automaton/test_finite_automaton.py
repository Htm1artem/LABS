from finite_automaton import finite_automaton
text = "12345678910121314151617181920212223242526272829303132"
print("Текст:", text)
pattern = "2"
indexes = finite_automaton(text, pattern)
print("Индексы", pattern, ":", indexes)
print()

text = "Carl stole the corals from Clara, and Clara stole the clarinet from Carl. Queen Clara severely punished Cavalier Charles for stealing corals!"
print("Текст:", text)
pattern = "Carl"
indexes = finite_automaton(text, pattern)
print("Индексы", pattern, ":", indexes)
print()

text = "I have a pen I have an apple Ah Apple pen I have a pen I have pineapple Ah Pineapple pen Apple pen Pineapple pen Ah Pen Pie Pineapple Apple Pen Pen Pie Pineapple Apple Pen"
print("Текст:", text)
pattern = "pen"
indexes = finite_automaton(text, pattern)
print("Индексы", pattern, ":", indexes)
print()