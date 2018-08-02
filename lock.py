import threading
from time import  sleep

sum1=0
loopSum=10000
lock=threading.Lock()

def maAdd():
    global sum1,loopSum
    for i in range(1,loopSum):
        lock.acquire()
        sum1+=1
        lock.release()

def my_main():
    global  sum1,loopSum
    for i in range(1,loopSum):
        lock.acquire()
        sum1-=1
        lock.release()


if __name__ == '__main__':
    print("Start__{0}".format(sum1))
    t1=threading.Thread(target=maAdd,args=())
    t2=threading.Thread(target=my_main,args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done.....{0}".format(sum1))