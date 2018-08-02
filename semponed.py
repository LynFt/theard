import threading
import time
import random

sum1=1

def func():
      global sum1
      sum1+=1
      print(sum1)

      sum1-=1
      print(sum1)
      time.sleep(0.1)

def main():
      t0=[]
      for i in range(10000):
            t=threading.Thread(target=func)
            t0.append(t)

      for i in range(10000):
            t0[i].start()
            print("process ",i, "start ")

if __name__ == '__main__':
      main()