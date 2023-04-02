from hash_map import HashMap

hm = HashMap()

print("Добавим элементы apple, banana, cherry, pear, grape с ключами k1, k2, k3, k4, k5 соответственно")
hm.add('k1', 'apple')
hm.add('k2', 'banana')
hm.add('k3', 'cherry')
hm.add('k4', 'pear')
hm.add('k5', 'grape')
print(hm.get('k1'))  
print(hm.get('k2'))
print(hm.get('k3'))
print(hm.get('k4'))
print(hm.get('k5'))
print("Число элементов:", hm.__len__())
print()

print("Добавим элемент pineapple с ключом k6")
hm.add('k6', 'pineapple')
print(hm.get('k1'))  
print(hm.get('k2'))
print(hm.get('k3'))
print(hm.get('k4'))
print(hm.get('k5'))
print(hm.get('k6'))
print("Число элементов:", hm.__len__())
print()

print("Удалим элемент apple с ключом k1 и проверим, есть ли он в списке")
hm.delete('k1')
print(hm.get('k1'))
print(hm.get('k2'))
print(hm.get('k3'))
print(hm.get('k4'))
print(hm.get('k5'))
print(hm.get('k6'))
print("Число элементов:", hm.__len__())
print()

print("Добавим элемент orange с ключом k1")
hm.add('k1', 'orange')
print(hm.get('k1'))
print(hm.get('k2'))
print(hm.get('k3'))
print(hm.get('k4'))
print(hm.get('k5'))
print(hm.get('k6'))
print("Число элементов:", hm.__len__())
print()

print("Проверим, есть ли в списке элемент с ключом k7")
print(hm.__contains__('k7'))
print()

print("Очистим список и проверим, очистился ли он, вызвав один из элементов")
hm.clear()  
print(hm.get('k1'))  