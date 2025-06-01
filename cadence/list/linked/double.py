from typing import Any


class DoubleLinkedList:

    def __init__(self, default: list[Any] = None) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        # if default:
        #     for value in default:
        #         self.append(value)

    def __len__(self) -> int:
        """
        Returns the number of elements in the double linked list. Defining the 
        __len__ method allows the use of the built-in len() function on the
        double linked list.

        Returns:
            int: The number of elements in the double linked list.
        """
        return self.size
    
    