import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict();
        

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return None;
        

    def put(self, key, value):
        try:
            self.cache.pop(key)
            # print(self.cache[0])
            # print(self.cache[1])
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last = False)
        self.cache[key] = value


def lru_cache(capacity):
    obj = LRUCache(capacity)

    def Inner(func): 
  
        def wrapper(*args, **kwargs):
            key = args[0]

            if obj.get(key) == None:
            	value = func(key)
            	obj.put(key, value)
            	return value
            else:
            	return obj.get(key)
              
        return wrapper

    return Inner
