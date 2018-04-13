class HashTable(object):
    def __init__(self):
        # table 是用来存储数据的数组, 这个尺寸最好选素数, 可以得到更为合理的下标分布
        self.table_size = 10007
        self.table = [0] * self.table_size

    # 这个魔法方法用来实现 in 语法
    def __contains__(self, item):
        return self.has_key(item)
        
    def has_key(self, key):
        """
        检查一个 key 是否存在, 时间是 O(1)
        """
        index = self._index(key)
        # 取元素
        v = self.table[index]
        if isinstance(v, list):
            # 检查是否包含要找的 key
            for kv in v:
                if kv[0] == key:
                    return True
        # 如果得到的是 int 0 说明没找到, 返回 False
        # 如果得到的是 list 但是遍历结果没有我们要找的 key 也是没找到
        return False

    def _insert_at_index(self, index, key, value):
        v = self.table[index]
        data = [key, value]
        # 检查下标处是否是第一次插入数据
        if v == 0:
            # 如果是第一次, 就插入一个 list 来存（解决hash碰撞的问题）
            self.table[index] = [data]
        else:
            # 如果不是, 直接 append
            self.table[index].append(data)

    def add(self, key, value):
        # 先计算出下标
        index = self._index(key)
        # 在下标处插入元素
        self._insert_at_index(index, key, value)

    def get(self, key, default_value=None):
        index = self._index(key)
        # 取元素
        v = self.table[index]
        if isinstance(v, list):
            # 检查是否包含要找的 key
            for kv in v:
                if kv[0] == key:
                    return kv[1]
        return default_value

    def _index(self, key):
        # 计算出下标
        return self._hash(key) % self.table_size

    def _hash(self, s):
        n = 1
        f = 1
        for i in s:
            n += ord(i) * f
            f *= 10
        return n


def test():
    import uuid
    names = [
        'bluesky',
        'web',
        'python',
    ]
    ht = HashTable()
    for key in names:
        value = uuid.uuid4()
        ht.add(key, value)
        print('add', key, value)
    for key in names:
        v = ht.get(key)
        print('get', key, v)
    print('in', 'bluesky' in ht)


if __name__ == '__main__':
    test()
