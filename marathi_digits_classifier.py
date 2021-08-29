from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageGrab
from keras.models import load_model
import numpy as np
import cv2
app = Tk()
app.geometry("200x200")
  
  
  


def get_x_and_y(event):
    global lasx, lasy
    
    lasx, lasy = event.x, event.y

def draw_smth(event):
    global lasx, lasy
    canvas.create_line((lasx, lasy, event.x, event.y), fill='black', width=10)
    lasx, lasy = event.x, event.y
    


def canvas_image(canvas,fileName):
   
    # save postscipt image 
    canvas.postscript(file = fileName + '.eps') 
    # use PIL to convert to PNG 
    img = Image.open(fileName + '.eps')
    img.save(fileName + '.jpg', 'JPEG')
    img = Image.open(fileName + '.jpg')
    img = img.resize((28, 28))
    return img
    
def preprocess_image(canvasImage):
    image = np.array(canvasImage)

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    imagem = cv2.bitwise_not(gray)
    return imagem   
def get_model_prediction(preProcessedImage):
    classifier = load_model('models/marathi_digits_10_Epochs.h5')
    input_im =np.array([np.array(preProcessedImage)])
    input_im = input_im.reshape(1,28,28,1) 
    res = (classifier.predict(input_im, 1, verbose = 0)[0])
    prediction = np.argmax(res)
    
    return prediction

    
    
    
 
def clear_button_clicked():
    canvas.delete("all")
def predict_button_clicked():
    """
    This function calls the save image function
    :param name:
    :return:
    """
    
    canvasImage = canvas_image(canvas,"temp_img")
  
    canvas.delete("all")
    
    preProcessedImage = preprocess_image(canvasImage)
    
    output = get_model_prediction(preProcessedImage)
    canvas.create_text(100, 25, text= "मराठी  Digits Classifier",fill="#ff8000",font=('Helvetica 11 bold'))
    canvas.create_text(100, 60, text= "Model Prediction is",fill="#00bfff",font=('Helvetica 11 bold'))
    canvas.create_text(100, 130, text= output ,fill="#00ff40",font=('Helvetica 40 bold'))
    

    
    
    
global canvas




canvas = Canvas(app, bg='white')
canvas.pack(anchor='nw', fill='both', expand=1)


canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw_smth)

canvas.create_text(200,350,fill="white",text="Enter Range")



btn = Button(app, text='Clear', width=4,bg='lightgreen',height=1,command=clear_button_clicked)
  
btn.place(x=30, y=170)



btn = Button(app, text='Predict',bg='lightgreen', width=4,height=1, command=predict_button_clicked)
btn.place(x=150, y=170)



textBox=Text(app, height=2, width=10)
textBox.pack()

#image = Image.open("image.jpg")
#image = image.resize((400,400), Image.ANTIALIAS)
#image = ImageTk.PhotoImage(image)
#canvas.create_image(0,0, image=image, anchor='nw')
counter = 50
counter2 = 51

app.mainloop()
