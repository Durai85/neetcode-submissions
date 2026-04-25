class MyHashSet:

    def __init__(self):
        self.dic = set()

    def add(self, key: int) -> None:
        self.dic.add(key) 

    def remove(self, key: int) -> None:
        if key in self.dic:
            self.dic.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.dic


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)