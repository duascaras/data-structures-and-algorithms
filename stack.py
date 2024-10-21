class Stack:
    def __init__(self):
        '''
        Initializes an empty stack using a Python list.
        The list will store elements in a LIFO (last-in, first-out) manner.
        '''
        self.items = []

    def is_empty(self):
        '''
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        '''
        return not self.items

    def push(self, item):
        '''
        Adds an item to the top of the stack.

        Parameters:
            item: The element to be added to the stack.
        '''
        self.items.append(item)

    def pop(self):
        '''
        Removes and returns the item from the top of the stack.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty when trying to pop.
        '''
        return self.items.pop()

    def peek(self):
        '''
        Returns the item at the top of the stack without removing it.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty when trying to peek.
        '''
        return self.items[-1]

    def size(self):
        '''
        Returns the number of items in the stack.

        Returns:
            int: The number of elements currently in the stack.
        '''
        return len(self.items)

    def __str__(self):
        '''
        Returns a string representation of the stack.

        Returns:
            str: A string showing the current elements in the stack.
        '''
        return str(self.items)


if __name__ == "__main__":
    def reverse_string(my_string):
        # Use the "accumulator pattern."
        # Start with an "empty bucket" of the right data type,
        # and build the solution by filling the bucket within a loop.
        reversed_string = ""

        # Create a new stack
        s = Stack()

        # Iterate through my_string and push the characters onto the stack
        for char in my_string:
            s.push(char)

        # Use a while loop with the exit condition that the stack is empty.
        # Within this loop, update reversed_string with characters popped off the stack.
        while not s.is_empty():
            reversed_string += s.pop()

        # Return the result
        return reversed_string

    result = reverse_string(
        "!sedarg doog teg annoG\nssalc ni sessa rieht kcik annoG")
    print(result)
