#coding:utf-8
class Stack(object):
    def __init__(self):
        self.__list=[]
    def push(self,item):
        """添加一个新的元素到栈顶"""
        self.__list.append(item)

    def pop(self):
        """弹出栈顶的元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None
    def is_empty(self):
        """判断栈是否为空"""
        # if self.__list:
        #     return  True
        # else:
        #     return  False
        return self.__list==[]
    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)


if __name__=="__main__":
    s=Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.is_empty())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())