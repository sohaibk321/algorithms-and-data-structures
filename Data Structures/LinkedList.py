# A single unit in every linked list
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    '''
    Establilsh a linked list with head as the first item.
    If no item is given, then None is the first item
    '''
    def __init__(self, head=None):
        self.head = head
    "Add Elements into the end of the linked list"
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        counter = 1
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        counter = 1
        element_moved = None
        while counter <= position and current:
            if counter + 1 == position:
                element_moved = current.next
                current.next = new_element
                current.next.next = element_moved
                return current.next
            current = current.next
            counter += 1
    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def delete_first(self):
        deleted = self.head
        if self.head:
            self.head = self.head.next
            deleted.next = None
        return deleted