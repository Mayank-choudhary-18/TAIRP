import cv2
import numpy as np

# Step 1: Install necessary libraries like OpenCV and NumPy.

# Step 2: Capture an image using a webcam or load an existing image.
image = cv2.imread('input.jpg')

# Step 3: Apply image processing to enhance document visibility.
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150)

# Step 4: Detect document edges using techniques like Canny edge detection.
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

    if len(approx) == 4:
        doc_contour = approx
        break

# Step 5: Save the scanned document as an image or PDF file.
cv2.drawContours(image, [doc_contour], -1, (0, 255, 0), 3)
cv2.imshow("Scanned Document", image)
cv2.waitKey(0)
cv2.destroyAllWindows()