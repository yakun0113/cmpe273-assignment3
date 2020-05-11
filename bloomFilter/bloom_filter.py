import math 
import mmh3 
from bitarray import bitarray 
  
class BloomFilter(object): 
	def __init__(self, NUM_KEYS, FALSE_POSITIVE_PROBABILITY):
		self.FALSE_POSITIVE_PROBABILITY = FALSE_POSITIVE_PROBABILITY
		self.bit_array_use = int(-(NUM_KEYS * math.log(FALSE_POSITIVE_PROBABILITY))/(math.log(2)**2))
		self.hash_counts = int((self.bit_array_use/NUM_KEYS) * math.log(2))
		self.bit_array_size = bitarray(self.bit_array_use)
		self.bit_array_size.setall(0)

	def add(self, item):
		digests = []
		for i in range (self.hash_counts):
			digest = mmh3.hash(item, i) % self.bit_array_use
			self.bit_array_size[digest] = True

	def is_member(self, item):
		for i in range (self.hash_counts):
			digest = mmh3.hash(item, i) % self.bit_array_use
			if self.bit_array_size[digest] == False:
				return False
		return True
