print('this is the master branch')

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

allowed = True
class Shape:
    def __init__(self,x,y):
        self._x = x
        self._y = y
    def __str__(self):
        return str((self._x,self._y))
    
    def area(self):
        return self._x * self._y

class Rectangle(Shape): 
    def area(self):
        return self._x * self._y
    def __str__(self):
        return str((self._x, 2*self._y))
    def perimeter(self):
        return 2*(self._x + self._y)

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
    def perimeter(self):
        return 4*self._x
class Triangle(Shape):
    def __init__(self,x,y,z):
        self._x = x
        self._y = y
        self._z = z

    def area(self):
        return 0.5*self._x * self._y

    def perimeter(self):
        return self._x + self._y + self._z

class SecondScreen(tk.Toplevel):
    def __init__(self,parent,name):
        self._shape = name
        self._closure = False
        super().__init__()
        self.geometry("500x500")
        self.resizable(False,False)
        self.title(self._shape)
        self._close_button = tk.Button(self,text='close',command=self.closure)
        self._close_button.place(x=270,y=300)
        self.grab_set()
        self._shape_entry = tk.Entry(self)
        self._shape_entry.place(x=180,y=250)
        self._answer = None
        self._got = False
        if self._shape.lower() == 'square':
            self._square_label = tk.Label(self,text='length',font=("Arial", 25))
            self._square_label.place(x=200,y=180)
        elif self._shape.lower() == 'rectangle':
            for i in ['height,length']:
                tk.Label(self,text=i,font=("Arial", 25)).place(x=170,y=180)
        else:
            for i in ['height,base,side']:
                tk.Label(self,text=i,font=("Arial", 25)).place(x=140,y=180)
        self._calculate_button = tk.Button(self,text='calculate',command= lambda:self.get_details(self._shape_entry))
        self._calculate_button.place(x=200,y=300)
    

    def get_details(self,entryWidget):
        self._answer = entryWidget.get()
        _object = None 
        if len(self._answer) != 0:
            if self._shape == 'square':
                square = Square(int(self._answer))
                _object = square
            else:
                if self._shape == 'rectangle':
                    x,y = self._answer.split(',')
                    rectangle = Rectangle(int(x),int(y))
                    _object = rectangle
                else:
                    x,y,z = self._answer.split(',')
                    triangle = Triangle(int(x),int(y),int(z))
                    _object = triangle
            messagebox.showinfo("showinfo",f"Releavnt information: Area: {_object.area()}\nPerimeter: {_object.perimeter()}")
        else:
            messagebox.showwarning("Warning","Please enter input")

            
    def closure(self):
        self.destroy()
        
happening = False
class App():
    def __init__(self,root):
        global allowed
        self._master = root
        self._new_screen = False
        root.minsize(height=500,width=500)
        root.resizable(False,False)
        square = Image.open("square.png")
        photo = ImageTk.PhotoImage(square)

        square = tk.Label(root,bg='blue',image=photo,height=100,width=100)
        square.pack(ipadx=10,ipady=10,side=tk.TOP,pady=10)

        rectangle= tk.Label(root,bg='pink',image=photo,height=100,width=100)
        rectangle.pack(ipadx=10,ipady=10,side=tk.TOP,pady=10)

        triangle= tk.Label(root,bg='orange',image=photo,height=100,width=100)
        triangle.pack(ipadx=10,ipady=10,side=tk.TOP,pady=10)

        square.bind('<Button-1>', lambda banana:self.on_click('square'))
        rectangle.bind('<Button-1>', lambda banana:self.on_click('rectangle'))
        triangle.bind('<Button-1>', lambda banana:self.on_click('triangle'))

    def check_screen_exists(self):
        global allowed
        return True if allowed else False
    def on_click(self,shape,event=None):
        """
        the flaw in my logic is that the isntance of the secondscreen is created everytime the function ie sexcuted. 
        this is the issue and therefore I need to use a hwhie loop to actually control the flow of the operation. 
        """
        secondScreen = SecondScreen(self._master,shape)
        


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
