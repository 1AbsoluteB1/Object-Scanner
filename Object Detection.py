#Library Import
import cv2
import numpy as np
#Reading File
def Object(image_name):
    image = cv2.imread(image_name)
    #Filter Application
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #Greyscale Conversion
    blurred = cv2.GaussianBlur(gray, (5, 5), 0) #White Noise Reduction
    edges = cv2.Canny(blurred, 75, 225) #Edge Detection using Canny
    cv2.imshow("image",edges) #Displays Canny Image
    #Edge Detection
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    # Initialize variables to keep track of the smallest and largest coordinates
    min_x = np.inf
    max_x = 0
    min_y = np.inf
    max_y = 0

    # Iterate through contours
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        # Update smallest and largest coordinates
        min_x = min(min_x, x)
        max_x = max(max_x, x+w)
        min_y = min(min_y, y)
        max_y = max(max_y, y+h)

    # Draw rectangle along smallest and largest coordinates
    cv2.rectangle(image, (min_x, min_y), (max_x, max_y), (0, 255, 0), 2)
    cv2.putText(image, f'Width: {max_x-min_x}, Height: {max_y-min_y}', (min_x, min_y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    print(w,h)
    #Display
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    if ord("q"):
        cv2.destroyAllWindows()
    return w,h,min_y
