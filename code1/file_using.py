poem='''Programming is fun
When the work is done
if you wanna make your work also fun:
        use Python!'''

f=open('poem.txt','w') #创建并打开文件
f.write(poem)
f.close()

f=open('poem.txt','r')
while(True):
    line=f.readline()
    if len(line)==0:
        break
    print (line,end=' ')
f.close()

#print语句用end=' ' 遇到空格不换行
