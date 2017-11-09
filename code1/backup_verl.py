#需要备份的文件和目录由一个列表指定。
#备份应该保存在主备份目录中。
#文件备份成一个zip文件。
#zip存档的名称是当前的日期和时间
# coding=gbk
import os
import time
source_dir=r'E:\1'

target_dir=r'E:\backup'
today=target_dir+ os.sep+time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')


if not os.path.exists(today):
    os.mkdir(today)
comment=input("Enter a comment-->")
if comment==0:
    target = today + os.sep + now + '.rar'
else:
    target = today + os.sep + now+'_'+comment.replace(' ', '_') + '.rar'

rar_command= r'"C:\Program Files (x86)\WinRAR\WinRAR.exe" A %s %s -r' % (target,source_dir)
if os.system(rar_command)== 0:
    print("Successful backup to",target)
else:
    print("Backup Failed.")

#要将WinRAR的路径放到你的环境变量里面，然后才能直接使用WinRAR命令行。
#或者加上WinRAR的安装路径像这样：rar_command = r'"C:\Program Files\WinRAR\WinRAR.exe" A %s %s -r' % (target,source)
#Windows把反斜杠（\）作为目录分隔符，而Python用反斜杠表示转义符！使用'C:\\Documents'或r'C:\Documents'而不是'C:\Documents'
#os.sep变量的用法——根据你的操作系统给出目录分隔符
#os.path.exists函数检验在主备份目录中是否有以当前日期作为名称的目录。如果没有，我们使用os.mkdir函数创建。
#comment.replace(' ', '_')将字符串中的空格替换成下划线。
