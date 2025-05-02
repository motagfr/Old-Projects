# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:16:05 2023

@author: M
"""

# Python program for implementation of queue

# import maxsize from sys module
# Used to return -infinite when stack is empty
from sys import maxsize

# Function to create a queue. It initializes size of queue as 0


def createQueuek():
    queue = []
    return queue

# Queue is empty when queue size is 0


def isEmpty(queue):
    return len(queue) == 0

# Function to add an item to queue. It increases size by 1


def enqueue(queue, item):
    queue.append(item)
    print(item + " enqueued ")

# Function to remove an item from queue. It decreases size by 1


def dequeue(queue):
    if (isEmpty(queue)):
        return str(-maxsize - 1)  # return minus infinite

    return queue.pop()

# Function to return the head of queue without removing it


def front(queue):
    if (isEmpty(queue)):
        return str(-maxsize - 1)  # return minus infinite
    return queue[0]


# Function to return the tail of queue without removing it
def rear(queue):
    if (isEmpty(queue)):
        return str(-maxsize - 1)  # return minus infinite

    return queue[-1]
