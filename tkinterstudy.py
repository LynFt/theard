import tkinter
import time
import tkinter.messagebox
#主窗口创建 ，大小，标题
top=tkinter.Tk()
top.minsize(600,480)
top.maxsize(600,480)
top.title("Tkinter study")
# tkinter._test()
#次级窗口创建
# msgwindow=tkinter.messagebox

#便签 按钮的创建
# label1=tkinter.Label(top,text=time.ctime())
# label1.pack(fill=tkinter.X,expand=1)

# def msgshow():
#       tkinter.messagebox.showinfo("hello","python")

bt1=tkinter.Button(top,text="quit",command=top.destroy,bd=3)
bt1.pack()




tkinter.mainloop()