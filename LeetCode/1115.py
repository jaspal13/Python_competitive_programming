from threading import Lock
import threading
class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooLock = Lock()
        self.barLock = Lock()
        self.barLock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.fooLock.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.barLock.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.barLock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.fooLock.release()

f=FooBar(5)
def printFoo():
    print ("foo")

def printBar():
    print ("bar")
thread1 = threading.Thread(target = f.bar, args = (printBar))

thread2 = threading.Thread(target = f.foo, args = (printFoo))
thread1.start()
thread2.start()