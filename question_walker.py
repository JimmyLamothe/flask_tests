import uuid
from node import Node, Tree
from random import randint

#Just a dictionary. As attributes are required, add them to the class to make contents clear.
class Tracker:
    current_node = None
    node_names = None

def random_tree(depth = 3, midrange = 3, variation = 2):
    tree = Tree()
    def random_name():
        return uuid.uuid4().hex
    def get_children():
        children = midrange + randint(-variation, variation)
        return children
    def create_children(node, depth, count = 0):
        if depth <= 0:
            return
        for child in range(get_children()):
            new_node = Node(random_name())
            count += 1
            print(new_node.name, count, depth)
            node.adopt(new_node)
            tree.node_list.append(new_node)
            create_children(new_node, depth - 1, count)
    root = Node(random_name())
    tree.root = root
    tree.node_list.append(root)
    create_children(root, depth)
    print(tree.get_node_index(root))
    print([node.name for node in tree.node_list])
    return tree

"""
#Function to walk down a question tree, or back up the tree if needed.
def question_walker(node):
    name = node.name
    children = node.children
    parent = node.parent
    if children:
        for index, child in enumerate(children):
            print(str(index + 1) + '. ' + child.name)
        answer = int(input('Choose child'))
        next = children[answer - 1]
        question_walker(next)
    else:
        print('End of tree')

question_walker(tree)
"""
