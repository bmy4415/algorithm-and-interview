# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def listToInt(node):
            """
            read whole linked list and return corresponding integer
            """
            digit = 0
            number = 0
            curr_node = node
            while curr_node:
                number += pow(10, digit) * curr_node.val
                curr_node = curr_node.next
                digit += 1
                
            return number
        
        def intToList(num):
            """
            return linked list which represents integer
            """
            root_node = ListNode(num % 10)
            curr_node = root_node
            num //= 10
            while num:
                next_node = ListNode(num % 10)
                curr_node.next = next_node
                curr_node = next_node
                num //= 10
                
            return root_node
        
        num1 = listToInt(l1)
        num2 = listToInt(l2)

        return intToList(num1 + num2)


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
sol = Solution()
answer = sol.addTwoNumbers(l1, l2)

while answer:
    print(answer.val)
    answer = answer.next