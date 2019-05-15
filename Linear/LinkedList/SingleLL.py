#node class
class Node:
	def __init__(self,data):
	    self.data = data  # Assign data 
	    self.next = None  # Initialize next as null 

#Linked list class Node object
class LinkedList:
	def __init__(self):
		self.head = None
		
	def printList(self):
		""" This function prints contents of linked list """
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next
		
if __name__ == '__main__':
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)
	llist.head.next = second
	second.next = third

	llist.printList()