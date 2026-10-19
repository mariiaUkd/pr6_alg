class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:

    def __init__(self):
        self.top = None
        self._size = 0

    def is_empty(self):
        return self.top is None

    def push(self, item):
        self.top = Node(item, self.top)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Стек порожній")
        node = self.top
        self.top = node.next
        self._size -= 1
        return node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("Стек порожній")
        return self.top.data

    def clear(self):
        self.top = None
        self._size = 0

    def count(self):
        n = 0
        current = self.top
        while current is not None:
            n += 1
            current = current.next
        return n

    def size(self):
        return self._size

    def toString(self):
        items = []
        current = self.top
        while current is not None:
            items.append(str(current.data))
            current = current.next
        return "[" + ", ".join(items) + "]"

    def __str__(self):
        return self.toString()


if __name__ == "__main__":
    s = Stack()
    print("Порожній стек:", s, "| size =", s.size(), "| count =", s.count())

    for x in (11, 22, 33):
        s.push(x)
        print(f"push({x}) ->", s)

    print("peek():", s.peek())
    print("toString():", s.toString())
    print("size():", s.size(), "| count():", s.count())

    print("pop():", s.pop(), "->", s)
    print("pop():", s.pop(), "->", s)
    print("size():", s.size())

    s.push(44)
    print("push(44) ->", s)

    s.clear()
    print("clear() ->", s, "| size =", s.size())

    try:
        s.pop()
    except IndexError as e:
        print("pop() на порожньому стеку:", e)