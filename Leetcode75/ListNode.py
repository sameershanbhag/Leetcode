class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        """
        Print the linked list starting from the current node.
        """
        node = self
        result = ""
        while node:
            result += str(node.val) + " "
            node = node.next
        return result

    def populating(self, values: list):
        """
        Populating the linked list with values.
        """
        node = self
        for val in range(len(values)):
            node.val = values[val]
            if val != len(values) - 1:
                node.next = ListNode()
                node = node.next
        return self

    def __eq__(self, other):
        """
        Overriding the equality operator.
        """
        if isinstance(other, ListNode):
            return self.__str__() == other.__str__()
        return False
