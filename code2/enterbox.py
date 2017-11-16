import easygui
flavor=easygui.enterbox("What is your favorite ice cream flavor?",default="vanilla")
print(easygui.msgbox("You enter "+flavor))