class Stack:
    def __init__(self):
        self._contents = []
        
    def __len__(self):
        return len(self._contents)
    
    def __repr__(self):
        return self._contents.__repr__()
    
    def is_empty(self):
        return len(self._contents) == 0
    
    def push(self, val):
        self._contents.append(val)
        
    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty; cannot pop empty stack!')
        return self._contents.pop()
