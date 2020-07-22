from LinkedList import LinkedList

class Stack(object):
    def __init__(self, top=None):
        self.linked_list = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.linked_list.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.linked_list.delete_first()