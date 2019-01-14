#Defines a node object. Done for fun, Anytree is better.
import json

class Node:
    def __init__(self, name, json_path = False, **kwargs):
        if json_path:
           with open(json_path, 'r') as json_file:
               dict = json.load(json_file)
        else:
            dict = kwargs
        self.name = name
        self.__dict__.update(dict)
        self.parent = self #Not actually true, but used to prevent traversing higher than root
        self.is_root = True #Use this instead of self.parent to test for root. FIX LATER
        self.children = []
        self.birth_order = 0
        
    def adopt(self, node):
        node.parent = self
        node.is_root = False
        node.birth_order = len(self.children)
        node.order = len(self.children)
        self.children.append(node)

    def new_parent(self, node):
        self.parent = node
        self.is_root = False
        self.birth_order = len(self.parent.children)
        node.children.append(self)
    
    def get_index(self):
        if self.is_root == True:
            return '0'
        return self.parent.get_index() + ',' + str(self.birth_order)
            
    def get_depth(self):
        if self.is_root == True:
            return 0
        return self.parent.get_depth() + 1

    def json_save(self):
        start_dir = 'json/nodes'
        filename = self.name + '.json'
        with open(start_dir + filename, 'w') as json_file:
            json.dump(self.__dict__, json_file)
    
    #Only prints downwards
    def print_tree(self):
        result = ''
        try:
            result += str(self.parent.name)
            result += '/'
        except AttributeError:
            result += 'root'
            result += ':'
        result += self.name
        print(result)
        for child in self.children:
            child.print_tree()

#Test class for tree - used to track nodes client-side (JSON only, no objects)
class Tree:
    def __init__(self):
        self.root = None
        self.node_list = [] #List of Node objects in tree

    #Used to track current node client-side.
    def get_node_index(self, node):
        node_names = [node.name for node in self.node_list]
        index = node_names.index(node.name)
        return index


"""    
    def __repr__(self): #Shamelessly stolen from Anytree - Thank you!
        args = ["%r" % self.separator.join([""] + [str(node.name)
                                                   for node in self.path])]
        return _repr(self, args=args, nameblacklist=["name"])
"""
#moved to questions.py
"""
class Question(Node): #Node with obligatory content attribute
    def __init__(self, name, content, json_path = False, **kwargs):
        Node.__init__(self, name, json_path, **kwargs)
        self.content = content #either filepath or list

def get_question_dict(filename):
    start_dir = 'json/questions/'
    filepath = start_dir + filename
    with open(filepath, 'r') as json_file:
        question_dict = json.load(json_file)
    return question_dict

#Function to walk down a question tree.
#Question is a node object.
#End branch content is a list: [function, *args] called as function(*args).
def question_walker(question):
    content = question.content
    if type(content) == str:
        question_dict = get_question_dict(content)
        answer = int(ask_question(question_dict)) #ask next question
        return question_walker(question.children[answer])
    elif type(content) == lst:
        return content[0](content[1:]) #call function - RETURN necessary???
"""
