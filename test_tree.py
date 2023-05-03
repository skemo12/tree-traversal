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

    def test_tree_find_2(self):
        t = Tree()
        for i in range(10):
            t.add(i)
        self.assertEqual(t.find(1).data, 1)
        self.assertEqual(t.find(2).data, 2)
        self.assertEqual(t.find(3).data, 3)
        self.assertEqual(t.find(4).data, 4)
        self.assertEqual(t.find(5).data, 5)
        self.assertEqual(t.find(11), None)

if __name__ == '__main__':
	unittest.main()