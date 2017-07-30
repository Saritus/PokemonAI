# Load csv file

from Tkinter import *
from PIL import ImageTk, Image
import PIL


class App:
    def __init__(self, master):
        # Frame
        frame = Frame(master)
        frame.pack()

        # Image
        self.canvas1 = Canvas(master)
        self.canvas1.pack(side=BOTTOM)
        self.change_image(self.canvas1)

        # Buttons
        self.accept = Button(frame, text="Accept", command=self.change_image, width=10)
        self.accept.pack(side=LEFT)

    def change_image(self, canvas):
        # Get image
        pilImage = PIL.Image.open("Sprites/100.PNG").resize((500, 500), PIL.Image.ANTIALIAS)

        # Change canvas size
        canvas.config(width=pilImage.width, height=pilImage.height)
        imagesprite = canvas.create_image(pilImage.width / 2, pilImage.height / 2)

        # Show image on canvas
        self.image = ImageTk.PhotoImage(pilImage)
        canvas.itemconfig(imagesprite, image=self.image)
        return imagesprite


def main():
    root = Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
