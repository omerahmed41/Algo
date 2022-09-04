def max_depth(root):
    if not root:
        return None

    _max = max(max_depth(root.left), max_depth(root.right))
    return _max + 1
