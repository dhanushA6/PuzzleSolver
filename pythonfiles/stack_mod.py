class Stack:
    def __init__(self):
        """
        Initialize an empty stack.

        Attributes:
            items (list): List to store the elements of the stack.
        """
        self.items = []

    def push(self, item):
        """
        Push an element onto the stack.

        Args:
            item: The element to be pushed onto the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Pop the top element from the stack.

        Returns:
            The popped element if the stack is not empty, otherwise "Underflow".
        """
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Underflow"

    def peek(self):
        """
        Peek the top element of the stack.

        Returns:
            The top element of the stack if the stack is not empty, otherwise "Stack is empty".
        """
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            True if the stack is empty, otherwise False.
        """
        return len(self.items) == 0

    def size(self):
        """
        Return the size of the stack.

        Returns:
            The number of elements in the stack.
        """
        return len(self.items)

    def print_stack(self):
        """
        Print the stack.

        Returns:
            The list representation of the stack.
        """
        return self.items


stack = Stack()
print(stack.is_empty())  # True

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.print_stack())  # [10, 20, 30]

print("Top element is:", stack.peek())  # 30

print("Popped element:", stack.pop())  # 30

print(stack.print_stack())  # [10, 20]
