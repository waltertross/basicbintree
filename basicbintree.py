"""
basicbintree - a basic binary tree

Copyright (c) 2021, Walter Tross <waltertross at gmail dot com>
"""

from __future__ import annotations
from typing import Any, List, Optional


class Node:
    """The (root) node of the basic binary tree."""

    def __init__(self, value: Any,
                 left:  Optional[Node] = None,
                 right: Optional[Node] = None):
        """Make the Node with any non-None value and optional subnodes."""

        if value is None:
            raise ValueError("Node value may not be None")
        self.value, self.left, self.right = value, left, right

    def set_level(self, values: List[Any]) -> None:
        """Set the 2**n values (n>=1) of a complete tree level.

        Use None for missing nodes. Descendants are cleared.
        """

        count = len(values)
        if count & (count - 1) or count < 2:
            raise ValueError("len(values) must be a power of 2 >= 2")
        if count > 2:
            if self.left:
                self.left.set_level(values[:count // 2])
            if self.right:
                self.right.set_level(values[count // 2:])
        else:
            self.left  = None if values[0] is None else Node(values[0])
            self.right = None if values[1] is None else Node(values[1])

    def height(self) -> int:
        """Get the edge count to the farthest leaf of this (sub)tree."""

        return max(1 + self.left .height() if self.left  else 0,
                   1 + self.right.height() if self.right else 0)

    def max_str_len(self) -> int:
        """Get the max len of all value strings of this (sub)tree."""

        return max(len(str(self.value)),
                   self.left .max_str_len() if self.left  else 0,
                   self.right.max_str_len() if self.right else 0)

    def print_tree(self, bottom_step: int = -1) -> None:
        """Print the tree having this node as root.

        A bottom_step > 0 is the step between leaf nodes.
        A bottom_step <= 0 is (without the sign) the spacing between
        leaf nodes, assuming nodes have the max width found in the tree.
        """

        w = self.max_str_len()
        if bottom_step <= 0:
            bottom_step = w + abs(bottom_step)
        shift = round(bottom_step / 2)
        height = self.height()
        step = bottom_step * 2 ** height
        print(f"{' '*(round(step / 2) - shift)}{self.value:{w}}")
        parents = [self]
        for h in range(height):
            row = [n for p in parents
                   for n in ((p.left, p.right) if p else (None, None))]
            step //= 2
            print(' '*(round(step / 2) - shift), end='')
            print((' '*(step - w)).join(f"{n.value:{w}}" if n else ' '*w
                                        for n in row))
            parents = row


if __name__ == "__main__":
    root = Node(1)
    root.print_tree()
    for level in range(1, 7):
        start = 2 ** level
        stop  = 2 ** (level + 1)
        root.set_level([i for i in range(start, stop)])
        print('=' * 50)
        root.print_tree()
    root.set_level([None, None, None, 'A'])
    root.set_level([None] * 6 + ['B', None])
    print('=' * 50)
    root.print_tree()
