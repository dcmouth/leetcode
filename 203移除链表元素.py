"""
删除链表中等于给定值 val 的所有节点。
示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # # #一个链表的节点由三个维度来描述。1、本节点的物理地址。2、本节点的val。3、指向的下一个节点的地址。
        # sentinel = ListNode(0)  #生成一个哨兵节点，并且给这个节点val赋值为0，直接打印，这个节点就是一个内存地址。
        # sentinel.next = head    #把这个节点的指针指向下一个节点，其实指向的是下一个节点的地址
        # kk = sentinel
        # mm = sentinel.next
        # # print(sentinel.next)
        # # print(sentinel.next.val)
        #
        # prev =  sentinel
        # curr =   head
        # while curr:
        #     if curr.val == val:
        #         prev.next = curr.next
        #     else:
        #         prev = curr
        #     curr = curr.next
        # return sentinel.next    #返回的是真正链表的第一个节点，给了头就相当于给了整个链表了
        
        sentinel = ListNode(0)  #生成一个哨兵节点，并且给这个节点val赋值为0，直接打印，这个节点就是一个内存地址。
        sentinel.next = head    #把这个节点的指针指向下一个节点，其实指向的是下一个节点的地址
        kk = sentinel
        mm = sentinel.next
        
        

l11 = ListNode()
l12 = ListNode()
l13 = ListNode()
l21 = ListNode()
l22 = ListNode()
l23 = ListNode()

l11.__init__(4,l12)
l12.__init__(2,l13)
l13.__init__(1,None)


val = 4
a = Solution()
c = a.removeElements(l11,val)
print(c.val)
print(c.next.val)


