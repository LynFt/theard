import tkinter

# def ptintmsg1():
#       print("button1")
login = tkinter.Tk()
login.title("login in")


# login.minsize(400,380)

def printmsg2():
      name = e1.get()
      pw = e2.get()
      if name == "123" and pw == "123":
            login_stauts_label['text'] = "Pass"
            login.destroy()

            mainbase = tkinter.Tk()
            mainbase.title("Hello")
            base(mainbase)
            mainbase.mainloop()
      else:
            login_stauts_label['text'] = "Error"


# def label_click(event):
#       global login
#       lb=tkinter.Label(login,text="Please Login in")
#       lb.pack()

but1 = tkinter.Button(login, text="button1", command=printmsg2)
but1.grid(row=3, column=1, stick=tkinter.E)

# but2=tkinter.Button(login,text="button2",command=printmsg2)
# but2.pack()

# lb=tkinter.Label(login,text="button3")
# lb.bind("<Button-1>",label_click)
# lb.pack()
# 登陆的输入框   位置设置 密码显示"*"
e1 = tkinter.Entry(login, text="username")
e2 = tkinter.Entry(login, text="password")
e1.grid(row=1, column=1, stick=tkinter.E)
e2.grid(row=2, column=1, stick=tkinter.E)
e2['show'] = '*'
# 登陆状态消息
login_stauts_label = tkinter.Label(login, text="")
login_stauts_label.grid(row=3, column=1, stick=tkinter.W)
# 登陆输入框提示
user_name_label = tkinter.Label(login, text="name")
user_pw_label = tkinter.Label(login, text="pw")
user_name_label.grid(row=1, column=0)
user_pw_label.grid(row=2, column=0)


def base(mainbase):
      meunbar = tkinter.Menu(mainbase)
      emenu = tkinter.Menu(meunbar)
      for item in ['file', 'edit', 'view', 'about']:
            emenu.add_command(label=item)

      meunbar.add_cascade(label='o', menu=emenu)
      meunbar.add_cascade(label='p', menu=emenu)
      mainbase['menu'] = meunbar


login.mainloop()
