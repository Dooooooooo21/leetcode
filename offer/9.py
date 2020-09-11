class CQueue(object):

    def __init__(self):
        self.size = 0
        self.stack = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        self.size += 1

    def deleteHead(self):
        """
        :rtype: int
        """
        if self.size > 0:
            top = self.stack.pop(0)
            self.size -= 1
            return top
        else:
            return -1


obj = CQueue()
obj.appendTail(5)
obj.appendTail(2)
param_5 = obj.deleteHead()
param_2 = obj.deleteHead()
print(param_5)
print(param_2)
