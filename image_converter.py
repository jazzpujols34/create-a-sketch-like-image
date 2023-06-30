import cv2
image = cv2.imread("<IMAGE_NAME>")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_image.jpg", gray_image)
inverted_image = 255 - gray_image
cv2.imwrite("inv.png", inverted_image)
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
cv2.imwrite("blur.png", blurred)
inverted_blurred = 255 - blurred
cv2.imwrite("invblur.png", inverted_blurred)
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
cv2.imwrite("Sketch.png", pencil_sketch)

