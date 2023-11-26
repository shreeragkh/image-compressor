from PIL import Image
import os
def compress_image(input_path, output_path, quality=85):
    try:
        img = Image.open("C:\\Users\\shree\\Desktop\\Shreerag\\Images\\forest.jpeg")
        img.save("C:\\Users\\shree\\Desktop\\Shreerag\\Images\\compressed image.jpeg", quality=quality)
        print(f"Image compressed successfully and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")


