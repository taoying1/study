name='Swarooop'
if name.startswith('Swa'):
    print("Yes, the string starts with 'Swa'")
if 'a' in name:
    print("Yes, it contains the string 'a'")
if name.find('war')!=-1:
    print("Yes, it contains the string 'war'")
delimeter='_*_'
print(delimeter.join(name))
mylist=['Brazil','Russia','India','China']
print(delimeter.join(mylist))

#startswith方法是用来测试字符串是否以给定字符串开始。in操作符用来检验一个给定字符串是否为另一个字符串的一部分。
#find方法用来找出给定字符串在另一个字符串中的位置，或者返回-1以表示找不到子字符串。