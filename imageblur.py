import os

def generate_output_path(base_path):
    if os.path.exists(base_path):
        if os.path.getsize(base_path) == 0:
            return base_path
        else:
            filename, extension = os.path.splitext(base_path)
            counter = 1
            while True:
                new_path = f"{filename}_{counter}{extension}"
                if not os.path.exists(new_path):
                    return new_path
                counter += 1
    else:
        return base_path

from rembg import remove
from PIL import Image

input_path = 'food1.jpg'
output_path = generate_output_path('output.png')

input_image = Image.open(input_path)
output_image = remove(input_image)
output_image.save(output_path)
