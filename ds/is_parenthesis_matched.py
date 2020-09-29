from stack import Stack

def is_parenthesis_matched(expr):
    s = Stack()
    openers = '([{'
    closers = ')]}'
    
    for each in expr:
        if each in openers:
            s.push(each)
        if each in closers:
            if s.is_empty():
                return False
            if openers.index(s.pop()) != closers.index(each):
                return False
    
    return s.is_empty()