# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        newList = []     
        queue = [root]

        if root is None:
            return newList

        while queue:
            subList = []
            levelSize = len(queue)

            for _ in range(levelSize):
                node = queue.pop(0)

                if node is None:
                    continue
            
                subList.append(node.val)

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

            newList.append(subList)
        return newList
        