
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
class BinarySearchTree:

    def __init__(self):
        self.root = None

    def __len__(self):
        return self._len_rec(self.root)
    
    def _len_rec(self, node: Node):
        if node is None:
            return 0
        return 1 + self._len_rec(node.left) + self._len_rec(node.right)

    def insert(self, key) -> None:
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, node: Node, key) -> None:
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_rec(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_rec(node.right, key)
    
    # Output methods
    def __str__(self) -> str:
        if not self.root:
            return "<empty tree>"
        lines = self._build_tree_string(self.root, 0, False, '-')[0]
        return "\n" + "\n".join((line.rstrip() for line in lines))

    def _build_tree_string(self, root, curr_index, include_index=False, delimiter='-'):
        """Recursively walk down the binary tree and build a pretty-print string."""
        if root is None:
            return [], 0, 0, 0

        line1 = []
        line2 = []
        node_repr = f'{root.val}'

        new_root_width = gap_size = len(node_repr)

        # Get the left and right sub-boxes, their widths, and root repr positions
        l_box, l_box_width, l_root_start, l_root_end = self._build_tree_string(root.left, 2 * curr_index + 1, include_index, delimiter)
        r_box, r_box_width, r_root_start, r_root_end = self._build_tree_string(root.right, 2 * curr_index + 2, include_index, delimiter)

        # Draw the branch connecting the current root node to left sub-box
        # Pad the line with whitespaces if necessary
        if l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            line1.append(' ' * (l_root + 1))
            line1.append('_' * (l_box_width - l_root))
            line2.append(' ' * l_root + '/')
            line2.append(' ' * (l_box_width - l_root))
        # No left subtree
        else:
            line1.append('')
            line2.append('')

        # Print the value of the current node
        line1.append(node_repr)
        line2.append(' ' * new_root_width)

        # Draw the branch connecting the current root node to the right sub-box
        if r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            line1.append('_' * r_root)
            line1.append(' ' * (r_box_width - r_root + 1))
            line2.append(' ' * r_root + '\\')
            line2.append(' ' * (r_box_width - r_root))
        else:
            line1.append('')
            line2.append('')

        # Combine left and right sub-boxes with root
        gap = ' ' * new_root_width
        new_box = [''.join(line1), ''.join(line2)]

        # Append left and right sub-boxes line by line
        for i in range(max(len(l_box), len(r_box))):
            left_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
            right_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
            new_box.append(left_line + gap + right_line)

        return new_box, l_box_width + new_root_width + r_box_width, l_box_width + new_root_width // 2, l_box_width + new_root_width // 2 + len(node_repr) - 1
    
    # def __str__(self) -> str:
    #     return self._str_rec(self.root)
    
    # def _str_rec(self, node: Node) -> str:
    #     if node is None:
    #         return ""
    #     left_str = self._str_rec(node.left)
    #     right_str = self._str_rec(node.right)
    #     return f"{left_str} {node.val} {right_str}".strip()
    
    def __repr__(self):
        return f"BinarySearchTree({self.inorder()})"
    
