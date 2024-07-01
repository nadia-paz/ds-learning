"""
Python's built-in hash table is a dictionary.
HT stores a key: value pairs. HTs use mathematical mapping to compress the key space. 
They run a math function to get the number of the index where the key: value pair is going to be stored
HTs are deterministic: meaning that running the key through the function will always return the same  number
HTs work one way, you can not get a key from the number.
It's recommended to use a prime number as a size(number) of the bins.

Collisions occur when different keys return the same number. There are different ways how to solve the proble:
- Linear Probation (the next available index)
- List of dictionaries
- Linked List, etc

Simple implementation of HashTable class in Python:
"""

class HashTable:
    def __init__(self, size=7):
        # createa a list of n-size with None values
        self.data_map = [None] * size

    def __hash(self, key):
        """
        Private Hash method, transforms a key into a number using a formula:
        (my_hash + ASCII code of the letter * prime number) % (size of the bins)
        """
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        # saves the key: value pair as a list [key, value] on the calculated index
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        bin = self.data_map[index]
        if bin is not None:
            for pair in bin:
                if pair[0] == key:
                    # return value
                    return pair[1]
        return None

    def get_keys(self):
        keys = []
        for bin in self.data_map:
            if bin is not None:
                for pair in bin:
                    keys.append(pair[0])
        return keys

    def print_hash_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

ht = HashTable()


ht.set_item("book", 143)
ht.set_item("magazines", 1200)
ht.set_item("newspapers", 34500)
# print(ht.data_map)

ht.print_hash_table()

print(ht.get_item("book")) # 143
print(ht.get_item("books")) # None
print(ht.get_item("magazines")) # 1200
print(ht.get_item("newspapers")) # 34500

print(ht.get_keys())