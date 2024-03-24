# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution(object):
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		prev_node = None  
		current_node = head 
		
		while current_node:
			next_node = current_node.next # proximo nó do nó atual
			current_node.next = prev_node # nó atual vai apontar pro de tras
			prev_node = current_node # na proxima iteracao, nó anterior vai ser o nó atual nessa iteracao
			current_node = next_node # passando pro proximo node
		
		return prev_node # retornando a nova "haed"
	
	def printList(self, node):
		while node:
			print(node.val)
			node = node.next

# 1 -> 2 -> 3
# 3 -> 2 -> 1 
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

solution = Solution()
reversed_list = solution.reverseList(head)
solution.printList(reversed_list)



