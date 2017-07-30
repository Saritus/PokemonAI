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
        self.canvas = Canvas(master)
        self.canvas.pack(side=BOTTOM)
        self.change_image()

        # Buttons
        self.accept = Button(frame, text="Accept", command=self.change_image, width=10)
        self.accept.pack(side=LEFT)

    def change_image(self):
        # Get image
        pilImage = PIL.Image.open("Sprites/100.PNG")

        # Change canvas size
        self.canvas.config(width=pilImage.width, height=pilImage.height)
        self.imagesprite = self.canvas.create_image(pilImage.width / 2, pilImage.height / 2)

        # Show image on canvas
        self.image = ImageTk.PhotoImage(pilImage)
        self.canvas.itemconfig(self.imagesprite, image=self.image)
        return self.imagesprite


def main():
    root = Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
