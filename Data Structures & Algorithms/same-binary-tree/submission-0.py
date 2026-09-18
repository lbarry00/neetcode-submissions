# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True

        queue = deque()
        queue.append([p, q])

        while queue:
            p_node, q_node = queue.pop()

            if not p_node and not q_node:
                continue
            elif p_node and not q_node:
                return False
            elif not p_node and q_node:
                return False
            elif p_node.val != q_node.val:
                return False
            
            queue.append([p_node.left, q_node.left])
            queue.append([p_node.right, q_node.right])

        return True