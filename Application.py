import tkinter as tk
from tkinter import filedialog

def button1_click():
    import Camera
    def submit_url():
        url = entry.get()
        url1=entry1.get()
        if entry.get() == "" and entry1.get() == "":
            message_window = tk.Tk()
            message_window.title("Error")
            message_window.geometry("200x50")
            message_label = tk.Label(message_window, text="\nPlease fill in the URL")
            message_label.pack()
            message_window.mainloop()
        else:
            if url1!="0" and url!="0":
                Camera.camera("https://"+url+":8080/video","https://"+url1+":8080/video")
            elif url=='0' and url1!='0':
                Camera.camera("https://"+url1+":8080/video",0)
            elif url1=="0" and url!="0":
                Camera.camera("https://"+url+":8080/video",0)
            else:                
                message_window = tk.Tk()
                message_window.title("Error")
                message_window.geometry("250x50")
                message_label = tk.Label(message_window, text="\nBoth the sources cannot be webcam")
                message_label.pack()
                message_window.mainloop()
    window = tk.Tk()
    window.title("Enter URL")
    window.geometry("300x200")
    

    # Create a label and entry field for the URL
    label = tk.Label(window, text="Enter URL given in the App:\nURL 1:")
    label.pack()

    entry = tk.Entry(window)
    entry.pack()
    label1 = tk.Label(window, text="URL 2:")
    label1.pack()

    entry1 = tk.Entry(window)
    entry1.pack()
    
    button = tk.Button(window, text="Submit", command=submit_url)
    button.pack()

    # Keep the window open until the user closes it
    window.mainloop()  


def button2_click():
    from LinearRegression import Line
    window = tk.Tk()
    window.title("Input Fields")
    window.geometry("300x200")

    # Create input fields
    label1 = tk.Label(window, text="Enter Pixel Length:")
    label1.pack()
    entry1 = tk.Entry(window)
    entry1.pack()

    label2 = tk.Label(window, text="Enter Pixel Width:")
    label2.pack()
    entry2 = tk.Entry(window)
    entry2.pack()

    label3 = tk.Label(window, text="Enter Pixel Height:")
    label3.pack()
    entry3 = tk.Entry(window)
    entry3.pack()

    def submit_values():
        import numpy as np
        value1 = float(entry1.get())
        value2 = float(entry2.get())
        value3 = float(entry3.get())
        x,y=Line()
        value4 = np.multiply(x[0], value1) + np.multiply(x[1], value2) + y

        window = tk.Tk()
        window.title("Output")
        window.geometry("300x200")
        label1 = tk.Label(root, text="The Answer is " + str(value4))
        label1.pack()  

    button2 = tk.Button(window, text="Submit", command=submit_values)
    button2.pack()    

        

    window.mainloop()





def button3_click():
    import Object
    root = tk.Tk()
    root.withdraw()

    # Open a file dialog to select the pictures
    pictures = filedialog.askopenfilenames(title="Select Pictures",filetypes=[("JPEG files", "*.jpg"), ("All Files", "*.*")])
    for picture in pictures:
        Object.Object(picture)
    root.destroy()

root = tk.Tk()
root.title("DOP Project")
root.geometry("500x150")

label = tk.Label(root, text="Welcome to Smart Packaging Solutions.\nThis will allow you to detect the aprroximate length, breadth and height of the Object.\n\n")
label.pack()
button1 = tk.Button(root, text="Camera", command=button1_click)
button1.pack()

button2 = tk.Button(root, text="Object Detection", command=button3_click)
button2.pack()

button3 = tk.Button(root, text="Linear Regression", command=button2_click)
button3.pack()

root.mainloop()
