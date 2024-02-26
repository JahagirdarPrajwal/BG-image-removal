# BG-image-removal
This Python script is designed to blur the background of an image using the `rembg` library and save the resulting image. If the output filename already exists, the script automatically generates a unique filename by appending a numerical suffix.

## Functionality

The script performs the following steps:
1. Opens an input image file.
2. Blurs the background of the image.
3. Saves the resulting image with a unique filename in the "outputs" folder.

## Libraries Used

### rembg
- **Description:** A Python library for removing image backgrounds using the `onnxruntime` framework.
- **Features:** 
  - Provides a simple interface for removing backgrounds from images.
  - Uses ONNX models for efficient background removal.
- **Installation:** `pip install rembg`

### Pillow (PIL)
- **Description:** Python Imaging Library (PIL) fork, now maintained as Pillow.
- **Features:** 
  - Powerful image processing capabilities, including opening, manipulating, and saving various image file formats.
  - Compatible with Python 3.x.
- **Installation:** `pip install Pillow`

## How to Run

Follow these steps to run the Python script:

1. **Clone the Repository:** 
   ```bash
   git clone https://github.com/JahagirdarPrajwal/BG-image-removal.git

2. **Install Required Libraries:**
   
   pip install rembg 
   pip install rembg[cil]
   pip install Pillow

3. **Place Input Image:**
   
   Place the input image file in the repository directory. 

4. **Run the script:**
   
   run the script by typing python imageblur.py 

5. **View output:**

   The resulting blurred image will be saved in the "outputs" folder within the repository directory.       
   