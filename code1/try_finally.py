try:
    f=open("poem.txt")
    while(True):
        data=f.readline()
        if len(data)==0:
            break
        print(data,end='' )
finally:
    f.close()
    print("Done")