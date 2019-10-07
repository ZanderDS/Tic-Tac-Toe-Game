# Tic Tac Toe

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Tic Tac Toe")
window.geometry('500x500')

rows = 0
while rows < 16:
    window.rowconfigure(rows, weight=1)
    rows += 1
columns = 0
while columns < 7:
    window.columnconfigure(columns, weight=1)
    columns += 1
curr_player = True

btn1_text = tk.StringVar()
btn2_text = tk.StringVar()
btn3_text = tk.StringVar()
btn4_text = tk.StringVar()
btn5_text = tk.StringVar()
btn6_text = tk.StringVar()
btn7_text = tk.StringVar()
btn8_text = tk.StringVar()
btn9_text = tk.StringVar()
winner_text = tk.StringVar()


def btnReset():
    global curr_player
    btn1_text.set("")
    btn2_text.set("")
    btn3_text.set("")
    btn4_text.set("")
    btn5_text.set("")
    btn6_text.set("")
    btn7_text.set("")
    btn8_text.set("")
    btn9_text.set("")
    winner_text.set("")
    curr_player = True
    for x in list:
        x.config(state='enabled')


def gameWon():
    for x in list:
        x.config(state='disabled')


def checkGameWon():

    if (btn1_text.get() == btn2_text.get()) and (btn2_text.get() == btn3_text.get()):
        if (btn1_text.get() != ""):
            winner_text.set("The winner is " + btn2_text.get())
            gameWon()

    if (btn4_text.get() == btn5_text.get()) and (btn5_text.get() == btn6_text.get()):
        if (btn4_text.get() != ""):
            winner_text.set("The winner is " + btn5_text.get())
            gameWon()

    if (btn7_text.get() == btn8_text.get()) and (btn8_text.get() == btn9_text.get()):
        if (btn7_text.get() != ""):
            winner_text.set("The winner is " + btn8_text.get())
            gameWon()

    if (btn1_text.get() == btn4_text.get()) and (btn4_text.get() == btn7_text.get()):
        if (btn1_text.get() != ""):
            winner_text.set("The winner is " + btn4_text.get())
            gameWon()

    if (btn2_text.get() == btn5_text.get()) and (btn5_text.get() == btn8_text.get()):
        if (btn2_text.get() != ""):
            winner_text.set("The winner is " + btn5_text.get())
            gameWon()

    if (btn3_text.get() == btn6_text.get()) and (btn6_text.get() == btn9_text.get()):
        if (btn3_text.get() != ""):
            winner_text.set("The winner is " + btn6_text.get())
            gameWon()

    if (btn1_text.get() == btn5_text.get()) and (btn5_text.get() == btn9_text.get()):
        if (btn1_text.get() != ""):
            winner_text.set("The winner is " + btn5_text.get())
            gameWon()

    if (btn3_text.get() == btn5_text.get()) and (btn5_text.get() == btn7_text.get()):
        if (btn3_text.get() != ""):
            winner_text.set("The winner is " + btn5_text.get())
            gameWon()


def onClick(btn, plr):
    global curr_player
    if (btn == "1"):
        if btn1_text.get() == 'X' or btn1_text.get() == 'O':
            return
        if (plr == True):
            btn1_text.set("X")
            curr_player = False
        else:
            btn1_text.set("O")
            curr_player = True
    elif (btn == "2"):
        if btn2_text.get() == 'X' or btn2_text.get() == 'O':
            return
        if (plr == True):
            btn2_text.set("X")
            curr_player = False
        else:
            btn2_text.set("O")
            curr_player = True
    elif (btn == "3"):
        if btn3_text.get() == 'X' or btn3_text.get() == 'O':
            return
        if (plr == True):
            btn3_text.set("X")
            curr_player = False
        else:
            btn3_text.set("O")
            curr_player = True
    elif (btn == "4"):
        if btn4_text.get() == 'X' or btn4_text.get() == 'O':
            return
        if (plr == True):
            btn4_text.set("X")
            curr_player = False
        else:
            btn4_text.set("O")
            curr_player = True
    elif (btn == "5"):
        if btn5_text.get() == 'X' or btn5_text.get() == 'O':
            return
        if (plr == True):
            btn5_text.set("X")
            curr_player = False
        else:
            btn5_text.set("O")
            curr_player = True
    elif (btn == "6"):
        if btn6_text.get() == 'X' or btn6_text.get() == 'O':
            return
        if (plr == True):
            btn6_text.set("X")
            curr_player = False
        else:
            btn6_text.set("O")
            curr_player = True
    elif (btn == "7"):
        if btn7_text.get() == 'X' or btn7_text.get() == 'O':
            return
        if (plr == True):
            btn7_text.set("X")
            curr_player = False
        else:
            btn7_text.set("O")
            curr_player = True
    elif (btn == "8"):
        if btn8_text.get() == 'X' or btn8_text.get() == 'O':
            return
        if (plr == True):
            btn8_text.set("X")
            curr_player = False
        else:
            btn8_text.set("O")
            curr_player = True
    elif (btn == "9"):
        if btn9_text.get() == 'X' or btn9_text.get() == 'O':
            return
        if (plr == True):
            btn9_text.set("X")
            curr_player = False
        else:
            btn9_text.set("O")
            curr_player = True
    checkGameWon()


