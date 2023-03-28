from pr_Q import PriorityQueue

pq = PriorityQueue()

print("Добавим элементы 5, 8, 19, 11, 4")
pq.add(5)
pq.add(8)
pq.add(19)
pq.add(11)
pq.add(6)
pq.add(4)

print("Текущий список элементов:", pq.container)
print("Количество элементов в очереди:", pq.get_length())
print("Максимальный элемент в очереди:", pq.get_max())
print()

print("Удалим элементы 5 и 19")
pq.delete(5)
pq.delete(19)

print("Текущий список элементов:", pq.container)
print("Количество элементов в очереди:", pq.get_length())
print("Максимальный элемент в очереди:", pq.get_max())
print()

print("Добавим элементы 20 и 1")
pq.add(20)
pq.add(1)

print("Текущий список элементов:", pq.container)
print("Количество элементов в очереди:", pq.get_length())
print("Максимальный элемент в очереди:", pq.get_max())