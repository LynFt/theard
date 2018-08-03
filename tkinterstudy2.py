import tkinter
import time
base=tkinter.Tk()
base.wm_title("study2")
base.minsize(600,500)
base.maxsize(700,600)
def show_lab():
      global base
      lab=tkinter.Label(base,text=time.ctime())

      lab.pack()

exit_bt=tkinter.Button(base,text="exit",command=show_lab)
exit_bt.pack()
time_l=tkinter.Label(base,text=time.ctime())
time_l.pack()

if __name__ == '__main__':
      base.mainloop()


