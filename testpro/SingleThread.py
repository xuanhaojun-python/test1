from time import ctime, sleep


def music(func):
    for i in range(2):
        print("I was listening to %s. %s" % (func, ctime()))
        sleep(1)


def move(func):
    for i in range(2):
       print("i am at the movies %s. %s" % (func,ctime()))
       sleep(5)


if __name__ == '__main__':
    music('爱情买卖')
    move('阿凡达')
    print("all over %s" % ctime())


