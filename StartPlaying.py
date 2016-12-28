import Tkinter as tk
#import PIL
from PIL import Image


def doNothing():
    return 0


def crop(image):
    box = cropwindow()
    IM = Image.open(image)
    IM.crop(box)
    IM.save(image + 'crop.png')
    print 'image saved'

def cropwindow():
    cropmaster = tk.Tk()
    print 'looping'
    cropmaster.mainloop()
    print 'reached main loop'
    box = (0,0, 10, 10)
    return box


def drawCanvas(photo, master):  # Draws canvas with photo and creates menu and buttons

    window = tk.Canvas(master, width=photo.width(), height=photo.height()+50)
    window.create_image(0,50, image=photo, anchor=tk.NW)

    menu = tk.Menu(master)
    fileMenu = tk.Menu(menu, tearoff=0)  # Creates file menu
    fileMenu.add_command(label="Open", command=doNothing)
    fileMenu.add_command(label="Save", command=doNothing)
    fileMenu.add_command(label="Quit", command=quit)
    menu.add_cascade(label='File', menu=fileMenu)

    master.config(menu=menu)
    #Creates button to Quit program
    quitButton = tk.Button(master, text="Quit", command=quit, anchor=tk.W, )
    quitButton.configure(width=5, activebackground="#aaaaaa", relief=tk.GROOVE)
    window.create_window(10, 10, anchor=tk.NW, window=quitButton)

    #Creates button for crop
    cropButton = tk.Button(master, text="Crop", command=lambda: crop('bb8.gif'), anchor=tk.W)
    cropButton.configure(width=5, activebackground="#aaaaaa", relief=tk.GROOVE)
    window.create_window(60, 10, anchor=tk.NW, window=cropButton)

    window.pack()


def main():

    master = tk.Tk()
    photo = tk.PhotoImage(file='bb8.gif')
    drawCanvas(photo, master)
    tk.mainloop()



if __name__ == '__main__':
    main()

