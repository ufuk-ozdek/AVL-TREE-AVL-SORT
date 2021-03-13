class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AvlTree:
    def insert_node(self, root, key):
        if not root:
            return Node(key)
        else:
            if key < root.key:
                root.left = self.insert_node(root.left, key)
            else:
                root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.height_of_node(root.left), self.height_of_node(root.right))
        if self.balance(root) > 1:
            # left-left
            if key < root.left.key:
                root = self.right_rot(root)
                return root
            # left-right
            else:
                root.left = self.left_rot(root.left)
                root = self.right_rot(root)
                return root
        elif self.balance(root) < -1:
            # right-right
            if key > root.right.key:
                root = self.left_rot(root)
                return root
            # right-left
            else:
                root.right = self.right_rot(root.right)
                root = self.left_rot(root)
                return root

        return root

    def deletion(self, root, key):
        if not root:
            return
        elif key < root.key:
            root.left = self.deletion(root.left, key)
        elif key > root.key:
            root.right = self.deletion(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.get_min(root.right)
            root.key = temp.key
            root.right = self.deletion(root.right, temp.key)

        root.height = 1 + max(self.height_of_node(root.left),
                              self.height_of_node(root.right))

        if self.balance(root) > 1:
            if self.balance(root.left) >= 0:
                return self.right_rot(root)
            else:
                root.left = self.left_rot(root.left)
                return self.right_rot(root)
        if self.balance(root) < -1:
            if self.balance(root.right) <= 0:
                return self.left_rot(root)
            else:
                root.right = self.right_rot(root.right)
                return self.left_rot(root)
        return root

    def get_min(self, root):
        if not root.left:
            return root
        return self.get_min(root.left)

    def height_of_node(self, root):
        if not root:
            return 0
        else:
            return root.height

    def balance(self, root):
        if not root:
            return 0
        else:
            return self.height_of_node(root.left) - self.height_of_node(root.right)

    def left_rot(self, root):
        y = root.right
        T2 = y.left
        root.right = T2
        y.left = root
        root.height = 1 + max(self.height_of_node(root.left), self.height_of_node(root.right))
        y.height = 1 + max(self.height_of_node(y.left), self.height_of_node(y.right))
        return y

    def right_rot(self, root):
        y = root.left
        T2 = y.right
        root.left = T2
        y.right = root
        root.height = 1 + max(self.height_of_node(root.left), self.height_of_node(root.right))
        y.height = 1 + max(self.height_of_node(y.left), self.height_of_node(y.right))
        return y

    def inorder(self, root):
        if root.left is not None:
            self.inorder(root.left)
        print(root.key, end=' ')
        if root.right is not None:
            self.inorder(root.right)

    def proper(self, root):
        if not root:
            return
        print(root.key)
        return self.proper(root.left), self.proper(root.right)


list_1 = [83, 2, 4, 9, 3, 8, 6, 1, 13, 10, 17, 21, 93, 12]
root = None
avl = AvlTree()

for i in list_1:
    root = avl.insert_node(root, i)

root = avl.deletion(root, key=17)

avl.inorder(root)
