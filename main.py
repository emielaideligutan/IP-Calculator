from tkinter import *
from tkinter import messagebox

main = Tk()

class calcu:
    def __init__(self):
        self.start = None
        self.icon()


    def icon(self):
        self.heads = Label(main, text='IP CALCULATOR',  font=('Times', 30, 'bold'), bg="skyblue")
        self.heads.pack()
        self.frame = Frame(main, padx=10, pady=30)
        Label(self.frame, text="IP ADDRESS :", font=("Times", 12), pady=10, padx=10)\
            .grid(row=1, column=0, sticky=W, padx=10, pady=10)
        Entry(self.frame, width=25,  bg='silver', fg='black',
              font=('Times', 12)).grid(row=1, column=1, padx=40, pady=10)
        Label(self.frame, text="CLASS :", font=("Times", 12), pady=10, padx=10)\
            .grid(row=2, column=0, sticky=W, padx=10, pady=10)
        Entry(self.frame, width=25, bg='silver', fg='black',
              font=('Times', 12)).grid(row=2, column=1, padx=10, pady=10)
        Label(self.frame, text="HOST :", font=("Times", 12), pady=10, padx=10) \
            .grid(row=3, column=0, sticky=W, padx=10, pady=10)
        Entry(self.frame, width=25, bg='silver', fg='black',
              font=('Times', 12)).grid(row=3, column=1, padx=10, pady=10)
        Label(self.frame, text="NETWORK :", font=("Times", 12), pady=10, padx=10) \
            .grid(row=4, column=0, sticky=W, padx=10, pady=10)
        Entry(self.frame, width=25, bg='silver', fg='black',
              font=('Times', 12)).grid(row=4, column=1, padx=10, pady=10)
        Label(self.frame, text="SUBNET MASK :", font=("Times", 12), pady=10, padx=10) \
            .grid(row=5, column=0, sticky=W, padx=10, pady=10)
        Entry(self.frame, width=25, bg='silver', fg='black',
              font=('Times', 12)).grid(row=5, column=1, padx=10, pady=10)
        Button(self.frame, text="CALCULATE", width=12, bg='skyblue', font=('Book Antiqua', 12, 'bold'), pady=2, padx=4,
               ).grid(row=6, column=0)
        self.frame.pack()

main.title("IP CALCULATOR")
main.geometry("980x600")
main.configure(width=1500,height=600,bg='skyblue')
calcu()
main.mainloop()