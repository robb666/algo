from collections import deque

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

    def enqueue(self, value):
        self.buffer.appendleft(value)

    def dequeue(self):
        self.buffer.pop()

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


# pq = Queue()
#
# pq.enqueue({
#     'company': 'Wall Mart',
#     'timestamp': '15 apr, 11.01 AM',
#     'price': 131.10
# })
# pq.enqueue({
#     'company': 'Wall Mart',
#     'timestamp': '15 apr, 11.02 AM',
#     'price': 132
# })
# pq.enqueue({
#     'company': 'Wall Mart',
#     'timestamp': '15 apr, 11.03 AM',
#     'price': 135
# })
#
# print(pq.buffer)


# ex. 1

from time import sleep
import concurrent.futures


def order(orders):
    # q = Queue()
    q = []
    for dish in orders:
        print(f'New order: {dish}')
        # q.enqueue(dish)
        q.append(dish)
        sleep(.5)
        yield q


def serve(q):
    while len(q) != 0:
        dish = q.pop(0)
        sleep(2)
        print(f'{dish} ready!')


orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

funk = [order, serve]


with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    f1 = executor.map(order, [orders])
    for item in f1:
        for item2 in item:
            f2 = executor.submit(serve, item2)
