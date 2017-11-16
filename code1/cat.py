import sys
def readfile(filename):
    f=open(filename)
    while(True):
        line=f.readline()
        if len(line)==0:
            break
        print(line)
    f.close()

if len(sys.argv)<2:
    print("NO action")
    sys.exit()

if sys.argv[1].startswith("--"):
    option=sys.argv[1][2:]
    if option=="version":
        print("version 12")
    elif option=="help":
        print("long")
    else:
        print("unknown")
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)