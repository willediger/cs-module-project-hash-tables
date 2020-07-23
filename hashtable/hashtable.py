class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableList:
    def __init__(self, head=None):
        self.head = head
    
    def insert_at_head(self, key, value):
        entry = HashTableEntry(key, value)
        entry.next = self.head
        self.head = entry
        return entry
    
    def put(self, key, value):
        curr = self.head

        #if found, update value, returning
        #in tuple along with 0 to indicate
        #no entries added to list
        while curr is not None:
            if curr.key == key:
                curr.value = value
                return (curr, 0)
            curr = curr.next
        
        #if not found, insert at head, returning
        #in tuple along with 1 to indicate
        #entry added to list
        return (self.insert_at_head(key,value), 1)

    def get(self, key):
        curr = self.head

        #if found return entry
        while curr is not None:
            if curr.key == key:
                return curr.value
            curr = curr.next

        return None

    def delete(self, key):
        curr = self.head

        if curr.key == key:
            self.head = curr.next
            #0 indicates head was last entry
            return (curr, 0)
        prev = curr
        curr = curr.next

        while curr is not None:
            if curr.key == key:
                prev.next = curr.next
                #1 indicates head was not last entry
                return (curr, 1)
            prev = curr
            curr = curr.next

        print("Key not found")
        return None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

FNV1A_64_OFFSET = 0xcbf29ce484222325
FNV1A_64_PRIME = 0x100000001b3

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = max(capacity, MIN_CAPACITY)
        self.table = [None]*self.capacity
        self.items_count = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.table)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.items_count/len(self.table)


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        hash_val = FNV1A_64_OFFSET

        for character in key:

            # Xor with the current character
            hash_val ^= ord(character)

            # Multiply by prime
            hash_val *= FNV1A_64_PRIME

            # Clamp
            hash_val &= 0xffffffffffffffff

        # Return the final hash as a number
        return hash_val


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        hash_index = self.hash_index(key)
        if self.table[hash_index] is not None:
            added = self.table[hash_index].put(key, value)
            self.items_count += added[1]
            return added[0]
        else:
            node = HashTableEntry(key, value)
            self.table[hash_index] = HashTableList(node)
            self.items_count += 1
            return node


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hash_index = self.hash_index(key)
        if self.table[hash_index] is None:
            print("Key not found")
        else:
            deleted = self.table[hash_index].delete(key)

            if deleted is not None:
                self.items_count -= 1

            if deleted[1] == 0:
                self.table[hash_index] = None

            return deleted[0]



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hash_index = self.hash_index(key)
        if self.table[hash_index] is not None:
            return self.table[hash_index].get(key)
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
