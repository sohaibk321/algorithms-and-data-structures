from LinkedList import *

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Setup a LinkedList
test = LinkedList(e1)
test.append(e2)
test.append(e3)

# Test get_position
# Should print 3
print('Get position 3')
print(test.head.next.next.value)
# Should also print 3
print(test.get_position(3).value)

# Test insert
test.insert(e4,3)
# Should print 4 now
print(test.get_position(3).value)

# Test delete
test.delete(1)
# Should print 2 now
print(test.get_position(1).value)
# Should print 4 now
print(test.get_position(2).value)
# Should print 3 now
print(test.get_position(3).value)