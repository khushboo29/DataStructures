from linkedlistpushtemplate import LinkedListPushTemplate

class LengthLinkedList(LinkedListPushTemplate):
    def getCount(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

if __name__=='__main__': 
    llist = LengthLinkedList() 
    llist.push(1) 
    llist.push(3) 
    llist.push(1) 
    llist.push(2) 
    llist.push(1) 
    print ("Count of nodes is :",llist.getCount()) 
