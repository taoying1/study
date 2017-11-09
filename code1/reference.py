print("Simple Assignment")
shoplist=["apple","mango","carrot","banana"]
mylist=shoplist
del shoplist[0]
print("shoplist is",shoplist)
print("mylist is",mylist)

print("Copy by making a full slice")
mylist=shoplist[:]
del mylist[0]
print("shoplist is",shoplist)
print("mylist is",mylist)

#记住列表的赋值语句不创建拷贝。你得使用切片操作符来建立序列的拷贝。