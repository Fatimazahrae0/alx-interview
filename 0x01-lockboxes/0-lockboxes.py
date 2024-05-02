#!/usr/bin/python3
"""
This is a module that provides a function for determining if all
boxes in a given list can be opened.
"""
def canUnlockAll(boxes):
    if not boxes:
        return False

    visited = [False] * len(boxes)
    visited[0] = True
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if 0 <= key < len(boxes) and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
