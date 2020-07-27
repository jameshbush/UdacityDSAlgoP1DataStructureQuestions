import hashlib
import time

class Node:
    def __init__(self, block, next=None, prev=None):
        self.block = block
        self.next = next
        self.prev = prev

class Block:
    def __init__(self, timestamp, data, previous_hash=''):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_data = self.data.encode('utf-8')
        hash_time = str(self.timestamp).encode('utf-8')
        hash_prev = self.previous_hash.encode('utf-8')

        sha.update(hash_data)
        sha.update(hash_time)
        sha.update(hash_prev)

        return sha.hexdigest()

    def __str__(self):
        return "{} {} {}".format(
            self.hash[0:7],
            time.asctime(time.localtime(self.timestamp)),
            self.data,
        )

class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_block(self, data):
        block_params = [time.time(), data]
        if self.tail:
            block_params.append(self.tail.block.hash)

        block = Block(*block_params)
        node = Node(block)

        if self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head, self.tail = node, node

    def print_blockchain(self):
        node = self.head
        while node:
            print(node.block)
            node = node.next

chain = Blockchain()
chain.add_block('Hello, World!')
time.sleep(1)
chain.add_block('Second block')
time.sleep(1)
chain.add_block('Third block')

chain.print_blockchain()
