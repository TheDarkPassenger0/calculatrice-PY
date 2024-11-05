from tkinter import *
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculatrice by TheDarkPassenger")
        master.resizable(False, False)

        
        self.screen = Entry(master, width=30, font=('Arial', 16))
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        
        r = 1  
        c = 0
        for b in buttons:
            cmd = lambda x=b: self.action(x)
            Button(master, text=b, width=5, height=2, font=('Arial', 12), command=cmd).grid(row=r, column=c, padx=5, pady=5)
            c += 1
            if c > 3:
                c = 0
                r += 1

    def action(self, key):
        if key == '=':
            try:
                result = eval(self.screen.get())
                self.screen.delete(0, END)
                self.screen.insert(END, str(result))
            except:
                self.screen.delete(0, END)
                self.screen.insert(END, "Erreur")
        elif key == 'C':
            self.screen.delete(0, END)
        else:
            self.screen.insert(END, key)

root = Tk()
app = Calculator(root)
root.mainloop()
