# Load csv file

from Tkinter import *
from PIL import ImageTk, Image


class App:
    def __init__(self, master):
        # Frame
        frame = Frame(master)
        frame.pack(side=BOTTOM)

        # Buttons
        self.move1 = Button(
            frame, text="Attack 1",
            command=self.change_image, width=20
        ).grid(row=0, column=0)
        self.move2 = Button(
            frame, text="Attack 2",
            command=self.change_image, width=20
        ).grid(row=0, column=1)
        self.move3 = Button(
            frame, text="Attack 3",
            command=self.change_image, width=20
        ).grid(row=1, column=0)
        self.move4 = Button(
            frame, text="Attack 4",
            command=self.change_image, width=20
        ).grid(row=1, column=1)

        # Image
        self.canvas1 = Canvas(master)
        self.canvas1.pack(side=BOTTOM)
        self.change_image(self.canvas1)

    def change_image(self, canvas):
        # Get image
        pilImage = Image.open("Sprites/100.PNG").resize((500, 500), Image.ANTIALIAS)

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
