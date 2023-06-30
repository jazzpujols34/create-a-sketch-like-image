# Pencil Sketch Generator

This Python script uses OpenCV to convert an image into a pencil sketch-like image.

## Requirements

This script requires the following Python package:

- opencv-python

You can install it using pip:

```bash
pip install opencv-python
```

## Usage

Replace <IMAGE_NAME> in the script with the name of the image file you want to convert. The image file should be in the same directory as the script.

```
image = cv2.imread("<IMAGE_NAME>")
```

Run the script. The script will generate several images in the process of creating the pencil sketch:

- `gray_image.jpg`: This is the grayscale version of the original image.

- `inv.png`: This is the inverted version of the grayscale image.

- `blur.png`: This is the blurred version of the inverted image.

- `invblur.png`: This is the inverted version of the blurred image.

- `Sketch.png`: This is the final pencil sketch image.

Enjoy creating pencil sketches from your images!