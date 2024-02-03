from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")
frame1 = Frame(root)
frame1.pack()
titlelabel = Label(frame1,text = "Tic Tac Toe",font = ("arial",30),bg = "yellow")
titlelabel.pack()
frame2 = Frame(root)
frame2.pack()



board = {1:" ",2:" ",3:" ",
         4:" ",5:" ",6:" ",
         7:" ",8:" ",9:" " }
# main function

turn = "X"

def checkforwin(player):
    if board[1] == board[2]and board[1] == board[3] and board[3]==  player:
        return True
    elif board[1] == board[4]and board[1] == board[7] and board[7]==  player:
        return True
    elif  board[1] == board[5]and board[1] == board[9] and board[9]==  player:
        return True
    elif  board[2] == board[5]and board[2] == board[8] and board[8]==  player:
        return True
    elif board[4] == board[5]and board[4] == board[6] and board[6]==  player:
        return True
    elif  board[7] == board[8]and board[7] == board[9] and board[9]==  player:
        return True
    elif  board[3] == board[6]and board[3] == board[9] and board[9]==  player:
        return True
    elif  board[3] == board[5]and board[3] == board[7] and board[7]==  player:
        return True
    else:
        return False

def play(event):
    global turn 
    button = event.widget
    buttontext = str(button)
    clicked = buttontext[-1]
    if clicked == "n":
        clicked = 1 
    else : 
        clicked = int(clicked)
    print((clicked))
    if button["text" ] == " ":
        if turn == "X":
            button["text"] = "X"
            board[clicked] = turn   
            if checkforwin(turn):
                print(turn,'win the game ')
                print('Game over')     
                exit()     
            turn = "O"
        else:
            button["text"] = "O"
            board[clicked] = turn 
            if checkforwin(turn):
                print(turn,'win the game ')
                print('Game over')
                exit()
            turn = "X"
    print(board)
    
    # if board != " ":
        # exit()
# Tic Tac Toe Board


#First row
button1 = Button(frame2,text = " ",width = 4,height = 2,font = ("Arial",35))
button1.grid(row=0,column = 0)
button1.bind("<Button-1>",play)

button2 = Button(frame2,text = " ",width = 4,height = 2,font = ("Arial",35))
button2.grid(row=0,column = 1)
button2.bind("<Button-1>",play)

button3 = Button(frame2,text = " ",width = 4,height = 2,font = ("Arial",35))
button3.grid(row=0,column = 2)
button3.bind("<Button-1>",play)

#SECOND ROW

button4 = Button(frame2,text = " ",width = 4,height = 2,font = ("Arial",35))
button4.grid(row=1,column = 0)
button4.bind("<Button-1>",play)

button5 = Button(frame2,text = " ",width = 4,height = 2,font = ("Arial",35))
button5.grid(row=1,column = 1)
button5.bind("<Button-1>",play)

button6 = Button(frame2,text = " ",width = 4,height = 2,font = ("Arial",35))
button6.grid(row=1,column = 2)
button6.bind("<Button-1>",play)

#THIRD ROW

button7 = Button(frame2,text = " ",width = 4,height = 2,font = ("Arial",35))
button7.grid(row=2,column = 0)
button7.bind("<Button-1>",play)

button8 = Button(frame2,text = " ",width = 4,height = 2,font = ("Arial",35))
button8.grid(row=2,column = 1)
button8.bind("<Button-1>",play)

button9 = Button(frame2,text = " ",width = 4,height = 2,font = ("Arial",35))
button9.grid(row=2,column = 2)
button9.bind("<Button-1>",play)

root.mainloop()
