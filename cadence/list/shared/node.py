class Node:
    def __init__(self, value=None) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"Node({self.value})"

    def __str__(self) -> str:
        return str(self.value)


class SingleNode(Node):
    def __init__(self, value=None) -> None:
        super().__init__(value)
        self.next = None


class DoubleNode(Node):
    def __init__(self, value=None) -> None:
        super().__init__(value)
        self.next = None
        self.prev = None
