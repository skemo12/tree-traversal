import unittest
from node import Node
from tree import Tree

class Test_tree(unittest.TestCase):

    def test_tree_init(self):
        t = Tree()
        self.assertEqual(t.root, None)

    def test_tree_find(self):
        t = Tree()
        for i in range(6):
            t.add(i)
        self.assertEqual(t.find(5).data, 5)
        self.assertEqual(t.find(6), None)

if __name__ == '__main__':
	unittest.main()