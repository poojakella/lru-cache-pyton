class LRUCache:
    def __init__(self, capacity):
        self.capacity=capacity
        self.cache={}
        self.order=[]
        self.hits=0
        self.misses=0
    def get(self,key):
        if key not in self.cache:
            self.misses+=1
            return -1
        self.hits+=1
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]
    def put(self,key,value):
        if key in self.cache:
            self.order.remove(key)
        self.cache[key]=value
        self.order.append(key)
        if  len(self.cache)>self.capacity:
            lru_key=self.order.pop(0)
            del self.cache[lru_key]
    def display(self):
        print("\n==== LRU CACHE STATUS ====")
        print("Cache:",self.cache)
        print("Order:",self.order)
        print("Cache Hits:",self.hits)
        print("Cache Misses:",self.misses)
        total=self.hits+self.misses
        if total>0:
            hit_rate=(self.hits/total)*100
        else:
            hit_rate=0
        print("Hit Rate:",round(hit_rate,2),"%")