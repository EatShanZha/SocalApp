import queue
import threading,time

class Match(object):
    def __init__(self):
        self.q = queue.Queue()
    def add(self,account):
        while True:

            evt =threading.Event()
            self.q.put((account,evt))
            evt.wait(6)

    def MatchChat(self,account):
        while True:
            time.sleep(0.2)
            data,evt = self.q.get()
            if not data:
                pass
            if data == account:
                evt.set()
            else:
                 self.q.task_done()
                 break
        return data

    def match(self,account):
        thread_one = threading.Thread(target=self.add, args=(account))
        thread_two = threading.Thread(target=self.MatchChat, args=(account))
        thread_one.start()
        thread_two.start()
        thread_one.join()
        thread_two.join()
