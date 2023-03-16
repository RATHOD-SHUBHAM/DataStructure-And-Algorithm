class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
		self.len = 0
		self.hash = {}
		self.dll = DoubleLinkList()