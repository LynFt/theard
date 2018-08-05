import multiprocessing
from time import ctime, sleep


def consumer(input_q):
      print("Info consumer: ", ctime())
      while True:
            item = input_q.get()
            print("c ", item, " out of q")
            input_q.task_done()
            sleep(0.5)
      print("Out of consumer: ", ctime())


def producer(sequenec, output_q):
      print("Info producer: ", ctime())
      for item in sequenec:
            output_q.put(item)
            print("p ", item, " into_q")
            sleep(0.3)
      print("Out of producer: ", ctime())


if __name__ == '__main__':
      q = multiprocessing.JoinableQueue()
      cons_p = multiprocessing.Process(target=consumer, args=(q,))
      cons_p.daemon = True
      cons_p.start()

      sequece = [1, 2, 3, 4.5, 6, 7, 8, 9, 0, 123, 312, 3, 3, 3, 1, 12, 3, 3, 4, 1, 51, 51, 1, 5, 1, 5]
      producer(sequece, q)
      q.join()
