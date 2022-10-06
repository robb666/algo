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

    # def front(self):
    #     return self.buffer[0]

    def front(self):
        return self.buffer[-1]

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


# def order(q, orders):
#     for dish in orders:
#         q.put(dish)
#         sleep(.5)
#         print(f'New order: {dish}')
#
#
# def serve(q):
#     while q.qsize() != 0:
#         dish = q.get()
#         sleep(2)  # preparing time
#         print(f'{dish} ready!')
#
#
# orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
#
# q = queue.Queue()
#
# t1 = threading.Thread(target=order, args=(q, orders))
# t2 = threading.Thread(target=serve, args=(q,))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()



# with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#     f1 = executor.map(order, orders)
    # f2 = executor.submit(serve)
    # print(f1, f2)

    # for qq in f1:
        # for q in qq:
            # print(q)
        # f2 = executor.submit(serve, q)



# ex. 2


# ex. 2


# Ver. 4 theirs
def produce_binary_numbers(n):
    pass


produce_binary_numbers(10)


# # Ver. 3
# def sequence():
#     q, q2 = Queue(), Queue()
#
#     zero, one = '0', '1'
#
#     q.enqueue(one), q2.enqueue(one)
#
#     for _ in range(10):
#         i = q.dequeue()
#         q.enqueue(i + zero), q2.enqueue(i + zero)
#
#         j = str(int(i + zero) + 1)
#         q.enqueue(j), q2.enqueue(j)
#
#         bin_num = q2.dequeue()
#         print(bin_num)
#
#
# q = Queue()
# sequence()


# # Ver. 2
# def sequence(q):
#     zero, one = '0', '1'
#
#     q.enqueue(one)
#     q.enqueue(one + zero)
#     q.enqueue(one + one)
#     q.enqueue(one + zero + zero)
#     q.enqueue(one + zero + one)
#     q.enqueue(one + one + zero)
#     q.enqueue(one + one + one)
#     q.enqueue(one + zero + zero + zero)
#     q.enqueue(one + zero + zero + one)
#     q.enqueue(one + zero + one + zero)
#
#     for _ in range(10):
#         print(q.dequeue())
#
#
# q = Queue()
# sequence(q)



# # Ver. 1
# def sequence():
#     zero, one = '0', '1'
#
#     q = [one]
#
#     for i in q:
#         i += zero
#         q.append(i)
#         j = q[-1]
#         j = str(int(j) + 1)
#         q.append(j)
#
#         if len(q) > 9:
#             for j in q:
#                 print(j)
#             break
#
#
# sequence()

















