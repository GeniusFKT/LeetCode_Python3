# 268ms/74.80%
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self.hashmap.get(key) is None:
            return -1
        else:
            return self.hashmap[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.hashmap.pop(key, 0)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)