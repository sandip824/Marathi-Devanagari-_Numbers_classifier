from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageGrab

app = Tk()
app.geometry("400x400")
  

def get_x_and_y(event):
    global lasx, lasy
    
    lasx, lasy = event.x, event.y

def draw_smth(event):
    global lasx, lasy
    canvas.create_line((lasx, lasy, event.x, event.y), fill='red', width=10)
    lasx, lasy = event.x, event.y
    


def save_as_png(canvas,fileName):
    global counter
    global counter2
    fileName = str(counter2)
    if counter == 0:
        print('saved enough samples')
        app.destroy()
        return
     
    # save postscipt image 
    canvas.postscript(file = fileName + '.eps') 
    # use PIL to convert to PNG 
    img = Image.open(fileName + '.eps')
    img.save('images/'+fileName + '.jpg', 'JPEG')
    
    counter2 = counter2 + 1
    
    counter = counter -1
    
    
 

    
def button_clicked():
    
    print("button is clicked")
    
    
    
    save_as_png(canvas,"img")
    
    canvas.delete("all")
    print("exit counter",counter)
    print("filename",counter2)
    
    
    
global canvas




canvas = Canvas(app, bg='black')
canvas.pack(anchor='nw', fill='both', expand=1)


canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw_smth)

canvas.create_text(200,350,fill="white",text="Enter Range")

btn = Button(app, text='Capture', width=10,
             height=2, bd='10', command=button_clicked)
  
btn.place(x=310, y=350)

textBox=Text(app, height=2, width=10)
textBox.pack()

#image = Image.open("image.jpg")
#image = image.resize((400,400), Image.ANTIALIAS)
#image = ImageTk.PhotoImage(image)
#canvas.create_image(0,0, image=image, anchor='nw')
counter = 3
counter2 = 0

app.mainloop()
