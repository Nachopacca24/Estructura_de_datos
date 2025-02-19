from memory_profiler import profile
import time

start = time.time()

class Stack:
    
    #@profile
    def __init__(self, size: int):
        self.max = size
        self.elements = [None] * size
        self.top = -1

    #@profile
    def __repr__(self):
        return f'Current stack: {self.elements} | Top: {self.top}'
    
    #@profile
    def push(self, val: str) -> None:
        if self.top == self.max - 1:
            print('Stack overflow')
            return None
        
        self.top += 1
        self.elements[self.top] = val

    #@profile
    def pop(self) -> any:
        if self.top == -1:
            print('Stack underflow')
            return None

        val = self.elements[self.top]
        self.elements[self.top] = None 
        self.top -= 1
        return val
    
    #@profile
    def peek(self) -> any:
        if self.top == -1:
            print('Stack underflow')
            return None

        return self.elements[self.top]
    
    #@profile
    def search(self, key) -> int:
    
        for i in range(self.top + 1):  # Desde el índice 0 hasta self.top
            _ = self.elements[i]  # Acceder manualmente a cada elemento sin comparaciones
        return -1

end = time.time()
print(end - start)