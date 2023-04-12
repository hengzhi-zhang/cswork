#  File: Josephus.py
#  Student Name: Ethan Mason
#  Student UT EID: em45486
#  Partner Name: Hengzhi Zhang
#  Partner UT EID: hz6984
#  Course Name: CS 313E
import sys

# This class represents one soldier. 
class Link(object):
    # Constructor
    def __init__ (self, data=None):
        self.data = data         #Each node has an integer value, named data
        self.next = None         #and a pointer to the next node in a list
                
    def __str__(self):
        return str(self.data)
  
    
class CircularList(object):
    # Constructor
    def __init__ (self, data= None):    
        self.head = Link(1)            #Sets head of list to 1
        self.tail = self.head          #Sets tail to head because list has size 1
        self.tail.next = self.head     #Connects head and tail
        
        for i in range(2, data+1):     #Adds data number of nodes to the list
            curr_node = Link(i)
            self.insert(curr_node)
        
        curr_node = self.head
        while curr_node.next != self.head:  #Iterates through list to approriately assign self.tail
            if curr_node.data == data:
                self.tail = curr_node
            curr_node = curr_node.next
                
        self.tail.next = self.head  #Connects the head and the tail of the list, making it circular
      
    # return the size of the list
    def get_size (self):
        if self.is_empty():         #Empty lists return size 0
            return 0
        
        curr_node = self.head       #Sets the position at the head of the list in order to count the number of elements
        size = 1
        
        while curr_node.next != self.head:      #While the list hasn't looped around to the front,
            size += 1                           #increment size by 1
            curr_node = curr_node.next          #Move forward in the list
            
        return size
    
    # returns true if empty, otherwise false
    def is_empty (self):
        if self.tail == None:                   #If there is no tail, the list is empty
            return True
        
        return False

    # Append an item at the end of the list
    def insert ( self, new_node ):
        if self.is_empty():
            self.head = new_node
            return
        
        curr_node = self.head                   #Beginning at the front of the list,
        
        while curr_node.next != self.head:      #move forward until the end is reached
            curr_node = curr_node.next
            
        curr_node.next = new_node               #Add the new node to the end of the list
        new_node.next = self.head
        self.tail = new_node                    #Set the tail as the new node
    
        
    # Find the node with the given data (value)
    # or return None if the data is not there
    def find ( self, data ):
        curr_node = self.head                   #Beginning at the front of the list,
        
        while curr_node.data != data:           #Check if the current node contains the target value
            if curr_node.next == self.head:     #If the end of the list is reached, return None
                return None
            curr_node = curr_node.next          #Otherwise, continue searching
            
        return curr_node.data
    
    # Delete a Link with a given data (value) and return the node
    # or return None if the data is not there
    def delete ( self, data ):                  
        curr_node = self.head                   #Beginning at the front of the list,
        
        while curr_node.next.data != data:      #Check if the target node follows current node
            if curr_node.next == self.head:     #If the end of the list is reached, return None
                return None
            curr_node = curr_node.next          #Otherwise, continue searching
        
        delete = curr_node.next                 #Saves the node to be deleted in a variable
        curr_node.next = curr_node.next.next    #Disconnects target note
        
        return delete.data                      #Returns the data of the node that was deleted
    
    # Delete the nth node starting from the start node
    # Return the data of the deleted node AND return the
    # next node after the deleted node in that order
    def delete_after ( self, start_count, count ):
        curr_node = self.head                   #Beginning at the front of the list,
            
        while curr_node.data != start_count:    #Move forward until the starting point is reached
            curr_node = curr_node.next
            
        while count > 2:                        #Locate the node to delete after
            curr_node = curr_node.next
            count -= 1
            
        deleted = curr_node.next                #Save the node to be deleted
        
        #If the list contains only one element, set tail to None in order to set list to empty
        if curr_node == self.head and curr_node == self.tail:   
            self.tail = None
        elif curr_node.next == self.head:       #If the node to be deleted is the head,
            self.head = curr_node.next.next     #reassign the head of the list to the following node
        elif curr_node.next == self.tail:       #If the node to be deleted is the tail,
            self.tail = curr_node               #reassign the head of the list to the previous node
            
        curr_node.next = curr_node.next.next    #Disconnect target node from list
        
        #Return the data of the deleted node, and the location of the next starting point
        return deleted.data, curr_node.next.data       
    
    
    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__ ( self ):
        output = '['
        curr_node = self.head
        
        while curr_node != self.tail:
            output += str(curr_node.data) + ', '
            curr_node = curr_node.next
            
        return output + str(self.tail.data) + ']'
    
def main():
      
    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('josephus.in')
    else:
        in_data = sys.stdin
  
    # read the three numbers from the file
    line = in_data.readline().strip()
    num_soldiers = int (line)
  
    line = in_data.readline().strip()
    start_count = int (line)

    line = in_data.readline().strip()
    count = int (line)

    # Add code here
    listy = CircularList(data = num_soldiers)       #Instantiates new CircualarList with num_soldiers elements
        
    #Assigns the data of the deleted node and the next starting point to a list
    while not listy.is_empty():
        output = []
        for i in listy.delete_after(start_count, count):
            output.append(i)
            
        #In order to print the deleted data and reassign the starting point
        print(str(output[0]))
        start_count = output[1]
            
         
  

if __name__ == "__main__":
  main()
