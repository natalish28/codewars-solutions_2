class Solution:
    def deleteNode(self, root, key):
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        if key == root.val:
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            successor = root.right
            while successor.left is not None:
                successor = successor.left
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
            return root
        return root
