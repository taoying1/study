def func():
    global x
    print("x is",x)
    x=2
    print("Change local x to", x)
x=50
func()
print("x still is",x)