window.configure(background='darkblue')

Label1 = tk.Label(window, height=2, textvariable=winner_text,
                  font=('Helvetica', '20'), bg="darkblue", fg="white")
Label1.grid(column=2, row=0, columnspan=3,
            rowspan=2, sticky=('w', 'e', 'n', 's'))

style = ttk.Style(window)
style.theme_use('clam')
style.configure('TButton', state='disabled', bordercolor="blue", bg="white",
                fg="blue", font=('Helvetica', '30'), height=2, weight=1)
style.configure('my.TButton', state='disabled', bordercolor="blue", bg="white",
                fg="blue", font=('Helvetica', '30'), width=2, height=2)

Button1 = ttk.Button(window, textvariable=btn1_text,
                     command=lambda: onClick("1", curr_player), style='my.TButton')
Button1.grid(column=2, row=2, rowspan=3, sticky=('w', 'e', 'n', 's'))
Button2 = ttk.Button(window, textvariable=btn2_text,
                     command=lambda: onClick("2", curr_player), style='my.TButton')
Button2.grid(column=3, row=2, rowspan=3, sticky=('w', 'e', 'n', 's'))
Button3 = ttk.Button(window, textvariable=btn3_text,
                     command=lambda: onClick("3", curr_player), style='my.TButton')
Button3.grid(column=4, row=2, rowspan=3, sticky=('w', 'e', 'n', 's'))
Button4 = ttk.Button(window, textvariable=btn4_text,
                     command=lambda: onClick("4", curr_player), style='my.TButton')
Button4.grid(column=2, row=5, rowspan=3, sticky=('w', 'e', 'n', 's'))
Button5 = ttk.Button(window, textvariable=btn5_text,
                     command=lambda: onClick("5", curr_player), style='my.TButton')
Button5.grid(column=3, row=5, rowspan=3, sticky=('w', 'e', 'n', 's'))
Button6 = ttk.Button(window, textvariable=btn6_text,
                     command=lambda: onClick("6", curr_player), style='my.TButton')
Button6.grid(column=4, row=5, rowspan=3, sticky=('w', 'e', 'n', 's'))
Button7 = ttk.Button(window, textvariable=btn7_text,
                     command=lambda: onClick("7", curr_player), style='my.TButton')
Button7.grid(column=2, row=8, rowspan=3, sticky=('w', 'e', 'n', 's'))
Button8 = ttk.Button(window, textvariable=btn8_text,
                     command=lambda: onClick("8", curr_player), style='my.TButton')
Button8.grid(column=3, row=8, rowspan=3, sticky=('w', 'e', 'n', 's'))
Button9 = ttk.Button(window, textvariable=btn9_text,
                     command=lambda: onClick("9", curr_player), style='my.TButton')
Button9.grid(column=4, row=8, rowspan=3, sticky=('w', 'e', 'n', 's'))

ButtonReset = ttk.Button(window, text='Reset',
                         command=lambda: btnReset(), style='TButton')
ButtonReset.grid(column=2, row=11, columnspan=3,
                 rowspan=3, sticky=('w', 'e', 'n', 's'))

Label2 = tk.Label(window, height=2, font=('Helvetica', '20'), bg="darkblue")
Label2.grid(column=2, row=14, columnspan=3,
            rowspan=2, sticky=('w', 'e', 'n', 's'))

list = [Button1, Button2, Button3, Button4,
        Button5, Button6, Button7, Button8, Button9]

window.mainloop()
