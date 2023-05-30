#!/usr/bin/env python
# coding: utf-8

# # Python Data Structure Practice

# ## Linked List

# In[ ]:


class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  # Add code below
  def insert_end(self, value):
    newNode = Node(value)
    if (self.head_node == None):
      self.head_node = newNode
      return
    else:
      temp = self.head_node
      while(temp.next_node != None):
        temp = temp.next_node 
      temp.next_node = newNode
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
  def print(self):
    current_node = self.get_head_node()
    while current_node is not None:
      print(f"{current_node.get_value()}", end=" ")
      current_node = current_node.get_next_node()
    print()
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node


# ## Hashmaps

# In[ ]:


class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]
    if current_array_value is None:
      self.array[array_index] = [key, value]
      return
    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return
    # Collision!
    number_collisions = 1
    while(current_array_value[0] != key):
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]
      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return
      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return
      number_collisions += 1
    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]
    if possible_return_value is None:
      return None
    if possible_return_value[0] == key:
      return possible_return_value[1]
    retrieval_collisions = 1
    while (possible_return_value != key):
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]
      if possible_return_value is None:
        return None
      if possible_return_value[0] == key:
        return possible_return_value[1]
      number_collisions += 1
    return

hash_map = HashMap(15)
hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')
print(hash_map.retrieve('gabbro'))
print(hash_map.retrieve('sandstone'))
print(hash_map.retrieve('gneiss'))


# ## Node + Stack Combo

# In[ ]:


from node import Node
class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.set_next_node(self.top_item)
      self.top_item = item
      self.size += 1
      print("Adding {} to the pizza stack!".format(value))
    else:
      print("No room for {}!".format(value))

  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      print("Delivering " + item_to_remove.get_value())
      return item_to_remove.get_value()
    print("All out of pizza.")

  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0
  
# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have 
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")
# Uncomment the push() statement below:
pizza_stack.push("pizza #7")
# Delivering pizzas from the top of the stack down
print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
# Uncomment the pop() statement below:
pizza_stack.pop()


from stack import Stack
print("\nLet's play Towers of Hanoi!!")
#Creating the Stacks
stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks += [left_stack, middle_stack, right_stack]
#Setting up the game
num_disks = int(input("\nHow many disks do you want to play with? \n(Must have a minimum of three!)\n"))
while num_disks < 3:
  print("Please pick a number greater than 3!")
else:
  pass
for disk in range (num_disks, 0, -1):
  left_stack.push(disk)
#left_stack.print_items()
num_optimal_moves = 2 ** num_disks - 1
print("\nThe fastest you can solve this game is in {0} moves".format(num_optimal_moves))
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
     name = stacks[i].get_name()
     letter = choices[i]
     print("Enter {0} for {1}".format(letter, name))
  user_input = input("")
  if user_input in choices:
    for i in range(len(stacks)):
      return stacks[i]


# ## Node + Singly Linked Lists

# In[ ]:


class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value

class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
  
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node
    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)
    self.head_node = new_head
    if self.tail_node == None:
      self.tail_node = new_head


  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node
    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)
    self.tail_node = new_tail
    if self.head_node == None:
      self.head_node = new_tail



  def remove_head(self):
    removed_head = self.head_node

    if removed_head == None:
      return None
    self.head_node = removed_head.get_next_node()

    if self.head_node != None:
      self.head_node.set_prev_node(None)

    if removed_head == self.tail_node:
      self.remove_tail()
    return removed_head.get_value()


  def remove_tail(self):
    removed_tail = self.tail_node

    if removed_tail == None:
      return None
    self.tail_node = removed_tail.get_prev_node()

    if self.tail_node != None:
      self.tail_node.set_next_node(None)

    if removed_tail == self.head_node:
      self.remove_head()
    return removed_tail.get_value()

  def remove_by_value(self, value_to_remove):
    node_to_remove = None
    current_node = self.head_node

    while current_node != None:
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
        break
      current_node = current_node.get_next_node()

    if node_to_remove == None:
      return None

    if node_to_remove == self.head_node:
      self.remove_head()
    elif node_to_remove == self.tail_node:
      self.remove_tail()
    else:
      next_node = node_to_remove.get_next_node()
      prev_node = node_to_remove.get_prev_node()
      next_node.set_prev_node(prev_node)
      prev_node.set_next_node(next_node)
    return node_to_remove

  def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list


# ## Node + Doubly Linked Lists

# In[ ]:


class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value

class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None
  
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node
    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)
    self.head_node = new_head
    if self.tail_node == None:
      self.tail_node = new_head


  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node
    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)
    self.tail_node = new_tail
    if self.head_node == None:
      self.head_node = new_tail



  def remove_head(self):
    removed_head = self.head_node

    if removed_head == None:
      return None
    self.head_node = removed_head.get_next_node()

    if self.head_node != None:
      self.head_node.set_prev_node(None)

    if removed_head == self.tail_node:
      self.remove_tail()
    return removed_head.get_value()


  def remove_tail(self):
    removed_tail = self.tail_node

    if removed_tail == None:
      return None
    self.tail_node = removed_tail.get_prev_node()

    if self.tail_node != None:
      self.tail_node.set_next_node(None)

    if removed_tail == self.head_node:
      self.remove_head()
    return removed_tail.get_value()

  def remove_by_value(self, value_to_remove):
    node_to_remove = None
    current_node = self.head_node

    while current_node != None:
      if current_node.get_value() == value_to_remove:
        node_to_remove = current_node
        break
      current_node = current_node.get_next_node()

    if node_to_remove == None:
      return None

    if node_to_remove == self.head_node:
      self.remove_head()
    elif node_to_remove == self.tail_node:
      self.remove_tail()
    else:
      next_node = node_to_remove.get_next_node()
      prev_node = node_to_remove.get_prev_node()
      next_node.set_prev_node(prev_node)
      prev_node.set_next_node(next_node)
    return node_to_remove

  def stringify_list(self):
    string_list = ""
    current_node = self.head_node
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list


# ## Enqueue + Dequeue w Node Practice

# In[ ]:


from node import Node
class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
    
  def enqueue(self, value):
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
      else:
        self.tail.set_next_node(item_to_add)
        self.tail = item_to_add
      self.size += 1
    else:
      print("Sorry, no more room!")
      
  # Add your dequeue method below:    
  def dequeue(self):
    if self.get_size() > 0:
      item_to_remove = self.head
      print("Removing " + str(item_to_remove.get_value()) + " from the queue!")
      if self.get_size() == 1:
        self.head = None
        self.tail = None
      else:
        self.head = self.head.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("This queue is totally empty!")
  
  def peek(self):
    if self.is_empty():
      print("Nothing to see here!")
    else:
      return self.head.get_value()
  
  def get_size(self):
    return self.size
  
  def has_space(self):
    if self.max_size == None:
      return True
    else:
      return self.max_size > self.get_size()
    
  def is_empty(self):
    return self.size == 0
q = Queue()
q.enqueue("some guy with a mustache")
q.dequeue()


# In[ ]:




