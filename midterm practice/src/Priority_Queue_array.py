"""
-------------------------------------------------------
Array version of the Priority Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 Spring 2019
__updated__ = "2022-02-14"
-------------------------------------------------------
"""
from copy import deepcopy


class Priority_Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty priority queue.
        Use: pq = Priority_Queue()
        -------------------------------------------------------
        Returns:
            a new Priority_Queue object (Priority_Queue)
        -------------------------------------------------------
        """
        self._values = []
        self._first = None
        return

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the priority queue.
        Use: n = len(pq)
        -------------------------------------------------------
        Returns:
            the number of values in the priority queue.
        -------------------------------------------------------
        """
        # Your code here

        return len(self._values)

    def _set_first(self):
        """
        -------------------------------------------------------
        Private helper function to set the value of _first.
        _first is the index of the value with the highest
        priority in the priority queue. None if queue is empty.
        Use: self._set_first()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here
        if len(self._values) == 0:
            self._first = None
        else:
            self._first = 0
            for i in range(1, len(self._values)):
                if self._values[i] < self._values[self._first]:
                    self._first = i

        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target priority queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based priority queue (Priority_Queue)
            source2 - an array-based priority queue (priority)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here
        while len(source1._values) > 0 and len(source2._values) > 0:
            self._values.append(deepcopy(source1._values.pop(0)))
            self._values.append(deepcopy(source2._values.pop(0)))
        while len(source1._values) > 0:
            self._values.append(deepcopy(source1._values.pop(0)))
        while len(source2._values) > 0:
            self._values.append(deepcopy(source2._values.pop(0)))
        source1._first = None
        source2._first = None
        self._set_first()
        return

    def insert(self, value):
        """
        -------------------------------------------------------
        A copy of value is appended to the end of the the priority queue
        Python list, and _first is updated as appropriate to the index of
        value with the highest priority.
        Use: pq.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here
        self._values.append(deepcopy(value))
        if self._first is None:
            self._first = 0
        else:
            if self._values[self._first] > value:
                self._first = len(self._values) - 1
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the priority queue is empty.
        Use: b = pq.is_empty()
        -------------------------------------------------------
        Returns:
            True if priority queue is empty, False otherwise.
        -------------------------------------------------------
        """
        # Your code here

        return len(self._values) == 0

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the highest priority value of the priority queue.
        Use: v = pq.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the highest priority value in the priority queue -
                the value is not removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty priority queue'

        # Your code here

        return deepcopy(self._values[self._first])

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns the highest priority value from the priority queue.
        Use: value = pq.remove()
        -------------------------------------------------------
        Returns:
            value - the highest priority value in the priority queue -
                the value is removed from the priority queue. (?)
        -------------------------------------------------------
        """
        assert (len(self._values) >
                0), 'Cannot remove from an empty priority queue'

        # Your code here
        v = self._values.pop(self._first)
        self._set_first()

        return v

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits a priority queue into two with values going to alternating
        priority queues. The source priority queue is empty when the method
        ends. The order of the values in source is preserved.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - a priority queue that contains alternating values
                from the current queue (Priority_Queue)
            target2 - priority queue that contains  alternating values
                from the current queue  (Priority_Queue)
        -------------------------------------------------------
        """
        # Your code here
        t1 = Priority_Queue()
        t2 = Priority_Queue()
        while len(self._values) > 0:
            t1.insert(deepcopy(self._values.pop(0)))
            if len(self._values) > 0:
                t2.insert(deepcopy(self._values.pop(0)))
        self._first = None
        t1._set_first()
        t2._set_first()
        return t1, t2

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits a priority queue into two depending on an external
        priority key. The source priority queue is empty when the method
        ends. The order of the values from source is preserved.
        Use: target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a data object (?)
        Returns:
            target1 - a priority queue that contains all values
                with priority higher than key (Priority_Queue)
            target2 - priority queue that contains all values with
                priority lower than or equal to key (Priority_Queue)
        -------------------------------------------------------
        """
        # Your code here
        t1 = Priority_Queue()
        t2 = Priority_Queue()
        while len(self._values) > 0:
            t = self._values.pop(0)
            if t < key:
                t1.insert(deepcopy(t))
            else:
                t2.insert(deepcopy(t))
        t1._set_first()
        t2._set_first()
        self._first = None

        return t1, t2

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the priority queue
        from front to rear. Not in priority order.
        Use: for value in pq:
        -------------------------------------------------------
        Returns:
            value - the next value in the priority queue (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
