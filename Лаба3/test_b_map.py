from btree_map import BinaryTreeMap

my_map = BinaryTreeMap()

print("Добавим элементы и найдем их по их ключам:")
my_map.insert(5, "five")
my_map.insert(3, "three")
my_map.insert(7, "seven")
my_map.insert(1, "one")
my_map.insert(9, "nine")
print(my_map.search(5))
print(my_map.search(3))
print(my_map.search(7))
print(my_map.search(1))
print(my_map.search(9))

print("Проверим дерево на пустоту:")
print(my_map.is_empty())

print("Обойдем дерево в прямом порядке:")
preorder_traversal = my_map.preorder_traversal(my_map.root)
for node in preorder_traversal:
    print(node.key, node.value)

print("Обойдем дерево в обратном порядке:")
postorder_traversal = my_map.postorder_traversal(my_map.root)
for node in postorder_traversal:
    print(node.key, node.value)

print("Обойдем дерево в симметричном порядке:")
inorder_traversal = my_map.inorder_traversal(my_map.root)
for node in inorder_traversal:
    print(node.key, node.value)

print("Очистим дерево и проверим, очистилось ли оно:")
my_map.clear()
print(my_map.is_empty())