from LinkedListClassDir.LinkedListClass import LinkedList, Node

class LinkedListPushTemplate(LinkedList):
    #add node at the front
    def push(self,new_data):
        """Function to insert a new node at the beginning 
        Time complexity of push() is O(1) as it does constant amount of work.
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node