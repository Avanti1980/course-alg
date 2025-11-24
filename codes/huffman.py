from queue import PriorityQueue


class HuffmanNode:  # 编码树结点类
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):  # 比较两个HuffmanNode实例时调用
        return self.frequency < other.frequency


def get_min_freq(l):  # 删除并返回结点列表中频率最小的结点
    node, index = l[0], 0
    for i in range(1, len(l)):
        if l[i] < node:
            node, index = l[i], i
    return l.pop(index)


def merge(left_node, right_node):  # 合并两个结点
    merged_node = HuffmanNode(None, left_node.frequency + right_node.frequency)  # 合并两个结点
    merged_node.left, merged_node.right = left_node, right_node
    return merged_node


def build_huffman_tree_elementary(C):  # 用列表保存结点
    l = [HuffmanNode(symbol, frequency) for symbol, frequency in C.items()]

    while len(l) > 1:  # 最终l中只剩编码树的根结点
        left_node = get_min_freq(l)  # 寻找频率最小的结点
        right_node = get_min_freq(l)  # 寻找频率次小的结点
        l.append(merge(left_node, right_node))  # 插入合并的结点

    return l[0]


def build_huffman_tree_advanced(C):  # 用优先队列保存结点
    q = PriorityQueue()
    for symbol, frequency in C.items():
        q.put(HuffmanNode(symbol, frequency))  # 初始化队列

    while q.qsize() > 1:   # 最终q中只剩编码树的根结点
        left_node = q.get()  # 寻找频率最小的结点
        right_node = q.get()  # 寻找频率次小的结点
        q.put(merge(left_node, right_node))  # 插入合并的结点

    return q.get()


def huffman_codes(node, current_code="", code_map=None):  # 递归保存字符的编码
    if code_map is None:
        code_map = {}

    if node is not None:
        if node.symbol is not None:  # 字符对应的结点
            code_map[node.symbol] = current_code
        huffman_codes(node.left, current_code + "0", code_map)
        huffman_codes(node.right, current_code + "1", code_map)

    return code_map


C = {"a": 45, "b": 13, "c": 12, "d": 16, "e": 9, "f": 5}

huffman_tree_root = build_huffman_tree_elementary(C)
huffman_code_map = huffman_codes(huffman_tree_root)
for symbol, code in huffman_code_map.items():
    print(f"{symbol}: {code}")

huffman_tree_root = build_huffman_tree_advanced(C)
huffman_code_map = huffman_codes(huffman_tree_root)
for symbol, code in huffman_code_map.items():
    print(f"{symbol}: {code}")
# ----------------------------------------------------
# a: 0
# c: 100
# b: 101
# f: 1100
# e: 1101
# d: 111
# a: 0
# c: 100
# b: 101
# f: 1100
# e: 1101
# d: 111
