print('this is the master branch')

import tkinter as tk
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
        return self._x * self._y * 2
    def __str__(self):
        return str((self._x, 2*self._y))

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

class Triangle(Shape):
    def __init__(self,x,y,z):
        super().__init__()
        self.__z = z


class SecondScreen(tk.Toplevel):
    def __init__(self,parent,name):
        self._shape = name
        self._closure = False
        super().__init__()
        self.geometry("500x500")
        self.resizable(False,False)
        self.title(self._shape)
        self._close_button = tk.Button(self,text='close',command=self.closure)
        self._close_button.pack(side=tk.TOP,padx=10,pady=10,fill=tk.Y)
        self.grab_set()
        

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
