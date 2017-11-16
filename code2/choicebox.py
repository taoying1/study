import easygui
flavor=easygui.choicebox("what is your favorite ice cream flavor?",choices=['Vanilla','Chocolate','Strawberry'])
easygui.msgbox("You picked "+flavor)