class Stack:
    def __init__(self) -> None:
        self.stack = []
        
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    def push(self, value) -> None:
        self.stack.append(value)
        
    def pop(self) -> int:
        # si mi stack está vacío
        if len(self.stack) < 1:
            return None
        return self.stack.pop()
    
    def size(self) -> int:
        return len(self.stack)
    
        
if __name__ == "__main__":
    stack: Stack = Stack()
    
    # insertar elementos
    

    