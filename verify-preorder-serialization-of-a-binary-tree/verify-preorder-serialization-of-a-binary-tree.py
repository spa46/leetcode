class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        
        stack, count = [], 0
        p = preorder.split(",")
        
        for item in p:
            stack.append(item)
            count += 1
            #  if stack  the last two elements are #， it means that these two nodes are preceded by a leaf node 
            #  the two #  pop, set the leaf node as  None， namely #
            #  if it's a preorder traversal stack  # 
            while count > 1 and stack[-1] == "#" and stack[-2] == "#":
                stack.pop()
                stack.pop()
                if not stack: return False
                stack[-1] = "#"
                count -= 2
        #  stack  #  True.
        return True if len(stack) == 1 and stack[0] == "#" else False
        
        
        