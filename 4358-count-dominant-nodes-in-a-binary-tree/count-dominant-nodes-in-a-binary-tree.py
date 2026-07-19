# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:

        def dfs(node):
            if not node:
                return -inf,0
                
            leftmx,leftcnt = dfs(node.left)
            rightmx,rightcnt = dfs(node.right)

            mx = max(node.val,leftmx,rightmx)

            cnt = leftcnt+rightcnt

            if node.val == mx:
                cnt+=1
            return mx,cnt
        ans = dfs(root)
        return ans[1]
    
                
        