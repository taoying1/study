class ShortInputException(Exception):
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast
try:
    s=input("Enter something:")
    if len(s)<3:
        raise ShortInputException(len(s),3)
except EOFError:
    print("why")
except ShortInputException as x:
    print("length %d,les %d"%(x.length,x.atleast))
else:
    print("Done")