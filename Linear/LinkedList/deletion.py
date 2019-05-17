from linkedlistpushtemplate import LinkedListPushTemplate

class DeletionLinkedList(LinkedListPushTemplate):
    def deleteNode(self, key):
        """ Given a reference to the head of a list and a key, 
        delete the first occurence of key in linked list """

        # If linked list is empty 
        if self.head == None: 
            return 

        temp = self.head

        # If head node itself holds the key to be deleted 
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the previous node as we need to change 'prev.next
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        #if key was not present in linked list
        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def deleteList(self):
        """ delete all  the nodes of singly linked list """
        current = self.head
        while current:
            prev = current.next
            del current.data
            current = prev

# Driver program 
llist = DeletionLinkedList() 
llist.push(7) 
llist.push(1) 
llist.push(3) 
llist.push(2) 
  
print("Created Linked List: ")
llist.printList() 
llist.deleteNode(1)  
print("\nLinked List after Deletion of 1:")
llist.printList() 
print("\n Deleting linked list") 
llist.deleteList()       
print("Linked list deleted") 
            