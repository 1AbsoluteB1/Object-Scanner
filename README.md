# Object-Scanner
This Program is in "Beta Stage" as more optimizations are required. However it can be used easily with two phones attached and (hopefully) without any latency
# Introduction
This Program aims to resolve the preliminary issue of able to design packges via knowing the dimenstions of the object. This is done using 2 camera system to define 3D Space. Inside this repository you'll find: 5 Python Projects, 1 Excel Sheet, all of which play a role in defining the Length, Breadth and width of an object. This aims to help small business shippers to package stuff properly without any use of heavy machinery and thereby streamling the packaging process. We shall be going through each of them.
# Camera
The provided Python code utilizes OpenCV for image processing and camera feed manipulation, along with Tkinter for creating a graphical user interface to control image parameters. Here is a breakdown of the key functionalities:

## Functions for Image Adjustment
1. `adjust_brightness(image, value)`: Adjusts the brightness of the image using the HSV color space.
2. `adjust_contrast(image, value)`: Modifies the image contrast by scaling the pixel values.
3. `adjust_saturation(image, value)`: Alters the image saturation within the HSV color space.

## Camera Function
The `camera(url, url1)` function initializes two video captures from the provided URLs, then creates a Tkinter window with sliders to manipulate brightness, contrast, and saturation. Key points include:
- Sliders for each parameter linked to their respective adjustment functions.
- Method to continuously update the video feed frames based on the slider values.
- Ability to adjust parameters for two separate video feeds simultaneously.

## Exception Handling
- The code includes exception handling in case there is a connection error with the provided URLs. It displays a message prompting the user to check the network connection and URLs.

This Python script provides an interactive interface to tweak image properties in real-time using OpenCV and Tkinter, enabling users to control the visual output of camera feeds effectively.
# Object Detection and Measurement Using OpenCV in Python

The provided Python code utilizes OpenCV to perform object detection and measurement on an input image. Here is a breakdown of the key functionalities:

## Image Processing and Object Detection
1. `Object(image_name)`: This function reads the input image and performs the following operations:
  - Conversion to grayscale using `cv2.cvtColor()`.
  - Application of Gaussian blur to reduce white noise.
  - Edge detection using the Canny edge detector.
  - Displaying the Canny edge-detected image using `cv2.imshow()`.

2. Contour Detection and Measurement:
  - Utilizes `cv2.findContours()` to detect contours in the Canny edge-detected image.
  - Iterates through the contours to find the smallest and largest coordinates to define a bounding rectangle around the detected object.
  - Draws a rectangle around the object and labels it with its width and height using `cv2.rectangle()` and `cv2.putText()` respectively.
  - Displays the processed image using `cv2.imshow()` and waits for user input with `cv2.waitKey()`.
  - Closes all windows using `cv2.destroyAllWindows()` when the user presses the 'q' key.
# Linear Regression

The provided Python code demonstrates the implementation of a simple linear regression model using the Scikit-Learn library to predict the dependent variable based on given independent variables. Below is a breakdown of the key functionalities:

## Data Import and Preprocessing
- The code first imports necessary libraries, including NumPy, Pandas, and the modules for linear regression modeling from Scikit-Learn.
- It defines the `Line()` function, which encompasses the steps for building and analyzing the linear regression model.

## Linear Regression Model Building
- **Data Loading**: Reads the dataset from an Excel file using Pandas' `read_excel()` function.
- **Defining Variables**: Specifies the independent variables (`X`) and the dependent variable (`Y`) from the dataset.
- **Model Initialization**: Creates an instance of the linear regression model using `LinearRegression()`.
- **Model Training**: Fits the linear regression model with the provided independent and dependent variables using the `fit()` method.
- **Coefficient and Intercept Extraction**: Retrieves the coefficients and intercept of the trained linear regression model.
- **Return Values**: The function returns the coefficients and intercept.


