from collections import deque

stack = [1, 3, 54, 2, 6, 84, 3, 5, 8, 7, 0]


def reverse(stack):
    queue = deque()
    while stack:
        queue.append(stack.pop())
    while queue:
        stack.append(queue.popleft())

    return stack


reverse(stack)
