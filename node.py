from __future__ import annotations


class Node:
    def __init__(self, value: str, position: tuple, parent: Node = None):
        self.value = value
        self.position = position
        self.parent = parent

    def __repr__(self):
        return self.value + str(self.position)
