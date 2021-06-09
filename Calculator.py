from tkinter import *
root = Tk()

root.geometry("444x630")
root.title("My_Calculator")

def click(event):
    global sc_value
    text = event.widget.cget("text")

    if text == "=":
        if sc_value.get().isdigit():
            value = int(sc_value.get())

        else:
            try:
                value = eval(sc_value.get())
            
            except Exception as e:
                print(e)
                value = "Error"
        
        sc_value.set(value)
        screen.update

    elif text == "C":
        sc_value.set(" ")
        screen.update()

    else:
        sc_value.set(sc_value.get() + text)
        screen.update()


sc_value = StringVar()
sc_value.set("")
screen = Entry(root, textvariable=sc_value, font="lucida 30 bold")
screen.pack(padx=76, pady=10)

frame = Frame(root,bg="grey")
b1 = Button(frame, text="C", padx=3, pady=12, font="lucida 20 bold", bg="orange", fg="white")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)

b1 = Button(frame, text="%", padx=6, pady=12, font="lucida 20 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)

b1 = Button(frame, text="pow()", padx=1, pady=12, font="lucida 15 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)
b1 = Button(frame, text="/", padx=9, pady=10, font="lucida 20 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)


frame.pack()

frame = Frame(root,bg="grey")
b1 = Button(frame, text="7", padx=10, pady=12, font="lucida 20 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)

b1 = Button(frame, text="8", padx=10, pady=12, font="lucida 20 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)

b1 = Button(frame, text="9", padx=10, pady=12, font="lucida 20 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)

b1 = Button(frame, text="*", padx=10, pady=12, font="lucida 20 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)

frame.pack()

frame = Frame(root,bg="grey")
b1 = Button(frame, text="4", padx=10, pady=12, font="lucida 20 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)

b1 = Button(frame, text="5", padx=10, pady=12, font="lucida 20 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)

b1 = Button(frame, text="6", padx=10, pady=12, font="lucida 20 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)
b1 = Button(frame, text="-", padx=10, pady=12, font="lucida 21 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)

frame.pack()

frame = Frame(root,bg="grey")
b1 = Button(frame, text="1", padx=10, pady=12, font="lucida 20 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)

b1 = Button(frame, text="2", padx=9, pady=12, font="lucida 20 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)

b1 = Button(frame, text="3", padx=9, pady=12, font="lucida 20 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)

b1 = Button(frame, text="+", padx=9, pady=12, font="lucida 20 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)

frame.pack()

frame = Frame(root,bg="grey")
b1 = Button(frame, text="00", padx=2, pady=12, font="lucida 22 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)

b1 = Button(frame, text="0", padx=10, pady=12, font="lucida 20 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)

b1 = Button(frame, text=".", padx=11, pady=12, font="lucida 20 bold")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)

b1 = Button(frame, text="=", padx=9, pady=12, font="lucida 20 bold", bg="purple", fg="white")
b1.bind('<Button-1>', click)
b1.pack(side=LEFT, padx=7, pady=10)

frame.pack()
root.mainloop()

# To pursue a challenging career and be a part of progressive organization that gives a scope to enhance my
#  knowledge and utilizing my skills towards the growth of the organization.