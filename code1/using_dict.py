#'ab' is short for 'a'ddress'b'ook
ab={'Swaroop':'swaroop@byteofpython.info',
    'Larry':'larry@wall.org',
    'Spammer':'spammer@hotmail.com'}
print("Swaroop's address is %s"%ab['Swaroop'])

ab['Guido']='guide@python.org'
del ab['Spammer']
print("\nThere are %d contacts in the address-book\n"%len(ab))
for name,address in ab.items():
    print("Contact %s at %s"%(name,address))
if 'Guido' in ab.keys():
    print("\nGuido's address is %s"%ab['Guido'])

#字典的items方法，来使用字典中的每个键/值对。会返回一个元组的列表，其中每个元组都包含一对项目——键与对应的值。
#字典的keys方法，来检验一个键/值对是否存在