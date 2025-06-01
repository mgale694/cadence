
class Node:

    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f"Node({self.value})"

    def __str__(self) -> str:
        return str(self.value)