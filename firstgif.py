from tkinter import *
from PIL import Image

root = Tk()

root.attributes('-fullscreen', True)

root.config(background='#d9d9d9')

gifImage = "gifs//Miss-ezgif.com-crop.gif"

openImage = Image.open(gifImage)

frames = openImage.n_frames

imageObject = [PhotoImage(file= gifImage, format=f"gif -index {i}") for i in range(frames)]

count = 0

showAnimation = None

def animation(count):

    global showAnination

    newImage = imageObject[count]

    gif_Label.configure(image=newImage)
    gif_Label.place(x=(root.winfo_width() - newImage.width()) // 2, y=(root.winfo_height() - newImage.height()) // 2, width=newImage.width(), height=newImage.height())

    count += 1

    if count == frames:

        count = 0

    showAnimation = root.after(40, lambda: animation(count))

gif_Label = Label(root, image="")

gif_Label. place(x=15, y=20, width=450, height=500)

animation(count)

root.mainloop()