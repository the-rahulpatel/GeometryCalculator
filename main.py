import tkinter as tk
print('branch is dev not master')
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


class LogoFrame(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self._logo_label = tk.Label(self,text="Geometry Calculator")
        self._logo_label.pack()

class UserMenuFrame(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self._intro_label = tk.Label(self,text='Get started')
        self._intro_label.pack()
class Geometry():
    def __init__(self,master):
        self._master = master
        self._master.title("Geometry Calculator")
        self._master.minsize(height=600,width=600)
        self._master.resizable(False,False)
        self._logo_frame = LogoFrame(self._master)
        self._logo_frame.place(x=250,y=50)
        self._usermenu_frame = UserMenuFrame(self._master)
        self._usermenu_frame.place(x=250,y=450)

        


if __name__ == '__main__':
    root = tk.Tk()
    app = Geometry(root)
    root.mainloop()
