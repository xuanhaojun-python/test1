import threading
from time import ctime, sleep


def music(func):
    for i in range(4):
        print("i was listening  to %s. %s" % (func, ctime()))
        sleep(1)


def move(func):
    for i in range(4):
        print("i was move at the %s. %s" % (func, ctime()))
        sleep(5)


threads = []
t1 = threading.Thread(target=music, args={'爱情卖卖'})
threads.append(t1)
t2 = threading.Thread(target=move, args={'阿凡达'})
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()

    print("all over %s" % ctime())
