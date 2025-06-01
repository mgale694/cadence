from typing import Any
from ..shared import DoubleNode


class DoubleLinkedList:

    def __init__(self, initlist: list[Any] = None) -> None:
        self.head: DoubleNode = None
        self.tail: DoubleNode = None
        self.size = 0
        if initlist:
            for value in initlist:
                self.append(value)


    def __len__(self) -> int:
        """
        Returns the number of elements in the double linked list. Defining the 
        __len__ method allows the use of the built-in len() function on the
        double linked list.

        Returns:
            int: The number of elements in the double linked list.
        """
        return self.size
    
    def __getitem__(self, index: int) -> Any:
        """
        Retrieves the value at the specified index in the double linked list.
        This method allows for indexing into the double linked list using the 
        syntax `double_linked_list[index]`.

        Args:
            index (int): The index of the element to retrieve.

        Raises:
            IndexError: If the index is out of bounds (negative or greater than
            or equal to the size of the double linked list).

        Returns:
            Any: Value of DoubleNode at the specified index.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds.")

        # Optimize traversal: start from head or tail depending on index
        if index < self.size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.size - 1, index, -1):
                current = current.prev
        return current.value
    
    def __setitem__(self, index: int, value: Any) -> None:
        """
        Sets the value at the specified index in the double linked list.
        This method allows for setting values in the double linked list using
        the syntax `double_linked_list[index] = value`.

        Args:
            index (int): The index of the element to set.
            value (Any): The value to set at the specified index.

        Raises:
            IndexError: If the index is out of bounds (negative or greater than
            or equal to the size of the double linked list).
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds.")

        # Optimize traversal: start from head or tail depending on index
        if index < self.size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.size - 1, index, -1):
                current = current.prev
        current.value = value
    
    def __contains__(self, value: Any) -> bool:
        """
        Checks if a value is present in the double linked list.

        Args:
            value (Any): The value to check for in the double linked list.

        Returns:
            bool: True if the value is found, False otherwise.
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def __iter__(self):
        """
        Returns an iterator for the double linked list, allowing for iteration
        over its elements.

        Yields:
            Any: The next value in the double linked list.
        """
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __next__(self):
        """
        Returns the next value in the double linked list during iteration.

        Raises:
            StopIteration: When there are no more elements to iterate over.
        """
        if not hasattr(self, '_iterator'):
            self._iterator = self.head
        if self._iterator is None:
            raise StopIteration
        value = self._iterator.value
        self._iterator = self._iterator.next
        return value

    # Interaction methods
    def append(self, value: Any) -> None:
        """
        Appends a new value to the end of the double linked list.

        Args:
            value (Any): The value to append to the double linked list.
        """
        new_node = DoubleNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, value: Any) -> None:
        """
        Prepends a new value to the beginning of the double linked list.

        Args:
            value (Any): The value to prepend to the double linked list.
        """
        new_node = DoubleNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    # Output methods
    def to_list(self) -> list[Any]:
        """
        Converts the double linked list to a regular Python list.

        Returns:
            list[Any]: A list containing all values in the double linked list.
        """
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values

    def __str__(self) -> str:
        """
        Returns a string representation of the double linked list in the format
        [1 <-> 2 <-> 3].
        
        Returns:
            str: A string representation of the double linked list.
        """
        
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return f"[{' <-> '.join(values)}]" if values else "[Empty List]"
    
    def __repr__(self) -> str:
        """
        Returns a string representation of the double linked list.

        Returns:
            str: A string representation of the double linked list.
        """
        return f"{self.to_list()}"
    