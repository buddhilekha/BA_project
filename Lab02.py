class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

#Activity 02
    def insert(self, key, val):
        hash_val = self.hash_function(key)
        if self.table[hash_val] is None:
            self.table[hash_val] = (key, val)

#Activity 03
    def search(self, key):
        hash_val = self.hash_function(key)
        if self.table[hash_val] is not None and self.table[hash_val][0] == key:
            return self.table[hash_val][1]
        return False

#Activity 04
    def delete(self, key):
        hash_value = self.hash_function(key)
        self.table[hash_val] = None


# Activity 05
hash_table = HashTable(20)

hash_table.insert(206037, "Sandunie")
hash_table.insert(206095, "Sasanga")
hash_table.insert(206098, "Madhushani")
hash_table.insert(206064, "Rashmi")
hash_table.insert(206100, "Dasuni")

#Activity 06
print(hash_table.search(206037))

