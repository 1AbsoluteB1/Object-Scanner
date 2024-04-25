import cv2

# Load the image
image = cv2.imread('Photo_H.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Converting to Greyscale

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply adaptive thresholding to segment shadows
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 10)
cv2.imshow('thresh',thresh)

# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

max_height = 0
max_area = 0
max_width = 0
max_x = 0
max_y = 0

# Iterate through contours
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    area = w * h
    
    # Filter out contours with small area
    if area < 1:
        continue
    
    # Update maximum width, height, and area
    if area > max_area:
        max_width = w
        max_height = h
        max_area = area
        max_x = x
        max_y = y

# Draw the bounding rectangle excluding shadows
cv2.rectangle(image, (max_x, max_y), (max_x + max_width, max_y + max_height), (0, 255, 0), 2)

# Put text for width and height
cv2.putText(image, f'Width: {max_width}, Height: {max_height}', (max_x, max_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
