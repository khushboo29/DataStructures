#node class
class Node:
	# Constructor to initialize the node object 
	def __init__(self,data):
	    self.data = data  # Assign data 
	    self.next = None  # Initialize next as null 

#Linked list class Node object
class LinkedList:
	# Function to initialize head 
	def __init__(self):
		self.head = None
		
	def printList(self):
		""" This function prints contents of linked list """
		temp = self.head
		while(temp):
			print(temp.data, end=' ')
			temp = temp.next