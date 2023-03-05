from tkinter import *

app = Tk()
output_text: str = ""
screen: Label = None
btn_frame = Frame()

my_font = ("",18,'bold')

def delete_onclick() -> None:
    global output_text
    global screen
    output_text = output_text[:-1]
    screen.config(text = output_text)

def delete_all_onclick() -> None:
    global output_text
    global screen
    output_text = ""
    screen.config(text = output_text)

def click_listner(val: int) -> None:
    global output_text
    global screen
    output_text = output_text + str(val)
    screen.config(text = output_text)

def add_oper_buttons(app: Tk) -> None:
    opp_btns: Button = [None] * 4
    opp = ["+","-","*","/"]
    for i in range(0,4):
        opp_btns[i] = Button(app, text = opp[i], width = 4, height = 2,
                     command = lambda a = opp[i]: click_listner(a),
                     background="orange",font = my_font)
        opp_btns[i].grid(row = i, column = 3)
    equal =  Button(app, text = '=', width = 10, height = 2,
                    command = lambda a = opp[i]: click_listner(a),
                    background="orange",font = my_font)
    equal.grid(row=4,column=0,columnspan=2)


def add_num_buttons(app: Tk) -> None:
    global output_text
    num_btns: Button = [None] * 10
    c: int = 1
    num_btns[0] = Button(app, text ="0", width = 4, height = 2,
                     command = lambda a = 0: click_listner(a),
                     background="orange",font = my_font)
    num_btns[0].grid(row = 3,column = 0)
    for i in range(0,3):
        for j in range(0,3):
            num_btns[c] = Button(app, text = f"{c}", width = 4, height = 2,
                             command = lambda a = c: click_listner(a),
                             background="orange",font = my_font)
            num_btns[c].grid(row = i, column = j)
            c = c + 1
    dot = Button(app, text =".", width = 10, height = 2,
                     command = lambda a = 0: click_listner(a),
                     background="orange",font = my_font)
    dot.grid(row = 3,column = 1,columnspan=2)

def add_del_buttons(app: Tk) -> None:
    del_btn = Button(app, text ="C", width = 4, height = 2,
                     command = delete_onclick,
                     background="orange",font = my_font)
    del_btn.grid(row=4,column=3)
    del_all_btn = Button(app, text ="AC", width = 4, height = 2,
                     command = delete_all_onclick,
                     background="orange",font = my_font)
    del_all_btn.grid(row=4,column=2)
    
    
def create_output_screen() -> None:
    global screen
    global app
    screen = Label(app, text = output_text, height = 5,width=5, font = my_font)
    screen.grid(column = 0, row = 4, columnspan = 3)

def main() -> None:
    global app
    app.geometry("350x500")
    app.title("Basic Calculator")
    app.resizable(height = False, width = False)
    add_num_buttons(app)
    add_oper_buttons(app)
    add_del_buttons(app)

    app.mainloop()
    
main()