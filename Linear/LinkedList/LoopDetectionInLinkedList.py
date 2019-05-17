from linkedlistpushtemplate import LinkedListPushTemplate

class LoopDetection(LinkedListPushTemplate):
    def detectLoop(self):
        """ by hashing technique """
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return 
    
    def detectLoopByAlgo(self):
        """ by Floyd's cycle finding algorithm """
        slow_p = self.head
        fast_p = self.head
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print("Loop found in linked list")
                return

    def detectAndCountLoop(self):
        """ checks whether a given Linked List contains loop and if loop is present then returns count of nodes in loop """
        slow_p = self.head
        fast_p = self.head
        flag = 0 #to show that both slow and fast  
                 # are at start of the Linked List 
        while (slow_p and slow_p.next and fast_p and fast_p.next and fast_p.next.next):
            if slow_p == fast_p and flag != 0:
                count = 1
                slow_p = slow_p.next
                while (slow_p != fast_p):
                    slow_p = slow_p.next
                    count += 1
                return count
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            flag = 1
        return 0

    def detectAndRemoveLoop(self):
        """ this function will help to detect and remove the loop in linked list """
        slow = fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                self.removeLoop(slow)
                return 1
        return 0

    def removeLoop(self, loopnode):
        ptr1 = ptr2 = loopnode

        #count no. of nodes in the loop
        k=1
        while (ptr1.next != ptr2):
            ptr1 = ptr1.next
            k += 1
        
        #fix nodes
        ptr1 = self.head
        ptr2 = self.head
        for i in range(k):
            ptr2 = ptr2.next

        # Move both pointers at the same place 
        # they will meet at loop starting node 
        while(ptr2 != ptr1):
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        # Get pointer to the last node 
            ptr2 = ptr2.next

        # Set the next node of the loop ending node 
        # to fix the loop 
        ptr2.next = None


llist = LoopDetection()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(7)
llist.push(50)

# Create a loop for testing 
llist.head.next.next.next.next.next = llist.head.next.next
print("Linked List before removing loop")
#llist.printList() 

llist.detectAndRemoveLoop() 
  
print("Linked List after removing loop")
llist.printList() 
'''
if llist.detectLoop():
    print("Loop found")
else:
    print("Loop not found")
'''

#llist.detectLoopByAlgo()
#llist.detectAndCountLoop()
