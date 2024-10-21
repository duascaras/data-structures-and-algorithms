"""
Stack class
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
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
