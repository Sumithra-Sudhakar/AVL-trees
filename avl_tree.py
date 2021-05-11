class AvlTree:
	
	def __init__(self):
		self.root = None

	class Node:
		def __init__(self, key):
			self.key = key
			self.leftchild = None
			self.rightchild = None
			self.height = 1

	def getHeight(self, node):
		if node is None:
			return 0
		return node.height

	def leftRotate(self, node):
		right = node.rightchild
		rightsleft = right.leftchild
		right.leftchild = node
		node.rightchild = rightsleft
		node.height = 1 + max(self.getHeight(node.leftchild), self.getHeight(node.rightchild))
		right.height = 1 + max(self.getHeight(right.leftchild), self.getHeight(right.rightchild))
		return right

	def rightRotate(self, node):
		left = node.leftchild
		leftsright = left.rightchild
		left.rightchild = node
		node.leftchild = leftsright
		node.height = 1 + max(self.getHeight(node.leftchild), self.getHeight(node.rightchild))
		left.height = 1 + max(self.getHeight(left.leftchild), self.getHeight(left.rightchild))
		return left

	def getBalanceFactor(self, node):
		if node is None:
			return 0
		return self.getHeight(node.leftchild) - self.getHeight(node.rightchild)

	def insertElement(self, node, key):
		if node is None:
			return self.Node(key)
		elif key > node.key:
			node.rightchild = self.insertElement(node.rightchild, key)
		else:
			node.leftchild = self.insertElement(node.leftchild, key)

		node.height = 1 + max(self.getHeight(node.leftchild), self.getHeight(node.rightchild))
		bfactor = self.getBalanceFactor(node)

		if bfactor < -1 and key > node.rightchild.key:
			return self.leftRotate(node)

		elif bfactor > 1 and key < node.leftchild.key:
			return self.rightRotate(node)

		elif bfactor > 1 and key > node.leftchild.key:
			node.leftchild = self.leftRotate(node.leftchild)
			return self.rightRotate(node)

		elif bfactor < -1 and key < node.rightchild.key:
			node.rightchild = self.rightRotate(node.rightchild)
			return self.leftRotate(node)

		return node


	def deleteElement(self, node, key):
		if node is None:
			return node
		elif key < node.key:
			node.leftchild = self.deleteElement(node.leftchild, key)
		elif key > node.key:
			node.rightchild = self.deleteElement(node.rightchild, key)
		else:
			if node.leftchild is None:
				temp = node.rightchild
				node = None
				return temp
			elif node.rightchild is None:
				temp = node.leftchild
				node = None
				return temp
			else:
				temp = node.rightchild
				while temp.leftchild is not None:
					temp = temp.leftchild
				node.key = temp.key
				node.rightchild = self.deleteElement(node.rightchild, temp.key)

		if self.root is None:
			return self.root

		node.height = 1 + max(self.getHeight(node.leftchild), self.getHeight(node.rightchild))
		bfactor = self.getBalanceFactor(node)

		if bfactor < -1 and self.getBalanceFactor(node.rightchild) <= 0:
			return self.leftRotate(node)

		elif bfactor > 1 and self.getBalanceFactor(node.leftchild) >= 0:
			return self.rightRotate(node)

		elif bfactor > 1 and self.getBalanceFactor(node.leftchild) < 0:
			node.leftchild = self.leftRotate(node.leftchild)
			return self.rightRotate(node)

		elif bfactor < -1 and self.getBalanceFactor(node.rightchild) > 0:
			node.rightchild = self.rightRotate(node.rightchild)
			return self.leftRotate(node)

		return node


	def preorder(self, root):
		if not root:
			return
		print(root.key, end=" ")
		self.preorder(root.leftchild)
		self.preorder(root.rightchild)

def main():
  tree = AvlTree()
	 
  n = int(input())
	
  arr=list(map(int,input().strip().split()))[:n]

  for key in arr:

			tree.root = tree.insertElement(tree.root, key) 
			tree.preorder(tree.root)
			print()
		 

if __name__ == '__main__':
	main()