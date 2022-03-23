"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Dev Patel
ID:      212325400
Email:   pate5400@mylaurier.ca
__updated__ = "2022-03-12"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List
from Food import Food
from copy import deepcopy
# Constants


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        stack.push(source.pop())
    return


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    # print(stack.is_empty())

    while not stack.is_empty():
        v = stack.pop()
        target.insert(0, v)

    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    stack = Stack()
    stack.push("--------------------- ")
    stack.push("Food menu")
    e = stack.is_empty()
    print("elements of stack :")
    for j in stack:
        print(j)
    print()
    print(f"check stack empty/not: {e}")
    for i in source:
        pu = stack.push(i)
        print(f"pushing element to stack:{i}")
    f = stack.is_empty()
    print()
    print(f"check stack after push empty/not :{f}")
    print("final elements of stack:")
    for d in stack:
        print(d)
    po = stack.pop()
    print(f"pop the stack :{po}")
    pe = stack.peek()
    print(f"peek the stack: {pe}")
    return


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while len(source) > 0:
        queue.insert(source.pop(0))

    return


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not queue.is_empty():
        v = queue.remove()
        target.append(v)
    # print(target)
    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()
    q.insert("------------")
    q.insert("Food menu")
    b = q.is_empty()
    print("elements of queue :")
    for j in q:
        print(j)
    print()
    print(f"check stack empty/not: {b}")
    for i in a:
        pu = q.insert(i)
        print(f"inserting element to queue:{i}")
    f = q.is_empty()
    print()
    print(f"check queue after insert empty/not :{f}")
    print("final elements of queue:")
    for d in q:
        print(d)
    po = q.remove()
    print(f"remove {po} from the queue")
    pe = q.peek()
    print(f"peek the queue: {pe}")
    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    queue = Queue()

    array_to_queue(queue, source)
    while not queue.is_empty():
        pq.insert(queue.remove())
    # for i in pq:
        # sprint(i)
    return


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        target.append(pq.remove())
    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    empty = pq.is_empty()
    print(f"Is this queue empty:{empty}")

    for i in a:
        pq.insert(i)
    re = pq.remove()
    print(f"{re} was removed")

    pe = pq.peek()
    print(f"{pe} was peeked")

    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:
        llist.append(source[0])
        source.remove(source[0])
    return


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not llist.is_empty():
        value = llist.remove(llist[0])
        target.append(value)
    return


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()
    empty = lst.is_empty()
    print(f"Is this list empty:{empty}")
    x = 0
    for i in source:
        lst.insert(x, i)
        print(f"{i}is inserted at {x} index")
        x += 1
    # lst.append(100)
    #print(f"100 is appended")
    re = lst.remove(lst[1])
    print(f"{re} was removed from 1 index")
    a = lst.append(Food("Butter Chicken", 2, None, None))

    pe = lst.peek()
    print(f"{pe} was peeked")
    n = lst.count([Food("Butter Chicken", 2, None, None)])
    print(f"1 is repeated {n} times")
    max = lst.max()
    print(f"maximum number:{max}")
    valuem = lst.min()
    print(f"minimum number:{valuem}")
    ni = lst.index([Food("Butter Chicken", 2, None, None)])
    print(f"key is at index:{ni} ")
    nf = lst.find(Food("Butter Chicken", 2, False, 490))
    print(f"find number  :{nf}")
    return
