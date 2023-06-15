#By JCNW aka manke nelis
import tkinter as tk
from tkinter.filedialog import askdirectory
from PIL import Image
import os
import numpy as np 

def set_everything_not_black_to_full_white(image):
    """Sets all pixels in an image that are not black to full white.

    Args:
        image (Image): The image to modify.

    Returns:
        The modified image.
    """
    image = np.array(image)
    image[image != 0] = 255
    return Image.fromarray(image)

def convert_npy_to_png(npy_file):
    """Converts a numpy image file to a grayscale png file.

    Args:
        npy_file (str): The path to the numpy image file.

    Returns:
        None.
    """
    image = Image.fromarray(np.array(np.load(npy_file)).astype(np.uint8)).convert("L")
    image = set_everything_not_black_to_full_white(image)
    image.save(npy_file.replace(".npy", ".png"))

def main():
    """The main function."""
    # Create the GUI window.
    root = tk.Tk()

    # Create a label for the folder selection.
    folder_label = tk.Label(root, text="Select a folder containing npy image files:")
    folder_label.pack()

    # Create a text entry box for the folder selection.
    folder_entry = tk.Entry(root)
    folder_entry.pack()

    # Create a button to select the folder.
    select_folder_button = tk.Button(root, text="Select Folder", command=lambda: select_folder(folder_entry))
    select_folder_button.pack()

    # Create a button to convert the npy files to png files.
    convert_npy_files_button = tk.Button(root, text="Convert NPY Files to PNG Files", command=lambda: convert_npy_files(folder_entry.get()))
    convert_npy_files_button.pack()

    # Start the GUI event loop.
    root.mainloop()

def select_folder(folder_entry):
    """Selects a folder and updates the folder entry.

    Args:
        folder_entry (tk.Entry): The text entry box for the folder selection.

    Returns:
        None.
    """
    # Get the selected folder.
    folder = askdirectory()

    # Update the folder entry.
    folder_entry.delete(0, "end")
    folder_entry.insert(0, folder)

def convert_npy_files(folder):
    """Converts all npy files in the specified folder to grayscale png files.

    Args:
        folder (str): The path to the folder containing the npy files.

    Returns:
        None.
    """
    # Get all the npy files in the folder.
    npy_files = [f for f in os.listdir(folder) if f.endswith(".npy")]

    # Convert each npy file to a png file.
    for npy_file in npy_files:
        convert_npy_to_png(os.path.join(folder, npy_file))

if __name__ == "__main__":
    main()
