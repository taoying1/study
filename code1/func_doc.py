def printMax(x,y):
    '''prints the maximum of two numbers.

    The two values must be integers.'''
    x=int(x)
    y=int(y)
    if x>y:
        print(x,"is maximum")
    else:
        print(y,"is maximum")
printMax(3,5)
print (printMax.__doc__)

#文档字符串的惯例是一个多行字符串，它的首行以大写字母开始，句号结尾。第二行是空行，从第三行开始是详细的描述。