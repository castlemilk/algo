# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        return "{} --> {}".format(self.val, self.next)

class Solution:
    """
    eg.1
    2 -----> 4 -----> 3 -----> None
    5 -----> 6 -----> 4 -----> None
    {0,7} -> {1,0} -> {0,7}
    val: 7
    next.val: 0
    pointer = {val: 7, next: 0}
    result = pointer

    val: 0+0
    next.val: 1
    pointer = {val: 0, next: 1}
    result.next = pointer
    result.val = result

    val: 1+7
    next.val: None or 0
    pointer = {val: 8, next: None}

        7 ----> 0 ----> 8 ----> None
        eg.2
        5 -----> None
        5 -----> None
    {1,0}
        1 -----> 0 ----> None
        eg.
        1 -----> 8 ----> None
        0 -----> None
    {0,1} -> {0,8}
        1 -----> 8 -----> None
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        v1 = l1
        v2 = l2
        result = None
        pointer = None
        while True:
            quotient, rem = divmod(v1.val+v2.val, 10)
            print("quotient: {}, rem: {}".format(quotient, rem))
            print("result.val: {}, result.next.val: {}".format(result.val if result else None, result.next.val if result else None))
            print("pointer.val: {}, pointer.next.val: {}".format(pointer.val if pointer else None, pointer.next.val if pointer else None))
            if pointer:
                pointer = ListNode(rem + pointer.next.val)
                pointer.next = ListNode(quotient)
                result = pointer
            else:
                pointer = ListNode(rem)
                pointer.next = ListNode(quotient)
                result = pointer
            print(result)
            print("-----")
            if v1.next == None and v2.next == None:
                return result
            v1 = v1.next if v1.next else ListNode(0)
            v2 = v2.next if v2.next else ListNode(0)

def makeList(l):
    n_prev = None
    for v in l:
        if n_prev:
            n_new = ListNode(v)
            n_new.next = n_prev
            n_prev = n_new
        else:
            n_prev = ListNode(v)
    return n_prev
def printList(l):
    print(l)

if __name__ == '__main__':
    l1 = makeList([3,4,2])
    l2 = makeList([4,6,5])
    
    printList(l1)
    printList(l2)
    print("-----")
    sol = Solution()
    res = sol.addTwoNumbers(l1,l2)
    # printList(res)
    # l1 = makeList([5])
    # l2 = makeList([5])
    # printList(l1)
    # printList(l2)
    # sol = Solution()
    # res = sol.addTwoNumbers(l1,l2)
    # printList(res)
    # l1 = makeList([8,1])
    # l2 = makeList([0,0])
    # printList(l1)
    # printList(l2)
    # sol = Solution()
    # res = sol.addTwoNumbers(l1,l2)
    # printList(res)
