## Пример использования:

```
tree = BinarySearchTree()

tree.insert(5, 'five')
tree.insert(1, 'one')
tree.insert(10, 'ten')
tree.insert(6, 'six')
```

```
print('search 6:', tree.search(6)) # search 6: six

print('height:', tree.height()) # height: 3

print('balanced:', tree.is_balanced()) # balanced: True

tree.delete(5)

print('delete 3:', tree.search(3)) # delete 3: None
```
