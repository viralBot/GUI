from my_package.model import ImageCaptioningModel
from my_package.model import ImageClassificationModel
import tkinter as tk
from tkinter import *
from functools import partial
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import ttk


def fileClick(clicked):
    # Define the function you want to call when the filebrowser button (Open) is clicked.
    # This function should pop-up a dialog for the user to select an input image file.
    # To have a better clarity, please check out the sample video.
    file = filedialog.askopenfilename(initialdir="./data/imgs")
    if file:#if file is selected
        im = ImageTk.PhotoImage(Image.open(file)) #opening image from filename

        #Adding image to the image label
        image_label.image = im
        image_label.config(image=image_label.image)

        #setting the value of clicked to filename
        clicked.set(file)

        #Creating text for the image name text box
        txt = "Image - " + file[len(file)-5]
        T.config(state = NORMAL)
        T.delete("1.0", "end")
        T.insert(INSERT, txt)
        T.config(state=DISABLED)#Disabling the editing of text widget after adding the text to prevent corruption of filename in widget by user


def process(clicked, captioner, classifier):
    # This function will produce the required output when 'Process' button is clicked.
    # Note: This should handle the case if the user clicks on the `Process` button without selecting any image file.
    file = clicked.get()#getting filename from previously set clicked variable
    if not file:#Case when no file has been selected
        print("Select a file first!")
        return
    
    #Required global variable declarations
    global choice
    global output

    #Getting the choice of user from menu
    choice = menu.get()
    if choice == " Captioning":#Case of captioning
        res = captioner(file, 3)#list of 3 captions generated using the model
        output.destroy()#Destroying previous output label to generate a fresh one
        output = Label(root, font=('Times New Roman',  '12'))
        output.grid(row=1, column=3, columnspan=4)

        #adding text to output from the captions list
        output.config(text = "Top-3 captions:" + "\n"+" 1) "+res[0] + "\n" + "2) "+res[1] + "\n" + "3) "+ res[2], padx=40, pady= 10, bg="#FDA769", fg="#00425A")
    else:#Case of classification
        res1 = classifier(file, 3)#list of 3 classes generated using the model
        output.destroy()
        output = Label(root, font=('Times New Roman',  '12'))
        output.grid(row=1, column=3, columnspan=4)

        #adding text to output from the classes list
        output.config(text="Top-3 classes:" + "\n"+"1) "+str(res1[0][1]) + "-" + str(round(res1[0][0]*100,5))+ "\n"+"2) "+str(res1[1][1]) + "-" + str(round(res1[1][0]*100,5))+ "\n"+"3) "+str(res1[2][1]) + "-" + str(round(res1[2][0]*100,5))+ "\n", padx=40, pady= 10, bg="#FDA769", fg="#00425A")
    


if __name__ == '__main__':
    # Instantiate the root window.
    root = Tk()

    # Provide a title to the root window.
    root.title("Software Lab | IIT KGP | Image Viewer")

    #Creating text widget to output the image name opened
    T = Text(root, height = 1, width = 60)
    T.grid(row = 0, column = 0)

    # Instantiate the captioner, classifier models.
    captioner = 1#ImageCaptioningModel()
    classifier = 2#ImageClassificationModel()

    # Declare the file browsing button.
    clicked = StringVar()
    button1 = Button(root, text = "Open", width=8, activebackground="yellow", command = partial(fileClick, clicked))
    button1.grid(row = 0, column = 4)
    image_label = Label(root)
    image_label.grid(row = 1, column = 0)

    # Declare the drop-down button.
    choice = tk.StringVar() 
    menu = ttk.Combobox(root, width = 13, textvariable = choice)
    menu['values'] = (' Captioning', ' Classification')
    menu.grid(row = 0, column = 5)
    menu.current(0)

    # Declare the process button.
    button2 = Button(root, text = "Process", width = 10, activebackground="yellow", command = partial(process, clicked, captioner, classifier))
    button2.grid(row = 0, column = 6)

    # Declare the output label.
    output = Label(root, font=('Times New Roman',  '12'))
    output.grid(row=1, column=3, columnspan=4)

    root.mainloop()