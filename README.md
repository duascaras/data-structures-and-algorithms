# Data Structures

## Stack

A data structure in which all insertions and deletions are made at one end, called the top of the stack.

LIFO data structure: last in, first out.

### Common Stack Operations

- Push: push item to the top of the stack
- Pop: remove and return the top item
- Peek: return the top item without removing it
- Is_empty: return true if the stack is empty

## Depth-First Search (DFS)

Depth-First Search (DFS) is an algorithm used to traverse or search through data structures like graphs and mazes. It explores as far as possible along each branch before backtracking, making it a backtracking algorithm.

DFS typically uses a stack to keep track of unexplored nodes, pushing nodes onto the stack as it visits them and popping nodes when they are fully explored.

### DFS Characteristics

- Type: Graph/Tree traversal algorithm
- Strategy: Explores deep into each branch before backtracking
- Data Structure Used: Stack (can be implemented with recursion)
- Applications: Pathfinding, cycle detection, solving mazes, etc.

### DFS Algorithm Outline

``` note
1. Push the starting node onto the stack.
2. Pop a node from the stack.
3. If it's the goal, return the path.
4. If not, push all its unvisited neighbors onto the stack.
5. Repeat until the stack is empty or the goal is found.
```

## Queue
A data structure in which items are inserted at the back (tail) and removed from the front (head), following the First In, First Out (FIFO) principle.

### Queue Characteristics
FIFO Data Structure: The first item added to the queue will be the first one to be removed.

### Common Queue Operations

- Enqueue: add an item to the back of the queue
- Dequeue: remove and return the front item
- Peek: return the front item without removing it
- Is_empty: return true if the queue is empty
- Size: return the number of items in the queue
