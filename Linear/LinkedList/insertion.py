from LinkedListClassDir.LinkedListClass import LinkedList, Node

class InsertionLinkedList(LinkedList):
#add node at the front
    def push(self,new_data):
        """Function to insert a new node at the beginning 
        Time complexity of push() is O(1) as it does constant amount of work.
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

#Add a node after a given node:
    def insertAfter(self, prev_node, new_data):
        """Function to inserts a new node after the given prev_node
        Time complexity of insertAfter() is O(1) as it does constant amount of work.
        """
        #check given prev_node exists
        if prev_node is None:
            print("Given previous node is not exists in LinkedList")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

#add node at the end.
    def append(self, new_data):
        """Function to inserts a new node at the end
        Time complexity of append is O(n) where n is the number of nodes in linked list. Since there is a loop from head to end, the function does O(n) work.
        """
        new_node = Node(new_data)

        # If the Linked List is empty, then make the new node as head 
        if self.head is None:
            self.head = new_node
            return

        #else traverse till the last node 
        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node
        new_node.next = None


if __name__=='__main__': 
  
    # Start with the empty list 
    llist = InsertionLinkedList() 
  
    # Insert 6.  So linked list becomes 6->None 
    llist.append(6) 
  
    # Insert 7 at the beginning. So linked list becomes 7->6->None 
    llist.push(7)
  
    # Insert 1 at the beginning. So linked list becomes 1->7->6->None 
    llist.push(1)
  
    # Insert 4 at the end. So linked list becomes 1->7->6->4->None 
    llist.append(4) 
  
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
    llist.insertAfter(llist.head.next, 8) 
  
    print('Created linked list is:'),
    llist.printList() 