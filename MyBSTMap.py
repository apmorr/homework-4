from BSTMap import BSTMap, BSTNode  # provided for you


# Inherit from BSTMap, but overload `newnode` to use this one instead
class MyBSTMap(BSTMap):

    def newnode(self, key, value=None):
        return MyBSTNode(key, value)  # overloads the `newnode` method to use MyBSTNode() instead of BSTNode()

    # TODO: implement the three methods below
    def __eq__(self, other):
        """ADD DOCSTRING"""
        if isinstance(other, MyBSTMap):     # determine if other object is instance of MyBSTMap
            if self.size() != other.size(): # check to see if the sizes of the BSTMaps are different
                return False
            else:
                return self.root._eq(other.root)    # call the _eq method to compare the subtrees
        else:
            return False

        # The heavy lifting here is done in the corresponding
        # function in MyBSTNode - just tell it which node to
        # start with.

    def frompreorder(self, L):
        if len(L) == 0:
            return MyBSTMap()
        else:
            root = MyBSTNode(L[0][0], L[0][1])      # build a root node
            i = 1
            while i < len(L) and L[1][0] < root.key:    # find the index of the first item larger that root.key
                i+=1
            root.left = MyBSTMap.frompreorder(L[1:i])    # recursively create left subtree with elements before i
            root.right = MyBSTMap.frompreorder(L[i:])   # recursively create right subtree with elements after i
            return MyBSTMap(root)

    def frompostorder(self, L):
        if len(L) == 0:
            return MyBSTMap()
        else:
            root = MyBSTNode(L[-1][0], L[-1][1])    # build a root node
            i = 0
            while i < len(L) - 1 and L[i][0] < root.key:    # locate the element with an index greater than root.key
                i += 1
            root.left = MyBSTMap.frompostorder(L[:i])       # recursively construct left subtree with elements before i
            root.right = MyBSTMap.frompostorder(L[i:-1])    # recursively construct right subtree with elements after i
            return MyBSTMap(root)



class MyBSTNode(BSTNode):
    newnode = MyBSTMap.newnode  # overloads the `newnode` method to use the correct Node class

    # TODO: implement the method below
    def __eq__(self, other):
        if isinstance(other, MyBSTNode): # checks if other objects is an instance
            if self.key == other.key and self.value == other.value:     # compare current node key-value pair
                if self.left is None and other.left is None:    # if both nodes don't have a left child
                    left_equal = True
                elif self.left is not None and other.left is not None:  # if both nodes have a left child
                    left_equal = self.left._eq(other.left)  # recursively compare left subtree
                else:   # if only one node has left child
                    left_equal = False

                if self.right is None and other.right is None:  # if both nodes don't have a right child
                    right_equal = True
                elif self.right is not None and other.right is not None:    # if both nodes have a right child
                    right_equal = self.right._eq(other.right)   # recursively compare right subtree
                else:   # if only one node has a right child
                    right_equal = False

                return left_equal and right_equal   # return True if left and right subtrees are equal
            else:
                return False


