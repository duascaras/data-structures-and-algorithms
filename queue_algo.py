"""
Queue class
"""

from collections import deque


class Queue:
    def __init__(self):
        '''
        Initializes an empty queue using a deque (double-ended queue),
        which allows fast appends and pops from both ends.
        '''
        self.items = deque()

    def is_empty(self):
        '''
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        '''
        return not self.items

    def enqueue(self, item):
        '''
        Adds an item to the back of the queue.

        Parameters:
            item: The element to be added to the queue.
        '''
        self.items.append(item)

    def dequeue(self):
        '''
        Removes and returns the item from the front of the queue.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty when trying to dequeue.
        '''
        return self.items.popleft()

    def size(self):
        '''
        Returns the number of items in the queue.

        Returns:
            int: The number of elements currently in the queue.
        '''
        return len(self.items)

    def peek(self):
        '''
        Returns the item at the front of the queue without removing it.

        Returns:
            The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty when trying to peek.
        '''
        return self.items[0]

    def __str__(self):
        '''
        Returns a string representation of the queue.

        Returns:
            str: A string showing the current elements in the queue.
        '''
        return str(self.items)


if __name__ == "__main__":
    # Complete this function by using a sequence of enqueue() and dequeue()
    # operations, so the final state of my_queue.items is
    # deque(['the', 'aardvark', 'wore', 'a', 'silly', 'hat'])
    output = deque(['the', 'aardvark', 'wore', 'a', 'silly', 'hat'])

    def queue_challenge():
        my_queue = Queue()
        word_list = ["wore", "a", "silly", "hat", "the", "aardvark"]

        for word in word_list:
            my_queue.enqueue(word)

        temp_queue = Queue()

        for target_word in output:
            while my_queue.peek() != target_word:
                my_queue.enqueue(my_queue.dequeue())
            temp_queue.enqueue(my_queue.dequeue())

        my_queue.items = temp_queue.items

        return my_queue.items

    result = queue_challenge()
    print(result)
