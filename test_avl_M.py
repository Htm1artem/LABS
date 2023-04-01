from avlMap import AVLMap

map = AVLMap()

print("Добавим в дерево элементы one, two, three, four, five с ключами 1, 2, 3, 4, 5 соответственно") 
map.add(1, 'one')
map.add(2, 'two')
map.add(3, 'three')
map.add(4, 'four')
map.add(5, 'five')
print(map.get(1))  
print(map.get(2)) 
print(map.get(3))
print(map.get(4))  
print(map.get(5))  

print("Поменяем значение two на new two, а значение five на new five")
map.update(2, 'new two')
map.update(5, 'new five')
print(map.get(1)) 
print(map.get(2)) 
print(map.get(3))
print(map.get(4))  
print(map.get(5))  

print("Проверим очередь на пустоту")
print(map.is_empty())

print("Удалим все элементы и проверим очередь на пустоту")
map.delete_all()
print(map.is_empty())
