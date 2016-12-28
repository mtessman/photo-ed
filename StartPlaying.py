import Tkinter as tk

def main():
    master = tk.Tk()

    photo = tk.PhotoImage(file = 'bb8.gif')
    window = tk.Canvas(master, width=photo.width(), height=photo.height() + 50)
    window.create_image(0,50, image=photo, anchor=tk.NW)

    quitButton = tk.Button(master, text="Quit", command=quit, anchor=tk.W, )
    quitButton.configure(width=5, activebackground="#aaaaaa", relief=tk.GROOVE)
    window.create_window(10, 10, anchor=tk.NW, window=quitButton)

    window.pack()

    tk.mainloop()

if __name__ == '__main__':
    main()

