def say(message,times=1):
    print(message*times)
say("Hi",5)
say("world")

#只有在形参表末尾的那些参数可以有默认参数值
#def func(a, b=5)是有效的，但是def func(a=5, b)是 无效 的