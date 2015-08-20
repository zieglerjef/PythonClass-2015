class Node:
	def __init__(self, val=None, nxt=None):
		self.value = int(val)
		self.next_node = nxt
	
	def __str__(self):
		return str(self.value)
	
	def set_next(self, new_next):
		self.next_node = new_next

class LinkedList:
	def __init__(self, value=None):
		self.front = None
		self.end = None
		self.length = 0
	
	def __str__(self):
		node = self.front
		output = ""
		while node:
			if node.next_node:
				output += str(node.value) + ", "
			else:
				output += str(node.value)
			node = node.next_node
		return output

	def addNode(self, new_value):
		new_node = Node(new_value)
		if self.front == None: self.front = new_node
		if self.end: self.end.next_node = new_node
		self.end = new_node
		self.length += 1
		return self.__str__()
    
	def addNodeAfter(self, new_value, after_node):
		head = self.front
		item = 2
		while item <= after_node:
			head = head.next_node
			item += 1
		head.next_node = Node(new_value, head.next_node)
		self.length += 1
		return self.__str__()
	
	def addNodeBefore(self, new_value, before_node):
		self.addNodeAfter(new_value, before_node-1)
		return self.__str__()
		
	def removeNode(self, node_to_remove):
		if node_to_remove < 1 or node_to_remove > self.length:
			print "Outside of range"
		elif node_to_remove == 1:
			self.front = self.front.next_node
			self.length -= 1
		elif node_to_remove == self.length:
			current_node = self.front
			item=2
			while item < self.length:
				current_node = current_node.next_node
				item += 1
			current_node = None
			current_node.next = current_node.next_node.next_node
			self.length -= 1
		else:
			current_node=self.front
			item=2
			while item <= node_to_remove:
				current_node = current_node.next_node
				item += 1
			current_node.value = current_node.next_node
			current_node.next_node = current_node.next_node.next_node
			self.length -= 1
		return self.__str__()
    
	def removeNodesByValue(self, value):
		current = self.front
		previous = None
		found = False
		while current and found is False:
			if current.value == value:
				found = True
			else:
				previous = current
				current = current.next_node
        	if current is None:
        		raise ValueError("Value not in list.")
        	if previous is None:
        		self.front = current.next_node
        	else:
        		previous.set_next(current.next_node)
		return self.__str__()

	def reverse(self):
		current = self.front									
		last = None
		while current:
			next = current.next_node
			current.next_node = last
			last = current
			current = next
		if self.front:										
			self.next_node = self.front
			self.front = last
		return self.__str__()