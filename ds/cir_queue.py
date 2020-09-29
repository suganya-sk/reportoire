INITIAL_SIZE = 10
import pdb

class CirQueue:
    def __init__(self):
        self._front = 0
        self._contents = [None] * 10
        self._size = 0

    def __repr__(self):
        answer = []
        for i in range(self._size-1):
            answer.append(self._contents[(self._front + i) % self._size])
        return repr(answer)
    
    def __len__(self):
        return self._size

    def _resize(self):
        #pdb.set_trace()
        new_len = len(self._contents) * 2
        orig = self._contents
        self._contents = [None] * new_len
        for i in range(len(orig)):
            self._contents[i] = orig[(self._front + i) % len(orig)]
        self._front = 0

    def enqueue(self, val):
        if self._size == len(self._contents):
            self._resize()
        pos = (self._front + self._size) % len(self._contents)
        self._contents[pos] = val
        self._size += 1

    def dequeue(self):
        answer = self._contents[self._front]
        self._contents[self._front] = None
        self._front = (self._front + 1) % len(self._contents)
        self._size -= 1
        return answer
