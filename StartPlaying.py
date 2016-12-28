import Tkinter as tk

def main():
    master = tk.Tk()

    photo = tk.PhotoImage(file = 'bb8.gif')
    window = tk.Canvas(master, width=photo.width(), height=photo.height() + 50)
    window.create_image(0,50, image=photo, anchor=tk.NW)

    button1 = tk.Button(master, text="Quit", command=quit, anchor=tk.W)
    button1.configure(width=10, activebackground="#33B5E5", relief=tk.FLAT)
    window.create_window(10, 10, anchor=tk.NW, window=button1)

    window.pack()

    tk.mainloop()

if __name__ == '__main__':
    main()

