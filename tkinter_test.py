from tkinter import *

def main():
    rt=Tk()
    rt.title("My first tkinter App")
    rt.minsize(width=300,height=300)
    rt.maxsize(width=300,height=300)

    button=Button(rt,text="Click!!",width=12,height=1)
    button.pack()
    rt.mainloop()

if __name__=="__main__":
    main()
