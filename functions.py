def text_letters(text):
    new_text = ''
    for char in text:
        if char.isalpha():
            new_text += char.lower()
        elif char.isnumeric():
            new_text += char
    return new_text


def freq(text):
    freq_dict = {}
    for char in text:
        if char in freq_dict.keys():
            freq_dict[char] += 1
        else:
            freq_dict[char] = 0
    return freq_dict


def bfs(tree):
    result = {}
    queue = [tree.root]

    result[tree.root.value] = ''
    while len(queue) > 0:
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
            result[node.left.value] = result[node.left.parent.value] + '.'

        if node.right is not None:
            queue.append(node.right)
            result[node.right.value] = result[node.right.parent.value] + '-'
    del result[0]
    return result