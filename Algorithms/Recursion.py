'''Implementing a function to get fibonacci numbers at a given index in the sequence '''
def get_fib(position):
    ans = 0
    if position == 0 or position == 1:
        return position
    else:
        return get_fib(position-1) + get_fib(position-2)
'''
Fibonacci sequence: 0,1,1,2,3,5,8,13,21,34,...
Index starts at 0 so at position 0 it's 0, at position 9 it's 34, and on 11 is 89 ...
'''
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))