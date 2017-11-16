#解压后，将easygui.py拷贝进入python安装目录Lib\site-packages.
#cmd进入easygui的文件目录，运行python setup.py install.
guess=int(input("Which multiplication table would you like?"))
i=int(input("How high do you want to go?"))
print("Here's your table:")
for i in range(1,i+1):
    print("%d*%d=%d"%(guess,i,i*guess))
    i+=1