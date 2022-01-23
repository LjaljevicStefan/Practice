import tkinter
from tkinter import *

#definisanje globalne varijable
expression = ""

#funkcija koja azurira izraz u textbox-u
def press(num):
    #pokazuje na globalnu varijablu expression
    global expression

    if decimal['state'] == tkinter.NORMAL:
        decimal['state'] = tkinter.DISABLED
    elif num == "+" or "-" or "X" or "/" or "=" or "C":
        decimal['state'] = tkinter.NORMAL
    else:
        decimal['state'] = tkinter.DISABLED


    #sabiranje stringova
    expression = expression + str(num)

    #update izraz
    equation.set(expression)

#funkcija koja racuna konacan izraz
def equalpress():
    #try & except za hvatanje gresaka kao sto su deljenje s nulom, itd.

    try:
        global expression

        #eval pretvara u broj i sracunava izraz, str vraca u string
        total = str(eval(expression))

        #azuriram equation na total
        equation.set(total)

        #vracam izraz na prazno
        expression = total

    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

'''def switchButtonState():
    if (decimal['state'] == tkinter.NORMAL):
        decimal['state'] = tkinter.DISABLED
    elif num == '+':
        decimal['state'] = tkinter.NORMAL
    else:
        decimal['state'] = tkinter.NORMAL'''
#Driver code
if __name__ == "__main__":

    #kreiranje prozora
    prozor = Tk()

    #postavljanje boje pozadine prozora
    prozor.configure(background = "gold")

    #postavljanje teksta naslova prozora
    prozor.title("Kalkulator")

    #postavljanje dimenzija prozora
    prozor.geometry("640x480")

    #StringVar() je klasa varijabli
    #kreiranje objekta iz klase StringVar()
    equation = StringVar()  #!!!

    #kreiranje textbox-a za prikaz izraza
    expression_field = Entry(prozor, textvariable = equation)

    #grid metoda se koristi za postavljanje widgeta na svoje pozicije u prozoru
    expression_field.grid(columnspan = 4 , ipadx = 70)

    #kreiranje Button-a
    button1 = Button(prozor, text = ' 1 ', fg = 'black', bg = 'light gray', command = lambda: press(1), height = 1, width = 7)
    button1.grid(row = 2, column = 0)

    button2 = Button(prozor, text = ' 2 ', fg = 'black', bg = 'light gray', command = lambda: press(2), height = 1, width = 7)
    button2.grid(row = 2, column = 1)

    button3 = Button(prozor, text=' 3 ', fg='black', bg='light gray', command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(prozor, text=' 4 ', fg='black', bg='light gray', command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(prozor, text=' 5 ', fg='black', bg='light gray', command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(prozor, text=' 6 ', fg='black', bg='light gray', command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(prozor, text=' 7 ', fg='black', bg='light gray', command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(prozor, text=' 8 ', fg='black', bg='light gray', command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(prozor, text=' 9 ', fg='black', bg='light gray', command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(prozor, text=' 0 ', fg='black', bg='light gray', command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(prozor, text=' + ', fg='black', bg='light gray', command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(prozor, text=' - ', fg='black', bg='light gray', command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(prozor, text=' X ', fg='black', bg='light gray', command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(prozor, text=' / ', fg='black', bg='light gray', command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(prozor, text=' = ', fg='black', bg='light gray', command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(prozor, text=' C ', fg='black', bg='light gray', command=clear, height=1, width=7)
    clear.grid(row=5, column=1)

    decimal = Button(prozor, text=' . ', fg='black', bg='light gray', command=lambda: press('.'), height=1, width=7)
    decimal.grid(row=6, column=0)

    #pokreni graficki interfejs
    prozor.mainloop()