from ..shared import Node
from typing import Any

class SingleLinkedList:

    def __init__(self, default: list[Any] = None) -> None:
        self.head: Node = None
        self.size = 0
        if default:
            for value in default:
                self.append(value)

    def __len__(self) -> int:
        """
        Returns the number of elements in the linked list. Defining the 
        __len__ method allows the use of the built-in len() function on the
        linked list.

        Returns:
            int: The number of elements in the linked list.
        """
        return self.size
    
    def __getitem__(self, index: int) -> Any:
        """
        Retrieves the value at the specified index in the linked list.
        This method allows for indexing into the linked list using the 
        syntax `linked_list[index]`.

        Args:
            index (int): The index of the element to retrieve.

        Raises:
            IndexError: If the index is out of bounds (negative or greater than
            or equal to the size of the linked list).

        Returns:
            Any: Value of Node at the specified index.
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds.")
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def __setitem__(self, index: int, value: Any) -> None:
        """
        Sets the value at the specified index in the linked list.
        This method allows for setting values using the syntax 
        `linked_list[index] = value`.

        Args:
            index (int): The index of the element to set.
            value (Any): The value to set at the specified index.

        Raises:
            IndexError: If the index is out of bounds (negative or greater than
            or equal to the size of the linked list).
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds.")
        
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value
    
    def __contains__(self, value: Any) -> bool:
        """
        Checks if a value is present in the linked list.
        This method allows for using the `in` keyword to check for 
        membership in the linked list.

        Args:
            value (Any): The value to check for in the linked list.

        Returns:
            bool: True if the value is found, False otherwise.
        """
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def append(self, value: Any) -> None:
        """
        Appends a new value to the end of the linked list.

        Args:
            value (Any): The value to append to the linked list.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def to_list(self) -> list[Any]:
        """
        Converts the linked list to a Python list.

        Returns:
            list[Any]: A list containing all the values in the linked list.
        """
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result
    
    def __str__(self) -> str:
        """
        Returns a string representation of the linked list in the format [1 -> 2 -> 3].

        Returns:
            str: A string representation of the linked list.
        """
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return f"[{' -> '.join(values)}]" if values else "[Empty List]"
    
    def __repr__(self) -> str:
        """
        Returns a string representation of the linked list for debugging purposes.
        This representation is similar to the output of `to_list()`.

        Returns:
            str: A string representation of the linked list.
        """
        return f"{self.to_list()}"
