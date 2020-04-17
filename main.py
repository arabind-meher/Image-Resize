import os
from os import listdir
from os.path import isfile, exists, join
import cv2
from tkinter import *
from tkinter import ttk, filedialog

IMAGE_EXTENSIONS = ['bmp', 'pbm', 'pgm', 'ppm', 'sr', 'ras', 'jpeg', 'jpg', 'jpe', 'jp2', 'tiff', 'tif', 'png']


class ImageResize:
    """Image Resize"""

    # Resize Image to a given Ratio.
    @staticmethod
    def image_resize_ratio(path, ratio):
        # Create an 'Output' Directory path
        output_path = join(path, 'Output')

        # Check if the Directory already existed
        if not exists(output_path):
            # Create Directory
            os.mkdir(output_path)
            print('Directory Created')
        else:
            print('Directory Already Exist')

        # List all the files present in the Directory
        files = [file for file in listdir(path)
                 if isfile(join(path, file)) and file[0] != '.' and file.split('.')[-1] in IMAGE_EXTENSIONS]
        print(files)

        # Convert each file one-by-one
        for file in files:
            image = cv2.imread(join(path, file), cv2.IMREAD_UNCHANGED)
            h, w, d = image.shape
            print(image.shape)

            dimension = (int(w * ratio), int(h * ratio))
            resized_image = cv2.resize(image, dimension, interpolation=cv2.INTER_CUBIC)
            print(resized_image.shape)

            # Save the Resized Image to 'Output' Directory
            cv2.imwrite(join(output_path, file), resized_image)

    # Resize Image to given Width and Height
    @staticmethod
    def image_resize_pixel(path, width, height):
        # Create an 'Output' Directory path
        output_path = join(path, 'Output')

        # Check if the Directory already existed
        if not exists(output_path):
            # Create Directory
            os.mkdir(output_path)
            print('Directory Created')
        else:
            print('Directory Already Exist')

        # List all the files present in the Directory
        files = [file for file in listdir(path)
                 if isfile(join(path, file)) and file[0] != '.' and file.split('.')[-1] in IMAGE_EXTENSIONS]
        for file in files:
            image = cv2.imread(join(path, file), cv2.IMREAD_UNCHANGED)
            print(image.shape)

            dimension = (width, height)
            resized_image = cv2.resize(image, dimension, interpolation=cv2.INTER_CUBIC)
            print(resized_image.shape)

            cv2.imwrite(join(output_path, file), resized_image)


class GUI:
    """Graphics User Interface"""

    def __init__(self):
        # Create a Graphics Window
        root = Tk()
        root.title('Image Resize')
        root.geometry('500x500')

        ttk.Separator(root).pack(fill=X)

        Label(
            root,
            text='Image Resize',
            font=('hack', 18, 'bold')
        ).pack(fill=X)

        ttk.Separator(root).pack(fill=X)

        Label(
            root,
            text='File Location:',
            font=('bitstream vera sans', 12)
        ).place(x=10, y=70)

        directory = StringVar()
        Entry(
            root,
            textvariable=directory,
            background='white',
            font=('bitstream vera sans', 12),
            width=32
        ).place(x=125, y=70)

        def find_directory():
            file_location = filedialog.askdirectory(initialdir='/home', title='Select directory')
            directory.set(file_location)

        Button(
            root,
            text='...',
            font=('bitstream vera sans', 12),
            command=find_directory
        ).place(x=455, y=65)

        ttk.Separator(root).place(y=125, relwidth=1)

        Label(
            root,
            text='With Accept Ratio',
            font=('bitstream vera sans', 12, 'bold')
        ).place(x=10, y=150)

        Label(
            root,
            text='Ratio:               px',
            font=('bitstream vera sans', 12)
        ).place(x=100, y=225)

        ratio = StringVar()
        Entry(
            root,
            textvariable=ratio,
            background='white',
            font=('bitstream vera sans', 12),
            width=5
        ).place(x=160, y=225)

        def convert_ratio():
            ImageResize.image_resize_ratio(
                directory.get(),
                float(ratio.get())
            )

        Button(
            root,
            text='Convert',
            font=('bitstream vera sans', 12),
            command=convert_ratio
        ).place(x=300, y=220)

        ttk.Separator(root).place(y=300, relwidth=1)

        Label(
            root,
            text='Without Accept Ratio',
            font=('bitstream vera sans', 12, 'bold')
        ).place(x=10, y=325)

        Label(
            root,
            text='Width:               px      | Height:               px',
            font=('bitstream vera sans', 12)
        ).place(x=25, y=400)

        width = StringVar()
        Entry(
            root,
            textvariable=width,
            background='white',
            font=('bitstream vera sans', 12),
            width=5
        ).place(x=90, y=400)

        height = StringVar()
        Entry(
            root,
            textvariable=height,
            background='white',
            font=('bitstream vera sans', 12),
            width=5
        ).place(x=280, y=400)

        def convert_pixel():
            ImageResize.image_resize_pixel(
                directory.get(),
                int(width.get()),
                int(height.get()),
            )

        Button(
            root,
            text='Convert',
            font=('bitstream vera sans', 12),
            command=convert_pixel
        ).place(x=390, y=395)

        ttk.Separator(root).place(y=500, relwidth=1)
        root.mainloop()


if __name__ == '__main__':
    GUI()
