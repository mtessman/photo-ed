import Tkinter as tk

def doNothing():
    return 0

def main():
    master = tk.Tk()
    photo = tk.PhotoImage(file = 'bb8.gif')
    window = tk.Canvas(master, width=photo.width(), height=photo.height()+50)
    window.create_image(0,50, image=photo, anchor=tk.NW)

    menu = tk.Menu(master)
    fileMenu = tk.Menu(menu, tearoff=0)
    fileMenu.add_command(label="Open", command=doNothing)
    fileMenu.add_command(label="Save", command=doNothing)
    fileMenu.add_command(label="Quit", command=quit)

    menu.add_cascade(label='File', menu=fileMenu)

    button1 = tk.Button(master, text="Quit", command=quit, anchor=tk.W)
    button1.configure(width=5, background="#FFFFFF", relief=tk.FLAT)
    window.create_window(10, 10, anchor=tk.NW, window=button1)
    master.config(menu=menu)
    window.pack()

    tk.mainloop()

if __name__ == '__main__':
    main()

