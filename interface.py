# Load csv file

from Tkinter import *
from PIL import ImageTk, Image


class App:
    def __init__(self, master):
        # Attacks
        attacks = Frame(master)
        attacks.grid(row=2)

        # Buttons
        self.move1 = Button(
            attacks, text="Attack 1",
            command=self.change_image, width=20
        ).grid(row=0, column=0)
        self.move2 = Button(
            attacks, text="Attack 2",
            command=self.change_image, width=20
        ).grid(row=0, column=1)
        self.move3 = Button(
            attacks, text="Attack 3",
            command=self.change_image, width=20
        ).grid(row=1, column=0)
        self.move4 = Button(
            attacks, text="Attack 4",
            command=self.change_image, width=20
        ).grid(row=1, column=1)

        # Opponent
        opponent = Frame(master)
        opponent.grid(row=0)

        self.o_infos = Label(opponent, text="Opponent")
        self.o_infos.pack(side=RIGHT)
        self.o_canvas = Canvas(opponent)

        self.o_img = Image.open("Sprites/110.PNG")
        self.o_photo = ImageTk.PhotoImage(self.o_img)
        self.o_canvas.create_image(20, 20, image=self.o_photo)
        self.o_canvas.pack(side=LEFT)

        # Current
        current = Frame(master)
        current.grid(row=1)

        self.c_infos = Label(current, text="Current")
        self.c_infos.pack(side=LEFT)
        self.c_canvas = Canvas(current)

        self.c_img = Image.open("Sprites/100.PNG")
        self.c_photo = ImageTk.PhotoImage(self.c_img)
        self.c_canvas.create_image(20, 20, image=self.c_photo)
        self.c_canvas.pack(side=RIGHT)

    def change_image(self):
        return


def main():
    root = Tk()
    App(root)
    root.configure(background='white')

    root.mainloop()


if __name__ == "__main__":
    main()
