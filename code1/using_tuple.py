zoo=("wolf","elephant","penguin")
print("Number of animals in the zoo is",len(zoo))

new_zoo=("monkey","dolphin",zoo)
print("Number of animals in the new zoo is",len(new_zoo))
print("All animals in new zoo is",new_zoo)
print("Animals brought from old zoo are",new_zoo[2])
print("Last animals brought from old zoo is",new_zoo[2][2])

#一个空的元组由一对空的圆括号组成。然而，含有单个元素的元组就不那么简单了。你必须在第一个（唯一一个）项目后跟一个逗号，这样Python才能区分元组和表达式中一个带圆括号的对象。