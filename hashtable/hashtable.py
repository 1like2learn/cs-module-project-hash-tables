class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __repr__(self):
        return f"HashEntry({repr(self.key)},{repr(self.value)})"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity if capacity > 8 else 8
        self.table = [None] * self.capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        pass


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        hashValue = 14695981039346656037
        for c in key:
            hashValue *= 1099511628211
            hashValue = hashValue ^ ord(c)
            hashValue &= 0xffffffffffffffff
        return hashValue


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hashValue = 5381
        for c in key:
            hashValue = hashValue * 33 + ord(c)
            hashValue &= 0xffffffff
        return hashValue


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        entry = self.table[index]
        # If there is nothing at the index add the new pair
        if not entry:
            self.size += 1
            self.table[index] = HashTableEntry(key, value)
            # self.resize()
        # Otherwise we need to find the end of the linked list or overwrite entry
        else:
            # Overwrite if they have the same key
            if entry.key == key:
                self.table[index] = HashTableEntry(key, value)
            # Find the end of the linked list, if we find an entry with the same key overwrite it
            while entry.next:
                if entry.key == key:
                    entry = HashTableEntry(key, value)
                    return
                entry = entry.next
            # Once we've found the end of the list add the new entry
            self.size += 1
            entry.next = HashTableEntry(key, value)
            # self.resize()


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if not self.table[index]: # Nothing exists at this index
            print(key, "does not exist, nothing was deleted")

        else: # Something exists at this index

            # Store the current and previous entries
            previousEntry = None
            entry = self.table[index]

            # We're at the start of the linked list and a next value does not exists
            if not entry.next:
                self.size -= 1
                self.table[index] = None
                return entry.value
                
            # Loop while a next entry exists
            while entry: 

                # If we find the key we're looking for
                if entry.key == key:

                    # We're at the start of the linked list and a next value exists
                    if not previousEntry and entry.next:
                        self.size -= 1
                        self.table[index] = entry.next
                        return entry.value

                    # We're in the middle of the linked list and we knit the neighbors of the removed item together
                    else:
                        self.size -= 1
                        previousEntry.next = entry.next

                previousEntry = entry
                entry = entry.next

            # If we never find the key we return nothing
            print(key, "does not exist, nothing was deleted")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if not self.table[index]: # Nothing exists at this index key doesn't exist
            return None
        else: # Something exists at this index
            entry = self.table[index]
            
            # Loop until we're at the end of the list
            while entry:
                # If we find the key we want return it
                if entry.key == key:
                    return entry.value
                # Otherwise move down the list
                entry = entry.next
            
            # Didn't find anything with the key
            return None


    def resize(self, new_capacity = None):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        if (self.size / self.capacity) > 0.7 or new_capacity:
            # Double capacity
            self.capacity = new_capacity if new_capacity else self.capacity * 2
            # Store the old table
            oldTable = self.table
            # Create a new table with new capacity
            self.table = self.capacity * [None]
            # Loop through all the old entries and add them to the new 
            for entry in oldTable:
                # Loop while not at the end of the linked list
                while entry:
                    self.put(entry.key, entry.value)
                    entry = entry.next
                





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
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    print("")
