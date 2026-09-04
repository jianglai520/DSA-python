class Stack:
    def __init__(self):
        self._items = []   # 初始化空栈，下划线表示私有属性，不建议直接访问

    def push(self, item):
        """压栈"""
        self._items.append(item)

    def pop(self):
        """出栈，并返回栈顶元素"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """查看栈顶元素，不移除"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """判断栈是否为空"""
        return len(self._items) == 0

    def size(self):
        """返回栈的大小"""
        return len(self._items)

    def __repr__(self):
        """便于调试的字符串表示"""
        return f"Stack({self._items})"
