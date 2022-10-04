from collections import deque
from time import sleep
import threading
import queue
import concurrent.futures


# q = deque()
#
# q.appendleft(5)
# q.appendleft(9)
# q.appendleft(40)
#
# print(q)


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    # def __iter__(self):
    #     return QueueIterator(self)


class QueueIterator:
    def __init__(self, queue):
        self._queue = queue
        self._index = 0

    def __next__(self):
        if self._index < (len(self._queue.buffer)):
            if self._index < len(self._queue.buffer):
                result = (self._queue.buffer[self._index])
            else:
                result = (self._queue.buffer[self._index - len(self._queue.buffer)])

            self._index += 1
            return result
        raise StopIteration


# ex. 1


# def place_orders(orders):
#     for order in orders:
#         print("Placing order for:",order)
#         food_order_queue.enqueue(order)
#         sleep(0.5)
#
#
# def serve_orders():
#     sleep(1)
#     while True:
#         order = food_order_queue.dequeue()
#         print("Now serving: ",order)
#         sleep(2)
#
#
# if __name__ == '__main__':
#     food_order_queue = Queue()
#     orders = ['pizza','samosa','pasta','biryani','burger']
#     t1 = threading.Thread(target=place_orders, args=(orders,))
#     t2 = threading.Thread(target=serve_orders)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()


def order(q, orders):
    for dish in orders:
        q.put(dish)
        sleep(.5)
        print(f'New order: {dish}')


def serve(q):
    while q.qsize() != 0:
        dish = q.get()
        sleep(2)  # preparing time
        print(f'{dish} ready!')


orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

q = queue.Queue()

t1 = threading.Thread(target=order, args=(q, orders))
t2 = threading.Thread(target=serve, args=(q,))

t1.start()
t2.start()

t1.join()
t2.join()



# with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#     f1 = executor.map(order, orders)
    # f2 = executor.submit(serve)
    # print(f1, f2)

    # for qq in f1:
        # for q in qq:
            # print(q)
        # f2 = executor.submit(serve, q)
