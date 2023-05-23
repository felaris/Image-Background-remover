import tkinter as tk
from tkinter import filedialog
import rembg
import numpy as np
import io
from PIL import Image

def remove_background(image_path):
    # Open the image file
    with open(image_path, "rb") as f:
        img_data = f.read()

    # Use rembg to remove the background
    output = rembg.remove(img_data)

    # Convert the output to a PIL image
    img = Image.open(io.BytesIO(output)).convert("RGBA")

    # Create a white background image with the same size as the input image
    background = Image.new("RGBA", img.size, (255, 255, 255))

    # Composite the input image with the white background
    final_image = Image.alpha_composite(background, img).convert("RGB")

    # Save the final image as output.jpg
    final_image.save("output.jpg")
    print("Background removed. Saved as output.jpg.")

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()

# Prompt the user to select a file
file_path = filedialog.askopenfilename()

# Check if a file was selected
if file_path:
    # Call the remove_background function with the selected file path
    remove_background(file_path)
else:
    print("No file selected.")
