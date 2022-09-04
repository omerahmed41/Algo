def max_depth(root):
    if not root:
        return None

    levels = 0
    queue = [root]

    while queue:
        count = len(queue)

        node = queue.pop(0)
        for i in range(count):
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        levels +=1

    return levels
