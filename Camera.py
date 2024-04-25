import cv2
import numpy as np
import tkinter as tk
def adjust_brightness(image, value):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    v = np.clip(v, 0, 255)
    final_hsv = cv2.merge((h, s, v))
    image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return image

def adjust_contrast(image, value):
    alpha = (value + 100.0) / 100.0
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=0)
    return adjusted_image

def adjust_saturation(image, value):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s = cv2.add(s, value)
    s = np.clip(s, 0, 255)
    final_hsv = cv2.merge((h, s, v))
    image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return image


def camera(url, url1):
    try:
        cap = cv2.VideoCapture(url)
        cap2 = cv2.VideoCapture(url1)

        # Create a window to display the video feed and sliders
        window = tk.Tk()
        window.title("Camera Feed")
        
        brightness_var = tk.DoubleVar()
        contrast_var = tk.DoubleVar()
        saturation_var = tk.DoubleVar()

        # Function to update the parameters based on slider values
        def update_params():
            brightness = brightness_slider.get()
            contrast = contrast_slider.get()
            saturation = saturation_slider.get()

            # Update the video feed for frame
            ret, frame = cap.read()
            frame = cv2.resize(frame, (960, 544))

            # Adjust brightness, contrast, and saturation for frame
            frame = adjust_brightness(frame, brightness)
            frame = adjust_contrast(frame, contrast)
            frame = adjust_saturation(frame, saturation)

            if frame is not None:
                cv2.imshow('frame', frame)

            # Update the video feed for frame1
            ret, frame1 = cap2.read()
            frame1 = cv2.resize(frame1, (960, 544))

            # Adjust brightness, contrast, and saturation for frame1
            frame1 = adjust_brightness(frame1, brightness)
            frame1 = adjust_contrast(frame1, contrast)
            frame1 = adjust_saturation(frame1, saturation)

            if frame1 is not None:
                cv2.imshow('frame1', frame1)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('c'):
                cv2.imwrite('Photo_H.jpg', frame)
                cv2.imwrite('Photo_V.jpg', frame1)
                print('Photo captured successfully!')
            if key == ord('q'):
                window.destroy()

            window.after(10, update_params)  # Update the parameters every 10 milliseconds
            window.protocol("WM_DELETE_WINDOW", window.destroy)  # Properly release resources upon closing the window

        # Slider for adjusting brightness
        brightness_slider = tk.Scale(window, from_= -100, to=100, orient='horizontal', label='Brightness', variable=brightness_var)
        brightness_slider.pack()

        # Slider for adjusting contrast
        contrast_slider = tk.Scale(window, from_= -100, to=100, orient='horizontal', label='Contrast', variable=contrast_var)
        contrast_slider.pack()

        # Slider for adjusting saturation
        saturation_slider = tk.Scale(window, from_= -100, to=100, orient='horizontal', label='Saturation', variable=saturation_var)
        saturation_slider.pack()

        # Call the function to update the video feed and sliders
        update_params()

        window.mainloop()
        window.protocol("WM_DELETE_WINDOW", window.destroy)  # Properly release resources upon closing the window


    except:
        window = tk.Tk()
        window.title("Connection Error")
        window.geometry("300x200")
        label = tk.Label(window, text="URL Cannot be connected to System.\nPlease Make Sure both the devices are on the same network\nalong with the correct URL given.")
        label.pack()
