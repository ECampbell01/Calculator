from tkinter import *

def button_pressed(num):

    global equation_string
    equation_string = equation_string + str(num)
    equation_label.set(equation_string)

def equals():

    global equation_string

    try:
        total = str(eval(equation_string))
        equation_label.set(total)
        equation_string = total

    except ZeroDivisionError:
        equation_label.set("Mathmatical error")
        equation_string = ""

    except SyntaxError:
        equation_label.set("Syntax error")
        equation_string = ""

def clear():

    global equation_string
    equation_label.set("")
    equation_string = ""

window = Tk()
window.title("Calculator")
window.geometry("500x520")
window.config(background = "white")

equation_string = ""
equation_label = StringVar()

label = Label(window, textvariable = equation_label,
              font = ('Arial', 20), bg = 'white', width = 27, height = 2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text = 1, height = 3, width = 9, font = 35,
                 command = lambda: button_pressed(1))
button1.grid(row = 0, column = 0)

button2 = Button(frame, text = 2, height = 3, width = 9, font = 35,
                 command = lambda: button_pressed(2))
button2.grid(row = 0, column = 1)

button3 = Button(frame, text = 3, height = 3, width = 9, font = 35,
                 command = lambda: button_pressed(3))
button3.grid(row = 0, column = 2)

button4 = Button(frame, text = 4, height = 3, width = 9, font = 35,
                 command = lambda: button_pressed(4))
button4.grid(row = 1, column = 0)

button5 = Button(frame, text = 5, height = 3, width = 9, font = 35,
                 command = lambda: button_pressed(5))
button5.grid(row = 1, column = 1)

button6 = Button(frame, text = 6, height = 3, width = 9, font = 35,
                 command = lambda: button_pressed(6))
button6.grid(row = 1, column = 2)

button7 = Button(frame, text = 7, height = 3, width = 9, font = 35,
                 command = lambda: button_pressed(7))
button7.grid(row = 2, column = 0)

button8 = Button(frame, text = 8, height = 3, width = 9, font = 35,
                 command = lambda: button_pressed(8))
button8.grid(row = 2, column = 1)

button9 = Button(frame, text = 9, height = 3, width = 9, font = 35,
                 command = lambda: button_pressed(9))
button9.grid(row = 2, column = 2)

button0 = Button(frame, text = 0, height = 3, width = 9, font = 35,
                 command = lambda: button_pressed(0))
button0.grid(row = 3, column = 0)

buttonplus = Button(frame, text = '+', height = 3, width = 9, font = 35,
                 command = lambda: button_pressed('+'))
buttonplus.grid(row = 0, column = 3)

buttonminus = Button(frame, text = '-', height = 3, width = 9, font = 35,
                 command = lambda: button_pressed('-'))
buttonminus.grid(row = 1, column = 3)

buttonmultiply = Button(frame, text = '*', height = 3, width = 9, font = 35,
                 command = lambda: button_pressed('*'))
buttonmultiply.grid(row = 2, column = 3)

buttondivide = Button(frame, text = '/', height = 3, width = 9, font = 35,
                 command = lambda: button_pressed('/'))
buttondivide.grid(row = 3, column = 3)

buttonequal = Button(frame, text = '=', height = 3, width = 9, font = 35,
                 command = equals)
buttonequal.grid(row = 3, column = 2)

buttondecimal = Button(frame, text = '.', height = 3, width = 9, font = 35,
                 command = lambda: button_pressed('.'))
buttondecimal.grid(row = 3, column = 1)

buttonclear = Button(window, text = 'Clear', height = 3, width = 12, font = 35,
                 command = clear)
buttonclear.pack()

window.mainloop()