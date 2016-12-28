import Tkinter as tk

def main():
    master = tk.Tk()
    photo = tk.PhotoImage(file = 'bb8.gif')
    window = tk.Canvas(master, width=photo.width(), height=photo.height())
    window.create_image(photo.width()/2,photo.height()/2, image=photo)
    window.pack()
    tk.mainloop()

if __name__ == '__main__':
    main()

